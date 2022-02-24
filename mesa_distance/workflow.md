# Workflow

## Data Extraction

Annotation data is extracted from the csv file into a pandas dataframe. Pandas offers a variety of powerful tools to analyse and filter this dataset for further use.

## Data Cleaning

### Select Images

We only consider images that have annotation data - and so extract all unique images with annotations attached from a given `.csv` file.

```python
df.drop_duplicates(subset='image_id', keep="last", inplace=True)
```

When only obtaining a list of the image IDs, to subsequently iterate through, we may simply use:

```python
images_ids = np.unique(df['image_id'])
```

Note that this may include images that have been marked as having no birds, these could be removed using:

```python
df.drop(df.index[np.isnan(df[["cluster_x", "cluster_y"]]).any()], inplace=True) 
```

However, I have retained these images to help avoid the model over-counting, and encourage the model to return a count of zero for images wth no birds in them, given this applies to a large portion of the dataset.

### Maintain Consistency

We subselect the year 2016 - the majority of our dataset was from this year anyway so we only lose <2% of the data. This is because a different camera was used in subsequent years, with a different aspect ratio, and so I wanted to avoid having to convert between the two image types, however this would be necessary for a larger scale model.

```python
annotation_df = annotation_df.loc[annotation_df['cam_id'].str.startswith('HVITa2016')]
```

## Run Model

The main model is contained within the `BirdCounting.m` file, and can be ran directly from there.