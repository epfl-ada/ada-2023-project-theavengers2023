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
## Causality between Revenue and Number of Actors
#### Research Objective:
The objective of this research is to investigate the impact of actor count on (log) revenue. However, numerous other variables could potentially confound causality, such as budget, country, language, publication year, and more. Consequently, we intend to analyze this effect conditionally with respect to the primary factors, including country, language, and budget magnitude.

To mitigate combinatorial explosion, we opt for a single group that maximizes the number of observations. The chosen features include:

- **Country of Production:** United States.
- **Language:** English.
- **Budget:** Magnitude equal to 10<sup>8</sup>, corresponding to revenues between 10<sup>7</sup> and 10<sup>8</sup>.

We exclude taking into account the year of publication due to the implementation of inflation, which already limits the impact of this variable.
In this analysis, the term "known" refers to actors who are sufficiently famous to be included in the database. By extension, these actors are those playing a significant role in the film.

<iframe src="assets/plots/boxplot_log_revenue.html" width="700" height="480" frameborder="0" position="relative"></iframe>

We discern a nuanced yet positive correlation between log revenue and the number of actors, albeit not prominently evident. To comprehensively assess this relationship, we will conduct a quantitative evaluation using statistical tests.



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

Finally, we have a list of useful actors who have a significant interaction with at least one other member of the list. We filter the list of films once again for our analysis. Indeed, we remove the films where none of the selected actors plays a role. Our database is now ready to reveal all the secrets that unveil which actor pairs add the most value to a film.

<iframe src="assets/plots/interactions_network.html" width="450px" height="330px" frameborder="0" position="relative"></iframe>

-----------------------------
