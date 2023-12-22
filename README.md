# Cinematic Connections: Unraveling the Influence of Actor Networks on Movie Success

## Abstract
Dive into the captivating world of cinema with our unique exploration of the CMU Movie Summary Corpus dataset. Tired of defending your love for the unparalleled duo of Ben Affleck and Matt Damon during your movie nights? You're in the right place! Our mission, should we decide to accept it (we do), takes you on a journey where we dissect connections between actors. Discover how these links influence financial success and film quality, while exploring aspects such as geography, timeline, and film genre. Thus, no more sterile debates about actor ensembles and dive into the data for an in-depth understanding of the seventh art. Get ready for an unprecedented cinematic adventure where the facts speak for themselves!


Visit our data story : [here](https://epfl-ada.github.io/ada-2023-project-theavengers2023/)

## Research Questions
Our approach aims to highlight redundant connections among certain actors and assess their financial and qualitative impact on films. This will enable film producers to make strategic decisions and, on the other hand, provide you with the necessary arguments to win your debates with cinephile friends

- Does an ensemble of renowned actors significantly influence a movie's revenue and critical acclaim?
- Which actor duos exhibit the most remarkable synergy, and which fall flat?
- How can we delineate the interconnectedness within actor networks?
- In relation to the above queries, do geographical, chronological, or genre-specific factors alter our findings?

## Aditionnal Datasets
- "The Movies Dataset" from Kaggle [1]: This dataset ressembles the one of CMU in terms of contents. We used this dataset to enrich the CMU dataset by filling its missing values. This would allow us to increase the robustness of the CMU dataset but also to expand and broadened our scope for analysis. It provided us with the means to conduct deeper and more precise evaluations of the cinematic information at hand.

- "IMDB Dataset" from Kaggle [2] : This dataset offers a wealth of information, including critical metrics like movie ratings and the volume of votes in line with IMDB standards. Such data points are key indicators of a film's success and popularity, providing valuable insights not present in the initial dataset.

- "Consumer price index (2010=100) - United States" from The World Bank [3] : This time series is useful to be able to compare appropriately the revenue accros the year. Adjusting revenue for inflation over the years is essential to provide a more accurate representation of the revenue made by the movies. This adjustment ensures that revenue figures are comparable across different periods (Enhanced by data provided by the Federal Reserve Bank of Minneapolis [4])

- "Oscar Nominations and Winners Dataset" from Kaggle [5]: To enrich our analysis and provide a comprehensive view of cinematic achievements, we incorporated a dataset detailing the history of Oscar nominations and winners. This dataset complements our existing sources by introducing critical acclaim aspects, allowing us to correlate box office success with industry recognition. 


Access all datasets on Google Drive using this link: [datasets](https://drive.google.com/drive/folders/1kKqpqdOm1F45n19MyqXFOTy_DvmOtbOA). To execute the `Project_milestone3.ipynb`  notebook, position the datasets folder in the same directory. 



## Methods
### t-tests
We employed t-tests to scrutinize the performance metrics of both renowned and non-renowned actors. These metrics encompassed the average rating and the average adjusted revenues attributed to a specific actor. Additionally, we leveraged t-tests to conduct an analysis based on movie genres. This involved exploring whether there exists a statistically significant difference in performance metrics between movies featuring renowned actors and those featuring non-renowned actors.

### Linear Regreesion (OLS)
We conducted Ordinary Least Squares (OLS) regression on various features, including adjusted budget. The dependent variables in this analysis were adjusted revenues and ratings. Our focus extended to evaluating the R-squared values and the significance of the regression coefficients. To ensure robustness, we employed the Monte Carlo method to obtain a reliable distribution of R-squared values based on an out-of-sample dataset. We also used linear regression to determine the performance of actors and pairs of actors on revenues and ratings. 

### Random Forest
We opted for a Random Forest as an alternative approach to traditional OLS regression. Prior to applying the Random Forest, we carefully selected various features to enhance its performance. Furthermore, we leveraged the power of the Random Forest to evaluate the features that exert the most influence on both revenues and ratings. Our assessment employed the Gini Impurity metric. Given the superior performance of Random Forest over OLS regression, particularly evident in the Out-of-sample $R^2$ metric, we utilized this method to predict the revenues of upcoming movies.

### Network analysis 

We embarked on a comprehensive Network analysis to distill renowned actors from the ensemble. Our analysis centered on quantifying the interactions each actor had with others, providing a visual representation of the interconnections and discerning patterns within the remaining actors. This proved pivotal in our analysis, enabling us to identify and address multicollinearity concerns arising from the Harry Potter Cast.

Employing three key metrics—Degree Centrality, Betweenness Centrality, and Closeness Centrality—we harnessed the power of network analysis to visually link actors sharing similar revenue profiles. This approach not only enriched our understanding of actor connections but also shed light on revenue patterns within this network.


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
Following a preliminary analysis encompassing the entire dataset, we delved into more nuanced examinations, meticulously controlling for potential biases. Factors such as country of origin, year of release, spoken languages, and movie budget were scrutinized to ensure a more refined analysis. Employing the consumer price index (CPI) to adjust revenues for inflation over time, we conducted linear regression models. These models sought to elucidate the influence of the number of actors per movie on both adjusted revenues and movie ratings. This approach allowed us to uncover more granular insights while addressing potential confounding variables.

#### 3.2. Feature importance and predicting models
Our objective was to identify the optimal model for revenue prediction, leveraging the available features. Employing both linear regression and the Random Forest method, we constructed models to discern the most effective predictor. Calculating the empirical distribution of out-of-sample $R^2$ for both models, we observed the superior performance of the Random Forest method over OLS regression. Utilizing Gini impurity as a metric, we identified the most influential features in explaining revenues and conducted a more in-depth analysis focused on these key variables.

### Part 4: 
#### 4.1. Chemistry 
At this stage, we will analyze "Which actor pairs have the best and worst chemistry?". Critical decisions must be made due to the necessity of reducing our actor sample. The challenge arises from the fact that, with the need for interactions between actors, the number of potential interactions among n people is [n(n-1)]/2. As n grows, the number of interactions becomes unmanageable. Consequently, we must carefully select the number of actors based on various considerations. It is acknowledged that we require actors who have collaborated sufficiently to generate significant interactions with their peers. However, determining the exact threshold depends on our specific objectives and preferences. Then, we can perform the regression of the interaction between actor to explain the revenues and ratings. 

### Part 5: 
### 5.1 Interconnection 
At this stage, we will use a network analyze to quantify the number of interactions between actors. That will provide an answer about the existence of communities and also an help to visualize these communities.
### 5.2 Forecast 
### Part 6:
Create the data story for our report.


## Proposed timeline

In order to answer the posed researched questions, we constructed a data analysis pipeline and the pipeline into 3 major parts as detailed in what follows:             


```
.
├── 23.11.22 - Filter the renowned actors by network analysis
│  
├── 25.11.22 - Study of the causality between the revenue and the number of actors 
│  
├── 27.11.22 - Prediction of the revenue in function of a set of variables
│  
├── 29.11.22 - Performed linear regession and random forests 
│  
├── 02.12.22 - Homework 2 deadline
│    
├── 05.12.22 - Classification of the pairs of actors
│  
├── 10.12.22 - Compare performance metrics of the renonwed and non renowned actors 
│  
├── 17.12.22 - Develop draft for data story
│  
├── 20.12.22 - Finalize code implementations and visualizations
│  
├── 21.12.22 - Finalize data story
│  
└── 22.12.22 - Milestone 3 deadline

```




## Organization within the team 

     Majda :      (1) Worked on the processing of the data, extraction and merging of the datasets.
                  (2) Worked on visualization of the raw data.
                  (3) Worked on the ranking of the actor pairs and their signicancy.
                  (4) Analysis of the regression
     ------------------------------------------------------------------------------------------------------------------------
     Julien :     (1) Worked on the processing of the data, extraction and merging of the datasets.       
                  (2) Implementation of the interaction matrix and first analysis with it 
                  (3) Linear regression of the interaction between actors
                  (4) additional linear regression
     ------------------------------------------------------------------------------------------------------------------------
      Louis :     (1) Worked on linear regression of the log-revenue and the rating in function of the numbner of known actors.
                  (2) Worked on the statistical impact of the models and parameters.
                  (3) Worked on the fitting of the functional form of the revenue and rating.
                  (4) Implementation and analysis of the linear regression
    ------------------------------------------------------------------------------------------------------------------------              
      Nathan :    (1) Worked on linear regression of the log-revenue and the rating in function of the numbner of known actors.
                  (2) Worked on the network analyze and the visualization of the interaction of actors.
                  (3) Worked on the fitting of the functional form of the revenue and rating.
                  (4) Implementation of the report and working for the data story 
     ------------------------------------------------------------------------------------------------------------------------             
      Albias :    (1) Worked on the processing of the data, extraction and merging of the datasets.
                  (2) Worked on the analyze of the raw data (distribution, mean, quantiles, statistics...).
                  (3) Worked on the ranking of the actor pairs and their signicancy.
                  (4) Implementation of the report and working for the data story
      ------------------------------------------------------------------------------------------------------------------------


## References 
1. [The Movies Dataset](https://www.kaggle.com/datasets/rounakbanik/the-movies-dataset?resource=download&select=movies_metadata.csv). Kaggle. 2017.  Accessed November 17, 2023.
2. [IMDb Dataset](https://www.kaggle.com/datasets/ashirwadsangwan/imdb-dataset). Kaggle. 2020. Accessed November 17, 2023.
3. ["Consumer price index (2010=100) - United States](https://data.worldbank.org/indicator/FP.CPI.TOTL?end=2022&locations=US&start=1960&view=chart). The World Bank. Accessed November 17, 2023. 
4. [Consumer Price Index, 1913-](https://www.minneapolisfed.org/about-us/monetary-policy/inflation-calculator/consumer-price-index-1913-). the Federal Reserve Bank of Minneapolis, Accessed November 21, 2023
5. [The Oscar Award, 1927 - 2023](https://www.kaggle.com/datasets/unanimad/the-oscar-award/data) Kaggle. 2023. Accessed November 28, 2023. 

