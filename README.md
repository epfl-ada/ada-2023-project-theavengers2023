# Cinematic Connections: Unraveling the Influence of Actor Networks on Movie Success

## Abstract
Dive into the captivating world of cinema with our unique exploration of the CMU Movie Summary Corpus dataset. Tired of defending your love for the unparalleled duo of Ben Affleck and Matt Damon during your movie nights? You're in the right place! Our mission, should we decide to accept it (we do), takes you on a journey where we dissect connections between actors. Discover how these links influence financial success and film quality, while exploring aspects such as geography, timeline, and film genre. Thus, no more sterile debates about actor ensembles and dive into the data for an in-depth understanding of the seventh art. Get ready for an unprecedented cinematic adventure where the facts speak for themselves!

## Research Questions
Our approach aims to highlight redundant connections among certain actors and assess their financial and qualitative impact on films. This will enable film producers to make strategic decisions and, on the other hand, provide you with the necessary arguments to win your debates with cinephile friends

- Does an ensemble of renowned actors significantly influence a movie's revenue and critical acclaim?
- Which actor duos exhibit the most remarkable synergy, and which fall flat?
- How can we delineate the interconnectedness within actor networks?
- In relation to the above queries, do geographical, chronological, or genre-specific factors alter our findings?

## Aditionnal Datasets
- "The Movies Dataset" from Kaggle [1]: This dataset ressembles the one of CMU in terms of contents. We used this dataset to enrich the CMU dataset by filling its missing values. This would allow us to increase the robustness of the CMU dataset but also to expand and broadened our scope for analysis. It provided us with the means to conduct deeper and more precise evaluations of the cinematic information at hand.

- "IMDB Dataset" from Kaggle [2] : This dataset offers a wealth of information, including critical metrics like movie ratings and the volume of votes in line with IMDB standards. Such data points are key indicators of a film's success and popularity, providing valuable insights not present in the initial dataset.

- "Consumer price index (2010=100) - United States" from The World Bank [3] : This time series is useful to be able to compare appropriately the revenue accros the year. Adjusting revenue for inflation over the years is essential to provide a more accurate representation of the revenue made by the movies. This adjustment ensures that revenue figures are comparable across different periods


Access all datasets on Google Drive using this link: [datasets](https://drive.google.com/drive/folders/1kKqpqdOm1F45n19MyqXFOTy_DvmOtbOA). To execute the `Project_milestone2.ipynb`  notebook, position the datasets folder in the same directory. 



## Methods

### Part 1:
#### 1.1. Data Visualization:
Our first task involves gaining a comprehensive understanding of the data. This entails visualizing various features within the created dataframe. Even features that may not directly impact our analysis should be examined to identify any potential hidden biases. The objective is to create a clear and insightful dataframe that will serve as a valuable resource throughout the entire project.

#### 1.2. Pre-processing:
During this stage, we will engage in pre-processing tasks to ensure the data is ready for analysis. This includes addressing any missing or inconsistent data, standardizing formats, and preparing the dataset for subsequent analytical steps.

Specifically, we are actively engaged with various datasets, including additional ones aimed at augmenting the richness of our project. Our efforts involve the meticulous removal of data noise, strategically undertaken to refine the dataset for our subsequent investigations. Our approach is characterized by a balance between precision and flexibility, aligning with our project objectives without imposing overly restrictive criteria.


### Part 2:
Moving forward in the project, we will delve into a more detailed examination of the relationship between actors and their respective movies.

#### 2.1 Analysis of Actor-Movie Dynamics:
Each movie involves a varying number of actors, and at this point, we aim to explore the intricacies of this relationship. We will initiate the investigation into the first research question, focusing on the impact of the number of actors per movie on their quality (measured by ratings) and revenue. The logarithm is applied on the revenues at this stage of the analysis. 

This two-part approach ensures a comprehensive exploration of the dataset, setting the stage for subsequent in-depth analyses. 

This part of the project is all about checking if our analysis might have problems or risks that could affect the project. Making sure the project is doable is really important. So, even if this step might seem unimportant, it's not. 

### Part 3:
#### 3.1. Improvement of the first analysis
The initial analysis conducted earlier requires refinement. We will enhance the approach by adjusting the revenues using the consumer price index (CPI), facilitating a more meaningful comparison of earnings for movie makers. Regression analyses involving variables such as the number of actors per film versus revenues (or the logarithm of revenues) and ratings will be performed. By the conclusion of this phase, we aim to provide a comprehensive answer to the first research question.

### Part 4: 
#### 4.1. Chemistry
At this stage, we will analyze "Which actor pairs have the best and worst chemistry?". Critical decisions must be made due to the necessity of reducing our actor sample. The challenge arises from the fact that, with the need for interactions between actors, the number of potential interactions among n people is [n(n-1)]/2. As n grows, the number of interactions becomes unmanageable. Consequently, we must carefully select the number of actors based on various considerations. It is acknowledged that we require actors who have collaborated sufficiently to generate significant interactions with their peers. However, determining the exact threshold depends on our specific objectives and preferences. Then, we can perform the regression of the interaction between actor to explain the revenues and ratings. 

### Part 5: 
### 5.1 Interconnection 
At this stage, we will use a network analyze to quantify the number of interactions between actors. That will provide an answer about the existence of communities and also an help to visualize these communities.

### Part 6:
Create the data story for our report.

#### T-test
A t-test will be used to compare the means of two groups (revenue and rating) and determine if there is a significant difference between them. It assesses whether the observed differences between the groups are likely to have occurred by chance or if they are statistically significant (alpha 5%).

#### F-test
The F-test will be used to evaluate hypotheses involving multiple parameters by comparing the fit of a more complex model (revenue or rating in function number of known actors) against a simplest model (average revenue or rating model). It assesses whether the additional parameters in the more complex model significantly improve the model fit, indicating if the added complexity is justified in explaining the observed data.

#### Linear regression
The linear regression will be applied to revenue or rating in function of dummy variables (0 known actor, 1 known actor, …). In our analysis, we are looking at the significance of the number of famous actors effect - globally (F-test) or variable per variable (t-tests).

#### Network Analysis
Useful for the understandability and visualization of the interaction between actors and highlight potential community of actors.



## Proposed timeline

In order to answer the posed researched questions, we constructed a data analysis pipeline and the pipeline into 3 major parts as detailed in what follows:             

17.11.2023 : Milestone 2 : End of part 1 & 2


24.11.2023 : Part 3


08.12.2023 : Part 4


15.12.2023 : Part 5


22.12.2023 : Milestone 3: Part 6



## Organization within the team 

     Majda :      (1) Worked on the processing of the data, extraction and merging of the datasets.
                  (2) Worked on visualization of the raw data.
                  (3) Worked on the ranking of the actor pairs and their signicancy.
                  (4) Analysis of the regression|
     ------------------------------------------------------------------------------------------------------------------------
     Julien :     (1) Worked on the processing of the data, extraction and merging of the datasets.       
                  (2) Implementation of the interaction matrix and first analysis with it 
                  (3) Linear regression of the interaction between actors
                  (4) additional linear regression
     ------------------------------------------------------------------------------------------------------------------------
      Louis :     (1) Worked on linear regression of the log-revenue and the rating in function of the numbner of known actors.
                  (2) Worked on the statistical impact of the models and parameters.
                  (3) Worked on the fitting of the functional form of the revenue and rating.
                  (4) Implementation and analysis of the linear regression|
    ------------------------------------------------------------------------------------------------------------------------              
      Nathan :    (1) Worked on linear regression of the log-revenue and the rating in function of the numbner of known actors.
                  (2) Worked on the network analyze and the visualization of the interaction of actors.
                  (3) Worked on the fitting of the functional form of the revenue and rating.
                  (4) Implementation of the report and working for the data story |
     ------------------------------------------------------------------------------------------------------------------------             
      Albias :    (1) Worked on the processing of the data, extraction and merging of the datasets.
                  (2) Worked on the analyze of the raw data (distribution, mean, quantiles, statistics...).
                  (3) Worked on the ranking of the actor pairs and their signicancy.
                  (4) Implementation of the report and working for the data story|
      ------------------------------------------------------------------------------------------------------------------------


## References 
1. [The Movies Dataset](https://www.kaggle.com/datasets/rounakbanik/the-movies-dataset?resource=download&select=movies_metadata.csv). Kaggle. 2017.  Accessed November 17, 2023.
2. [IMDb Dataset](https://www.kaggle.com/datasets/ashirwadsangwan/imdb-dataset). Kaggle. 2020. Accessed November 17, 2023.
3. ["Consumer price index (2010=100) - United States](https://data.worldbank.org/indicator/FP.CPI.TOTL?end=2022&locations=US&start=1960&view=chart). The World Bank. Accessed November 17, 2023. 


