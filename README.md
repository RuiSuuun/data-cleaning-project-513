# Data Cleaning project - 513
Team72:\
Shan Shan ([ss163@illinois.edu](mailto:ss163@illinois.edu))\
Anqi Chen ([ac89@illinois.edu](mailto:ac89@illinois.edu))\
Rui Sun ([ruisun6@illinois.edu](mailto:ruisun6@illinois.edu))

---
## Overview
The NYPL historic menus dataset is a mix of simple bibliographic descriptions of the menus and the culinary and economic content of the menus themselves. It is originally from http://menus.nypl.org/data. Based on the dataset, two U1 use cases are derived in our mind.

**Case 1: Which sponsors offer breakfast/lunch/dinner?**\
This case can be answered by clustering the “event” column. Currently, the data format in each category is not consistent. For example, there are DINNER vs dinner vs [DINNER], LUNCH vs LUNCHEON vs [LUNCH].  By cleaning the data, we should be able to query which sponsor offers which event.

**Case2:  Which sponsors are located in New York, NY?**\
This case can be answered by clustering the “place” column. Currently, there are different formats for each place. For example, there are NEW YORK, NY vs [NEW YORK, NY] vs NY. NASHVILLE, [TN?] vs NASHVILLE, TN. By cleaning the data, we should be able to query the location of each sponsor.

---
## Run YesWorkflow on Python Scripts
The YesWorkflow prototype is distributed as a jar (Java archive) file that can be executed using the java -jar command.\
Source: https://github.com/yesworkflow-org/yw-prototypes
### Pre-requisites
1. Java (JRE) version 1.7 or higher
2. Graphviz visualization software installed, *installation link: http://graphviz.org/Download.php*
3. YesWorkflow jar file, which is provided in git repo

### Generate and open YesWorkflow
1. Generate .gv graph
```
java -jar yesworkflow-0.2.0-jar-with-dependencies.jar graph project.py > yesWorkflow.gv
```
2. Generate PDF file based on .gv graph
```
dot -Tpdf yesWorkflow.gv -o yesWorkflow.pdf
```
3. Open PDF file
```
open yesWorkflow.pdf
```
<object data="yesWorkflow.pdf" type="application/pdf" width="100%">
</object>
