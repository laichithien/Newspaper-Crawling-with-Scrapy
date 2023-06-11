<!-- Title -->
<h1 align="center"><b>Newspaper Crawling with Scrapy</b></h1>
## Set up environment

```
conda env create -f environment.yaml
conda activate webcrawling
```

## Crawl
To crawl data from a newspaper site, you must first cd into that newspaper site folder, then the following command below will help you to do that

To crawl data from a newspaper site, navigate to the subfolder directory that corresponds to the name of the newspaper you want to crawl. Then, run the crawler using following command
```
scrapy crawl <crawler name> -o output.json
```
## Crawler name


| Crawler name | Newspaper name |
| ------------ | -------------- |
| VNE          | VNExpress      |
| Kenh14       | Kênh 14        |
