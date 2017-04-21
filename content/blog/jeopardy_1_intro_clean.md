Title: Cleaning a Data Set, or Aaargh! Regular Expressions!
Date: 2017-04-18 12:01
Category: Blog
Tags: jeopardy, regular-expressions, data-cleaning
Slug: jeopardy-1-intro
Authors: Andrea Urban
Summary: *Introducing and cleaning the Jeopardy dataset. What's in the dataset? Cleaning up the text data by removing links. Regular expressions are greedy. Standardizing the dollar amounts after value change in 2001.*

*Introducing and cleaning the Jeopardy dataset. What's in the dataset? Cleaning up the text data by removing links. [Regular expressions are greedy](#Regular-expressions-are-greedy.). [Standardizing the dollar amounts after value change in 2001.](#Fixing-the-dollar-amounts-after-the-change-in-2001.)*

{% notebook notebooks/jeopardy_1_intro_clean_data.ipynb cells[0:16] %}

![Artist's View of Lightning on Venus]({filename}/images/Artist_s_concept_of_lightning_on_Venus.jpg)

** Artist's Concept of Lightning on Venus **

*Image Credit: [J. Whatmore, ESA](http://www.esa.int/spaceinimages/Images/2007/11/Artist_s_concept_of_lightning_on_Venus2){:target="_blank"}*

{% notebook notebooks/jeopardy_1_intro_clean_data.ipynb cells[16:26] %}

For reasons that I don't quite understand, the [pelican plugin that renders the notebook on this blog](https://github.com/danielfrg/pelican-ipynb){:target="_blank"} interprets the html code. (I can see how this might actually be a feature and not a bug.) Anyway... this means I can't show the actual html tags in my dataframe as they appear in the notebook. However, if you look at the [notebook on github](linkehere) you will see it shown correctly. Until I figure this out, I'll include a hacked column that shows the html syntax as it appears in the notebook in the column labeled `question_htmlview`.

{% notebook notebooks/jeopardy_1_intro_clean_data.ipynb cells[26:] %}

That's it for cleaning the data. You can find this [jupyter notebook on github](https://github.com/aurban8/aurban8.github.io/blob/dev/content/notebooks/jeopardy_1_intro_clean_data.ipynb){:target="_blank"}. [Next time]({filename}./jeopardy_2_states_values.md), I'll take a look at the relationship between the dollar value of questions about U.S. states and the frequency of their appearance on Jeopardy.