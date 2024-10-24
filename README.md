<a href="https://datahub.io/core/seismic-bumps"><img src="https://badgen.net/badge/icon/View%20on%20datahub.io/orange?icon=https://datahub.io/datahub-cube-badge-icon.svg&label&scale=1.25)" alt="badge" /></a>

This is dataset about seismic bumps occurrences. This dataset contains csv
file in which is only header and data rows with no additional information 
about the dataset.

## Data

Dataset is gathered from [seismic-bumps Data Set](https://archive.ics.uci.edu/ml/datasets/seismic-bumps)

The data describe the problem of high energy (higher than 10^4 J) seismic bumps forecasting in a coal 
mine. Data come from two of longwalls located in a Polish coal mine.

Mining activity was and is always connected with the occurrence of dangers which are commonly called 
mining hazards. A special case of such threat is a seismic hazard which frequently occurs in many 
underground mines. Seismic hazard is the hardest detectable and predictable of natural hazards and in 
this respect it is comparable to an earthquake. More and more advanced seismic and seismoacoustic 
monitoring systems allow a better understanding rock mass processes and definition of seismic hazard 
prediction methods. Accuracy of so far created methods is however far from perfect. Therefore, it is 
essential to search for new opportunities of better hazard prediction, 
also using machine learning methods. Unbalanced distribution of positive ("hazardous state") and negative 
("non-hazardous state") examples is a serious problem in seismic hazard prediction. Currently used 
methods are still insufficient to achieve good sensitivity and specificity of predictions. The task of 
seismic prediction can be defined in different ways, but the main aim of all seismic hazard assessment 
methods is to predict (with given precision relating to time and date) of increased seismic activity which 
can cause a rockburst. In the data set each row contains a summary statement about seismic activity in 
the rock mass within one shift (8 hours). If decision 
attribute has the value 1, then in the next shift any seismic bump with an energy higher than 10^4 J was 
registered. That task of hazards prediction bases on the relationship between the energy of recorded 
tremors and seismoacoustic activity with the possibility of rockburst occurrence. Hence, such hazard 
prognosis is not connected with accurate rockburst prediction. Moreover, with the information about the 
possibility of hazardous situation occurrence, an appropriate supervision service can reduce a risk of 
rockburst (e.g. by distressing shooting) or withdraw workers from the threatened area. Good prediction 
of increased seismic activity is therefore a matter of great practical importance. The presented data 
set is characterized by unbalanced distribution of positive and negative examples. In the data set there 
are only 170 positive examples representing class 1.

Instances: 2584 \
Attributes: 18 + class \
Missing Attribute Values: None
Class distribution: 
* hazardous state" (class 1)    :  170  (6.6%)
* non-hazardous state" (class 0): 2414 (93.4%) 


Field descriptions:
 1. seismic: result of shift seismic hazard assessment in the mine working obtained by the seismic 
method (a - lack of hazard, b - low hazard, c - high hazard, d - danger state);
 2. seismoacoustic: result of shift seismic hazard assessment in the mine working obtained by the 
seismoacoustic method;
 3. shift: information about type of a shift (W - coal-getting, N -preparation shift);
 4. genergy: seismic energy recorded within previous shift by the most active geophone (GMax) out of 
geophones monitoring the longwall;
 5. gpuls: a number of pulses recorded within previous shift by GMax;
 6. gdenergy: a deviation of energy recorded within previous shift by GMax from average energy recorded 
during eight previous shifts;
 7. gdpuls: a deviation of a number of pulses recorded within previous shift by GMax from average number 
of pulses recorded during eight previous shifts;
 8. ghazard: result of shift seismic hazard assessment in the mine working obtained by the 
seismoacoustic method based on registration coming form GMax only;
 9. nbumps: the number of seismic bumps recorded within previous shift;
10. nbumps2: the number of seismic bumps (in energy range [10^2,10^3)) registered within previous shift;
11. nbumps3: the number of seismic bumps (in energy range [10^3,10^4)) registered within previous shift;
12. nbumps4: the number of seismic bumps (in energy range [10^4,10^5)) registered within previous shift;
13. nbumps5: the number of seismic bumps (in energy range [10^5,10^6)) registered within the last shift;
14. nbumps6: the number of seismic bumps (in energy range [10^6,10^7)) registered within previous shift;
15. nbumps7: the number of seismic bumps (in energy range [10^7,10^8)) registered within previous shift;
16. nbumps89: the number of seismic bumps (in energy range [10^8,10^10)) registered within previous shift;
17. energy: total energy of seismic bumps registered within previous shift;
18. maxenergy: the maximum energy of the seismic bumps registered within previous shift;
19. class: the decision attribute - "1" means that high energy seismic bump occurred in the next shift 
("hazardous state"), "0" means that no high energy seismic bumps occurred in the next shift 
("non-hazardous state")

Data is located directory `data`

`data/seismic-bumps.csv`

Attributes are same as are were in input data

## Preparation

To get our output data several things are done to input data:
* header with description about the data is removed
* repetition of rows is removed

Run python script:

`scripts/main.py`

## License
Licensed under the [Public Domain Dedication and License][pddl] (assuming
either no rights or public domain license in source data).

[pddl]: http://opendatacommons.org/licenses/pddl/1.0/

### Citation
Sikora M., Wrobel L.: Application of rule induction algorithms for analysis of data collected by seismic 
hazard monitoring systems in coal mines. Archives of Mining Sciences, 55(1), 2010, 91-114.

### Donors and creators
Marek Sikora^{1,2} (marek.sikora@polsl.pl), Lukasz Wrobel^{1} (lukasz.wrobel@polsl.pl)
(1) Institute of Computer Science, Silesian University of Technology, 44-100 Gliwice, Poland
(2) Institute of Innovative Technologies EMAG, 40-189 Katowice, Poland