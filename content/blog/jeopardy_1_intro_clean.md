Title: Introduction to Jeopardy Dataset
Date: 2017-03-18 12:01
Category: Blog
Tags: jeopardy,
Slug: jeopardy-intro
Authors: Andrea Urban
Summary: Introducing and cleaning the Jeopardy dataset. What's in the dataset? Cleaning up the text data by removing links. Standardizing the dollar amounts after change in 2001.


{% notebook notebooks/jeopardy_1_intro_clean_data.ipynb cells[0:15] %}

![Artist's View of Lightning on Venus]({filename}/images/Artist_s_concept_of_lightning_on_Venus.jpg)

** Artist's Concept of Lightning on Venus **

*Image Credit: [J. Whatmore, ESA](http://www.esa.int/spaceinimages/Images/2007/11/Artist_s_concept_of_lightning_on_Venus2)*

{% notebook notebooks/jeopardy_1_intro_clean_data.ipynb cells[15:25] %}


For reasons that I don't quite understand, the [pelican plugin that renders the notebook on this blog](https://github.com/danielfrg/pelican-ipynb) interprets the html code. (I can see how this might actually be a feature and not a bug.) Anyway... this means I can't show the actual html tags in my dataframe as they appear in the notebook. However, if you look at the [notebook on github](linkehere) you will see it shown correctly. Until I figure this out, I'll include a hacked column that shows the html syntax as it appears in the notebook in the column labeled `question_htmlview`.

{% notebook notebooks/jeopardy_1_intro_clean_data.ipynb cells[25:] %}


That's it for cleaning the data. Next time, I'll take a look at answers about U.S. states and wikipedia.