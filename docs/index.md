---
layout: page
title: Cinematic connections - Unravelling the influence of Actor Networks on Movie Success
subtitle: Charting the Constellations of Cinema's Leading Lights
cover-img: /assets/img/background_img.png
thumbnail-img: /assets/img/background_img.png
share-img: /assets/img/background_img.png
use-site-title: true
---

Dive into the captivating world of cinema with our unique exploration of the CMU Movie Summary Corpus dataset. Tired of defending your love for the unparalleled duo of Ben Affleck and Matt Damon during your movie nights? You're in the right place! Our mission, should we decide to accept it (we do), takes you on a journey where we dissect connections between actors. Discover how these links influence financial success and film quality, while exploring aspects such as geography, timeline, and film genre. Thus, no more sterile debates about actor ensembles and dive into the data for an in-depth understanding of the seventh art. Get ready for an unprecedented cinematic adventure where the facts speak for themselves!

### Money Talks, But Let's Keep It Real
When we talk box office hits, we gotta make sure we're not comparing the '20s silent flicks to today's 3D extravaganzas without some tweaks. Money's worth more or less depending on when you're spending it, right? That's why we adjust the cash flow from back in the day to match today's dollars. It's like giving old movies a fair fight in today's box office arena.

Take a peek at this chart right here. Once we adjust for inflation, the old correlation between a movie's release year and its wallet—both what it cost and what it made—kinda fades away. But here's a kicker: the relationship between what a film spends and earns? Still cozy. The more a movie's budget balloons, the more it seems to rake in. Looks like spending big could mean earning big, but let's not forget—correlation isn't causation. So, let's not jump to conclusions just yet!

<iframe src="assets/plots/revenue-plot.html" width="750px" height="530px" frameborder="0" position="relative">Genre plot</iframe>
<iframe src="assets/plots/budget-plot.html" width="750px" height="530px" frameborder="0" position="relative">Genre plot</iframe>

-----------------------------
### Causality between Revenue and Number of Actors
#### Research Objective:

In our research, we set out to investigate the relationship between the number of actors in a movie and its (log) revenue. Our initial causal diagram suggests a straightforward link, but we recognize the potential influence of confounding variables like budget, country, language, and more. 

Indeed, it seems like we must have the following straightforward causality : 

<iframe src="assets/plots/Causal_Diagram_first.html" width="350" height="180" frameborder="0" style="display: block; margin: auto;"></iframe>

However, numerous other variables could potentially confound causality, such as budget. Consequently, we could have a diagram that considers budget as a confounder :

<iframe src="assets/plots/Causal_Diagram_second.html" width="350" height="280" frameborder="0" style="display: block; margin: auto;"></iframe>

Consequently, we intend to analyze this effect conditionally with respect to the primary factors, including country, language, and budget 
magnitude.
In order to exclude the effect of a possible counfounder, we try to look at a subgroup of movies that share the same country,language and  
budget magnitude. We do not exactly proceed with a matching because the number of movies for some countries is very low but we still try to 
find an effect of the number of known actors on the revenues within this subgroup.

To mitigate combinatorial explosion, we opt for the group that maximizes the number of observations. The chosen features include:

- **Country of Production:** United States.
- **Language:** English.
- **Budget:** Magnitude equal to 10<sup>8</sup>, corresponding to revenues between 10<sup>7</sup> and 10<sup>8</sup>.

We exclude taking into account the year of publication due to the implementation of inflation, which already limits the impact of this variable.
In this analysis, the term "known" refers to actors who are sufficiently famous to be included in the database. By extension, these actors are those playing a significant role in the film. We started with a visual exploration using boxplots :

<iframe src="assets/plots/boxplot_log_revenue.html" width="700" height="480" frameborder="0" position="relative"></iframe>

We discern a nuanced yet positive correlation between log revenue and the number of actors, albeit not prominently evident. To comprehensively assess this relationship, we will conduct a deeper quantitative evaluation using statistical tests.

#### Method : Linear Regression

The initial quantitative study involved performing a linear regression, examining the relationship between the number of actors with significant roles in a film and the corresponding adjusted revenue.

<iframe src="assets/plots/Beta_Values_and_confidence_intervals.html" width="800" height="500" frameborder="0" position="relative"></iframe>

Initially, the entire set of independent variables displayed significance in predicting the adjusted log-revenue (P(F-statistic) < 0.05). However, challenges emerged, such as low observations for some dummy variables. While the overall model was significant, none of the independent variables exhibited a significant impact (p-values > 0.05), indicating a high level of correlation among the variables.

To address these challenges and avoid drawing conclusions from an inconsistent model, our plan is to group the independent variables to reduce correlation.We aggregate the independent variables into groups of 5 actors, we obtain the following beta parameters :

<iframe src="assets/plots/Beta_Values_and_confidence_intervals2.html" width="800" height="500" frameborder="0" position="relative"></iframe>

The revised model maintained statistical significance, and a majority of the independent variables demonstrated a significant impact on log-revenue. Hence, within a movie group sharing the same language, country of production, and budget magnitude, we still discern an impact of the actor count on log-revenue.

We conclude that within the selected movie group sharing the same language, country, and budget magnitude, we observe a meaningful impact of actor count on log revenue. However, it is essential to note that these findings may not be universally applicable to other groups due to the inability to establish clean matches. 

----------------------------
### Prediction of the revenue in function of a set of variables 

The objective of this section is to construct models enabling us to forecast movie revenue by considering dependent variables such as the number of actors, the movie genre, the country of production, and other relevant factors. 
Within our dataset, numerous categorical and numerical variables capture our interest. Consequently, we generate dummy variables for each categorical variable.

Now, we have the following method, we iterate 1000 times. Each iteration unfolds as follows :
We divide our dataset in train/test set, a fundamental step for model evaluation. We perform an OLS regression with the train set. Then, we calculate the out-of-sample (with the test set) \(R^2\). This metric gauges how well our model generalizes to unseen data. After each iteration, we meticulously document the out-of-sample \(R^2\), allowing us to construct a distribution. This distribution gives a great picture of the model's performance variability. Below is our resulting plot :

A CHANGER !!!!
<iframe src="assets/plots/Distribution_of_the_R2_from_the_linear_regression.html" width="800" height="500" frameborder="0" position="relative"></iframe>

The distribution of \(R^2\) values provides us with valuable insights into the stability and reliability of our forecasting models.Indeed, by the central limit theorem it should follow : A COMPLETER !!!


A CHANGER !!!
<iframe src="assets/plots/Distribution_of_the_R2_from_the_random_forest.html" width="800" height="500" frameborder="0" position="relative"></iframe>

A CHANGER !!!
<iframe src="assets/plots/Feature_Importances_using_MDI.html" width="800" height="500" frameborder="0" position="relative"></iframe>

-----------------------------
### A New Measure of Stardom

In the context of our cinematic project, we aim to assess the significance of interactions among various actors. The objective is to quantify the value or impact of these interactions. To pinpoint noteworthy actor pairs, we adopted the following approach:


#### Crafting the Lens: Our Method for Identifying Renowned Actors

###### Step 1: Setting the Stage with Experience 

We start by considering actors who have been in at least 10 movies. Why? This threshold ensures that we're looking at actors with a substantial body of work, indicating both experience and sustained relevance in the industry. It's not just about having a moment in the spotlight; it's about consistent participation in the cinematic world.

<iframe src="assets/plots/percentage_actors_and_number_movies.html" width="700" height="480" frameborder="0" position="relative"></iframe>


###### Step 2: Filtration of Relevant Movies

Our goal is to enhance your movie night. Therefore, it is interesting to filter the films that are part of our dataframe. The criteria were as follows: The movie must have been translated or created in English. It must have been released after 1980. Thus, we now have a list of actors who have a role in one of the preselected films.

###### Step 3:  Mapping the Connections

Next, we delve into the heart of our analysis - the interactions between actors. By mapping out how often actors work together, we're able to see who's really at the center of the industry's collaborative network. This isn't just about appearing on screen; it's about being a part of the creative partnerships that define cinema. We set a threshold for the number of interactions to focus on actors who are not only experienced but also integral to the network. Those below the threshold might have a presence, but they don't yet form crucial links in the industry's collaborative web. Therefore, we decide to continue with pairs of actor that played in more than 5 movies together.

###### The Final Curation:

The endgame of our selection process yields a curated list of actors whose interactions bear the hallmark of significance. With the final filter applied, we eliminate any film devoid of our shortlisted actors' presence, sharpening the focus of our database. Now primed for the grand reveal, we stand on the brink of uncovering the enigmatic duo of actors that hold the keys to cinematic success.

<iframe src="assets/plots/interactions_network.html"  width="100%" height="700" frameborder="0" position="relative"></iframe>

The graph above corresponds to a network containing the 69 actors that will be useful for quantifying the power of interactions. Additional information can be obtained by hovering over the photo of an actor. The lines connecting two actors indicate an existing relationship between them. What we can observe is a cluster of significant points. These actors have the particularity of having worked together in the saga (Harry Potter), consisting of 8 films. The actors positioned more centrally in the network are those who interact with several different peers. Take, for example, Steve Buscemi, an actor with an extensive filmography in various cinematic genres, from comedy to action films, enabling him to collaborate with a significant number of his peers.

-----------------------------
### Forecasting
In the enchanting realm of cinema, the year 2024 promises a captivating array of films gracing screens around the globe. Amongst this cinematic tapestry, certain gems stand out, eagerly anticipated by audiences worldwide. If you aspire to be a cinematic trailblazer, ready to regale your friends with insights into the blockbusters set to dominate the box office, then this section is tailored just for you.

Here, we delve into the anticipation surrounding several films poised to take center stage in the cinematic landscape. Our endeavor extends beyond mere anticipation as we embark on the fascinating journey of predicting the revenues these cinematic marvels are destined to amass. Join us in this cinematic odyssey, where the magic of storytelling meets the allure of box office predictions.
