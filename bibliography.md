# Bibliography

This file contains a list of papers useful or relevant to this project, grouped by topic.

## Dot-Annotation Introduction

[[1]](https://openaccess.thecvf.com/content/ICCV2021W/ILDAV/html/Chen_Learning_to_Localise_and_Count_With_Incomplete_Dot-Annotations_ICCVW_2021_paper.html) Chen, F., Pound, M., French, A. (2021). Proceedings of the IEEE/CVF International Conference on Computer Vision (ICCV) Workshops, pp. 1612-1620

>_Proposes a method to allow deep networks to be trained on data with reduced numbers of annotations per image in heatmap regression tasks (e.g. object localisation and counting), by applying an asymmetric loss function. Helps reduce annotation workload, and also account for missing annotations (up to 90% in examples)_

[[2]](https://openaccess.thecvf.com/content/CVPR2021/html/Ranjan_Learning_To_Count_Everything_CVPR_2021_paper.html) Ranjan, V., Sharma, U., Nguyen, T., Hoai, M. (2021). Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), pp. 3394-3403

>_Poses counting as a few-shot regression task, and presents a novel method that takes a query image together with a few exemplar objects from the query image, predicting a density map for the presence of all objects of interest in the query image._

## Dot-Annotation Workflows

[[3]](https://www.robots.ox.ac.uk/~vgg/publications/2014/Arteta14/arteta14.pdf) Arteta C., Lempitsky V., Noble J.A., Zisserman A. (2014) Interactive Object Counting. In: Fleet D., Pajdla T., Schiele B., Tuytelaars T. (eds) Computer Vision – ECCV 2014. ECCV 2014. Lecture Notes in Computer Science, vol 8691. Springer, Cham. https://doi.org/10.1007/978-3-319-10578-9_33

>_Describes an interactive method to count (and localize) object instances in an image, targetting the regime where individual object detectors do not work reliably due to crowding, or overlap, or size of the instances, through an estimation of object density_

[[4]](https://projet.liris.cnrs.fr/imagine/pub/proceedings/ICPR-2012/media/files/0268.pdf) Fiaschi, L., Nair, R., Köthe, U., Hamprecht, F.A.. (2012). Learning to count with regression forest and structured labels. Proceedings - International Conference on Pattern Recognition. 2685-2688.

>_Introduces a method to estimate the object density map by averaging over structured, namely patch-wise, predictions. Using an ensemble of randomized regression trees that use dense features as input, they obtain results that are of similar quality, at a fraction of the training time, and with low implementation effort. Implemented within the framework of [ilastik](https://www.ilastik.org/documentation/counting/counting.html)._

[[5]](https://papers.nips.cc/paper/2010/file/fe73f687e5bc5280214e0486b273a5f9-Paper.pdf) Lempitsky, V. and Zisserman, A. (2010). Learning to count objects in images. In Proceedings of the 23rd International Conference on Neural Information Processing Systems - Volume 1 (NIPS'10). Curran Associates Inc., Red Hook, NY, USA, 1324–1332.

>_Proposes a new supervised learning framework for visual object counting tasks, such as estimating the number of cells in a microscopic image or the number of humans in surveillance video frames. They focus on the practical case when the training images are annotated with dots (one dot per object), and aim to accurately estimate the count. Instead of learning to detect and localize individual object instances, they cast the problem as that of estimating an image density whose integral over any image region gives the count of objects within that region. An implementation in MATLAB is [avaliable](https://www.robots.ox.ac.uk/~vgg/research/counting/index_org.html)._

[[6]](https://www.tandfonline.com/doi/full/10.1080/21681163.2016.1149104) Xie, W., Noble, J. A., Zisserman, A. (2018) Microscopy cell counting and detection with fully convolutional regression networks, Computer Methods in Biomechanics and Biomedical Engineering: Imaging & Visualization, 6:3, 283-292, https://doi.org/10.1080/21681163.2016.1149104

>_Specifically concering automated cell counting and detection in microscopy images, they use convolutional neural networks (CNNs) to regress a cell spatial density map across the image. This is applicable to situations where traditional single-cell segmentation-based methods do not work well due to cell clumping or overlaps. Since the networks are fully convolutional, they can predict a density map for an input image of arbitrary size, and this can be exploited to improve efficiency by end-to-end training on image patches._

## Wildlife Imaging

[[7]](https://www.nature.com/articles/sdata2018124) Jones, F., Allen, C., Arteta, C. et al. (2018). Time-lapse imagery and volunteer classifications from the Zooniverse Penguin Watch project. Sci Data 5, 180124. https://doi.org/10.1038/sdata.2018.124

>_Outlines an analogous approach to bird counting, using a sister dataset on Penguin populations, also from the Zooniverse Project. It also deals with variance between multiple annotators, and uses their variance to cope with varying size of target (depending on the scale of the image, or due to perspective shift within a single image)._

[[8]](https://www.robots.ox.ac.uk/~vgg/publications/2016/Arteta16/arteta16.pdf) Arteta, C., Lempitsky, V., Zisserman, A. (2016). Counting in The Wild. European Conference on Computer Vision

>_Describes the algorithm used in paper [7] in more detail. They used a multitask convolutional neural network to produce foreground/background segmentation, generate an object density function, and predict the agreement of this with annotations provided, using the [MatConvNet](https://www.vlfeat.org/matconvnet/) package._
