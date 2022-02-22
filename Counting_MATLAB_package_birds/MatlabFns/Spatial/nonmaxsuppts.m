% NONMAXSUPPTS - Non-maximal suppression for features/corners
%
% Non maxima suppression and thresholding for points generated by a feature
% or corner detector.
%
% Usage:   [r,c] = nonmaxsuppts(cim, Keyword-Value options...)
%                                                             
% Required argument:
%            cim    - Corner strength image.
%
% Optional arguments specified as keyword - value pairs:
%          'radius' - Radius of region considered in non-maximal
%                     suppression. Typical values to use might
%                     be 1-3 pixels. Default is 1.
%          'thresh' - Threshold, only features with value greater than
%                     threshold are returned. Default is 0.
%          'N'      - Maximum number of features to return.  In this case the
%                     N strongest features with value above 'thresh' are
%                     returned. Default is Inf.
%        'subpixel' - If set to true features are localised to subpixel
%                     precision. Default is false.
%          'im'     - Optional image data.  If an image is supplied the
%                     detected corners are overlayed on this image. This can
%                     be useful for parameter tuning. Default is [].
% Returns:
%            r      - Row coordinates of corner points.
%            c      - Column coordinates of corner points.
%
% Example of use:
% >> hes = hessianfeatures(im, 1);   % Compute Hessian feature image in image im
%
% Find the 1000 strongest features to subpixel precision using a non-maximal
% suppression radius of 2 and overlay the detected corners on the origin image.
% >> [r,c]= nonmaxsuppts(abs(hes), 'radius', 2, 'N', 1000, 'im', im, 'subpixel', true);
%
% Note: An issue with integer valued images is that if there are multiple pixels
% all with the same value within distance 2*radius of each other then they will
% all be marked as local maxima. 
%
% See also: HARRIS, NOBLE, SHI_TOMASI, HESSIANFEATURES

% Copyright (c) 2003-2016 Peter Kovesi
% Centre for Exploration Targeting
% The University of Western Australia
% peter.kovesi at uwa edu au
% 
% Permission is hereby granted, free of charge, to any person obtaining a copy
% of this software and associated documentation files (the "Software"), to deal
% in the Software without restriction, subject to the following conditions:
% 
% The above copyright notice and this permission notice shall be included in all
% copies or substantial portions of the Software.
%
% The Software is provided "as is", without warranty of any kind.

% September 2003  Original version
% August    2005  Subpixel localization and Octave compatibility
% January   2010  Fix for completely horizontal and vertical lines (by Thomas Stehle,
%                 RWTH Aachen University) 
% January   2011  Warning given if no maxima found
% January   2016  Reworked to allow the N strongest features to be returned.
%                 Arguments changed to be specified as keyword - value
%                 pairs. (no doubt this breaks some code, sorry)

function [r,c] = nonmaxsuppts(cim, varargin)
    
    [thresh, radius, N, subpixel, im] = checkargs(varargin);    
    [rows,cols] = size(cim);
    
    % Extract local maxima by performing a grey scale morphological
    % dilation and then finding points in the corner strength image that
    % match the dilated image and are also greater than the threshold.
    sze = 2*radius+1;                    % Size of dilation mask.
    mx = ordfilt2(cim, sze^2,ones(sze)); % Grey-scale dilate.

    % Make mask to exclude points within radius of the image boundary. 
    bordermask = zeros(size(cim));
    bordermask(radius+1:end-radius, radius+1:end-radius) = 1;
    
    % Find maxima, threshold, and apply bordermask
    cimmx = (cim==mx) & (cim>thresh) & bordermask;
    [r,c] = find(cimmx);        % Find row,col coords.
    
    % Check if we want to limit the number of maxima
    if isfinite(N)   
        mxval = cim(cimmx);         % Get values of maxima and sort them.
        [mxval,ind] = sort(mxval,1,'descend');   
        
        r = r(ind);                 % Reorder r and c arrays
        c = c(ind);                 % to match.
        
        if length(r) > N            % Grab the N strongest features.
            r = r(1:N);
            c = c(1:N);
        end
    end
    
    if isempty(r)     
        warning('No maxima above threshold found');
        return
    end
    
    if subpixel        % Compute local maxima to sub pixel accuracy  
        ind = sub2ind(size(cim),r,c);   % 1D indices of feature points
        w = 1;         % Width that we look out on each side of the feature
                       % point to fit a local parabola
        
        % Indices of points above, below, left and right of feature point
        indrminus1 = max(ind-w,1);
        indrplus1  = min(ind+w,rows*cols);
        indcminus1 = max(ind-w*rows,1);
        indcplus1  = min(ind+w*rows,rows*cols);
        
        % Solve for quadratic down rows
        rowshift = zeros(size(ind));
        cy = cim(ind);
        ay = (cim(indrminus1) + cim(indrplus1))/2 - cy;
        by = ay + cy - cim(indrminus1);
        rowshift(ay ~= 0) = -w*by(ay ~= 0)./(2*ay(ay ~= 0));       % Maxima of quadradic
        rowshift(ay == 0) = 0;
    
        % Solve for quadratic across columns    
        colshift = zeros(size(ind));
        cx = cim(ind);
        ax = (cim(indcminus1) + cim(indcplus1))/2 - cx;
        bx = ax + cx - cim(indcminus1);    
        colshift(ax ~= 0) = -w*bx(ax ~= 0)./(2*ax(ax ~= 0));       % Maxima of quadradic
        colshift(ax == 0) = 0;
    
        r = r+rowshift;  % Add subpixel corrections to original row
        c = c+colshift;  % and column coords.
    end
    
    if ~isempty(im)       % Overlay corners on supplied image.
        figure, imshow(im,[]), hold on
        plot(c,r,'r+'), title('corners detected');
        hold off
    end
end

%---------------------------------------------------------------
function [thresh, radius, N, subpixel, im] = checkargs(v)
    
    p = inputParser;
    p.CaseSensitive = false;
    
    % Define optional parameter-value pairs and their defaults    
    addParameter(p, 'thresh',       0, @isnumeric);  
    addParameter(p, 'radius',       1, @isnumeric);  
    addParameter(p, 'N',          Inf, @isnumeric);  
    addParameter(p, 'subpixel', false, @islogical);  
    addParameter(p, 'im',          [], @isnumeric);  

    parse(p, v{:});
    
    thresh   = p.Results.thresh;
    radius   = p.Results.radius;
    N        = p.Results.N;
    subpixel = p.Results.subpixel;
    im       = p.Results.im;    
    
end    