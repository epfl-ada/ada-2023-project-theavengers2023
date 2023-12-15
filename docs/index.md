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

### A New Measure of Stardom

In our cinematic saga, 'renowned' isn't just about who’s clinched the most Oscars or whose films have filled the most seats. We’re turning the camera to capture something different – the power of connections. Instead of counting trophies and tallying ticket sales, we’re spotlighting the stars who truly connect. Our measure of fame? The number of times actors collaborate on screen. It's the repeated partnerships, the shared scenes, and the collective performances that truly make an actor 'renowned' in our story. This fresh angle reveals the unsung heroes of Hollywood, the ones who might not always make headlines but are, in fact, the linchpins of the industry's most beloved tales. Let's roll the film on this network of narratives and uncover the real champions of the silver screen.

#### Crafting the Lens: Our Method for Identifying Renowned Actors

###### Step 1: Setting the Stage with Experience 

We start by considering actors who have been in at least 10 movies. Why? This threshold ensures that we're looking at actors with a substantial body of work, indicating both experience and sustained relevance in the industry. It's not just about having a moment in the spotlight; it's about consistent participation in the cinematic world.

###### Step 2:  Mapping the Connections

Next, we delve into the heart of our analysis - the interactions between actors. By mapping out how often actors work together, we're able to see who's really at the center of the industry's collaborative network. This isn't just about appearing on screen; it's about being a part of the creative partnerships that define cinema. We set a threshold for the number of interactions to focus on actors who are not only experienced but also integral to the network. Those below the threshold might have a presence, but they don't yet form crucial links in the industry's collaborative web.

###### Step 3: Weighing Their Influence and the Threshold of Renown

We integrate three key centrality metrics:
- **Degree Centrality**: Number of direct connections, indicating an actor's versatility.
- **Betweenness Centrality**: Actor's role as a bridge within the network, showcasing their ability to link diverse cinematic groups.
- **Closeness Centrality**: How close an actor is to all others, highlighting their accessibility in the industry.

By combining these metrics, we get a weighted centrality score that captures not just how connected an actor is, but how influential they are in bridging different parts of the industry and maintaining close ties across the network. This comprehensive measure allows us to identify the true linchpins of the cinematic universe. Finally, we apply a threshold to the weighted centrality scores. This step ensures that we're spotlighting those who are not just connected, but truly central to the fabric of the film industry.

-----------------------------
