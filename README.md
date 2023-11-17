# Title

## Abstract
Dive into the captivating world of cinema with our unique exploration of the CMU Movie Summary Corpus dataset. Tired of defending your love for the unparalleled duo of Ben Affleck and Matt Damon during your movie nights? You're in the right place! Our mission, should we decide to accept it (we do), takes you on a journey where we dissect connections between actors. Discover how these links influence financial success and film quality, while exploring aspects such as geography, timeline, and film genre. Thus, no more sterile debates about actor ensembles and dive into the data for an in-depth understanding of the seventh art. Get ready for an unprecedented cinematic adventure where the facts speak for themselves!

## Research Questions
Our approach aims to highlight redundant connections among certain actors and assess their financial and qualitative impact on films. This will enable film producers to make strategic decisions and, on the other hand, provide you with the necessary arguments to win your debates with cinephile friends

- Does the rise of the number of famous actors has a significant impact on the revenue and the quality of a movie ?
- Which actor pairs have the best and worst chemistry ?
- Can we characterize the interconnetions between the actors ?
- Vis-a-vis to the previous questions, do we observe different conclusion in function of the geography, timeline, or film gender ?

## Aditional Datasets
The Movies Dataset on Kaggle : \url{https://www.kaggle.com/datasets/rounakbanik/the-movies-dataset/data}
This data is useful to enhance the revenues of the dataset. It contains information about 45'000 movies. Therefore, merging this dataset to the original dataset increases the number of value for the column "Revenu" by 19%. This is a significately improvement and justify the utilisation of this additional dataset. 

World Bank CPI : \url{https://data.worldbank.org/indicator/FP.CPI.TOTL?end=2022&locations=US&start=1960&view=chart}
This time series is useful to be able to compare appropriately the revenue accros the year. Adjusting revenue for inflation over the years is essential to provide a more accurate representation of the revenue made by the movies. This adjustment ensures that revenue figures are comparable across different periods.


IMDb dataset (*ToDo*)

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


# Part :
Create the data story to present our report. 

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

Organization within the team: A list of internal milestones up until project Milestone P3.


Questions for TAs (optional): Add here any questions you have for us related to the proposed project.


