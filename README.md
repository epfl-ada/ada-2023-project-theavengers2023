# Cinematic Connections: Unraveling the Influence of Actor Networks on Movie Success

## Abstract
Dive into the captivating world of cinema with our unique exploration of the CMU Movie Summary Corpus dataset. Tired of defending your love for the unparalleled duo of Ben Affleck and Matt Damon during your movie nights? You're in the right place! Our mission, should we decide to accept it (we do), takes you on a journey where we dissect connections between actors. Discover how these links influence financial success and film quality, while exploring aspects such as geography, timeline, and film genre. Thus, no more sterile debates about actor ensembles and dive into the data for an in-depth understanding of the seventh art. Get ready for an unprecedented cinematic adventure where the facts speak for themselves!

## Research Questions
Our approach aims to highlight redundant connections among certain actors and assess their financial and qualitative impact on films. This will enable film producers to make strategic decisions and, on the other hand, provide you with the necessary arguments to win your debates with cinephile friends

- Does an ensemble of renowned actors significantly influence a movie's revenue and critical acclaim?
- Which actor duos exhibit the most remarkable synergy, and which fall flat?
- How can we delineate the interconnectedness within actor networks?
- In relation to the above queries, do geographical, chronological, or genre-specific factors alter our findings?

## Aditional Datasets
- "The Movies Dataset" from Kaggle [1]: This dataset ressembles the one of CMU in terms of contents. We used this dataset to enrich the CMU dataset by filling its missing values. This would allow us to increase the robustness of the CMU dataset but also to expand and broadened our scope for analysis. It provided us with the means to conduct deeper and more precise evaluations of the cinematic information at hand.

- "IMDB Dataset" from Kaggle [2] : This dataset offers a wealth of information, including critical metrics like movie ratings and the volume of votes in line with IMDB standards. Such data points are key indicators of a film's success and popularity, providing valuable insights not present in the initial dataset.

- "Consumer price index (2010=100) - United States" from The World Bank [3] : This time series is useful to be able to compare appropriately the revenue accros the year. Adjusting revenue for inflation over the years is essential to provide a more accurate representation of the revenue made by the movies. This adjustment ensures that revenue figures are comparable across different periods


Access all datasets on Google Drive using this link: [datasets](https://drive.google.com/drive/folders/1kKqpqdOm1F45n19MyqXFOTy_DvmOtbOA). To execute the `Project_milestone2.ipynb`  notebook, position the datasets folder in the same directory. Below is the structure of the datasets provided:

```bash
/datasets
├──  MoviesSummaries
│ ├── character.metadata.tsv
│ └── movie.metadata.tsv
├── kaggle_movie
│ ├── movies_metadata.csv
│ └── ratings.csv
├── kaggle_imdb
│ ├── title.basics.tsv
│ └── title.ratings.tsv
└── Consumer price idex
  └── ....
```





## Methods

# Methods
## Part 1 
# Data Visualization:
Our first task involves gaining a comprehensive understanding of the data. This entails visualizing various features within the created dataframe. Even features that may not directly impact our analysis should be examined to identify any potential hidden biases. The objective is to create a clear and insightful dataframe that will serve as a valuable resource throughout the entire project.

# Pre-processing:
During this stage, we will engage in pre-processing tasks to ensure the data is ready for analysis. This includes addressing any missing or inconsistent data, standardizing formats, and preparing the dataset for subsequent analytical steps.

Specifically, we are actively engaged with various datasets, including additional ones aimed at augmenting the richness of our project. Our efforts involve the meticulous removal of data noise, strategically undertaken to refine the dataset for our subsequent investigations. Our approach is characterized by a balance between precision and flexibility, aligning with our project objectives without imposing overly restrictive criteria.

For instance, data points lacking revenue information or featuring a revenue of 0 are systematically excluded from the dataframe. Given that revenue constitutes a foundational element of our analysis, maintaining data integrity is crucial. On the other hand, when faced with missing year values—a constraint for the adjusted revenue metric we plan to utilize—we opt to retain these entries. To address this gap, we substitute the missing year with a coherent and reasoned value, ensuring the overall robustness of our dataset.


## Part 2: Exploring Actor-Movie Relationships
Moving forward in the project, we will delve into a more detailed examination of the relationship between actors and their respective movies.

# Analysis of Actor-Movie Dynamics:
Each movie involves a varying number of actors, and at this point, we aim to explore the intricacies of this relationship. We will initiate the investigation into the first research question, focusing on the impact of the number of actors per movie on their quality (measured by ratings) and revenue. The logarithm is applied on the revenues at this stage of the analysis. 

This two-part approach ensures a comprehensive exploration of the dataset, setting the stage for subsequent in-depth analyses. 

This part of the project is all about checking if our analysis might have problems or risks that could affect the project. Making sure the project is doable is really important. So, even if this step might seem unimportant, it's not. It's a way to be sure our analysis is strong and won't face unexpected issues that could mess up the whole project.

# DEADLINE MILESTONE 2

# Part 3 :
# Improvement of the first analysis
The initial analysis conducted earlier requires refinement. We will enhance the approach by adjusting the revenues using the consumer price index (CPI), facilitating a more meaningful comparison of earnings for movie makers. Regression analyses involving variables such as the number of actors per film versus revenues (or the logarithm of revenues) and ratings will be performed. By the conclusion of this phase, we aim to provide a comprehensive answer to the first research question.

# Part 4 : 
# Chemistry
At this stage, we will analyze "Which actor pairs have the best and worst chemistry?". Critical decisions must be made due to the necessity of reducing our actor sample. The challenge arises from the fact that, with the need for interactions between actors, the number of potential interactions among n people is [n(n-1)]/2. As n grows, the number of interactions becomes unmanageable. Consequently, we must carefully select the number of actors based on various considerations. It is acknowledged that we require actors who have collaborated sufficiently to generate significant interactions with their peers. However, determining the exact threshold depends on our specific objectives and preferences.
Then, we can perform the regression of the interaction between actor to explain the revenues and ratings. 

# Part 5: 
# Interconnection 


### T-test
Explanation later.

### F-test
Explanation later.

### ANOVA
Explanation later.

### Linear regression
Explanation later.

### Network Analysis
Explanation later.

## Proposed timeline

In order to answer the posed researched questions, we constructed a data analysis pipeline and the pipeline into 3 major parts as detailed in what follows:



## Organization within the team 

| Teammate | Contributions |
|   :---:  |    :---:      |
|   Majda |               |
|   Julien |               |
|   Louis |               |
|   Nathan |               |
|   Albias |               |

assign each task to team memebers

## Questions for TAs (optional): 
Add here any questions you have for us related to the proposed project.

## References 
1. [The Movies Dataset](https://www.kaggle.com/datasets/rounakbanik/the-movies-dataset?resource=download&select=movies_metadata.csv). Kaggle. 2017.  Accessed November 17, 2023.
2. [IMDb Dataset](https://www.kaggle.com/datasets/ashirwadsangwan/imdb-dataset). Kaggle. 2020. Accessed November 17, 2023.
3. ["Consumer price index (2010=100) - United States](https://data.worldbank.org/indicator/FP.CPI.TOTL?end=2022&locations=US&start=1960&view=chart). The World Bank. Accessed November 17, 2023. 


