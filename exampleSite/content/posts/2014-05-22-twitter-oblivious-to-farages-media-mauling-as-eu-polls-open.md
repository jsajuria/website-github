---
title: Twitter oblivious to Farage’s media mauling as EU polls open
author: Javier Sajuria
type: post
date: 2014-05-22T09:57:12+00:00
url: /twitter-oblivious-to-farages-media-mauling-as-eu-polls-open/
dsq_thread_id:
  - "2713869908"
categories:
  - Uncategorized

---
<address>
  ** UPDATE: Extended methods section at the bottom of the post
</address>

<address>
  This article was originally published on <a href="http://theconversation.com">The Conversation</a>. Read the <a href="http://theconversation.com/twitter-oblivious-to-farages-media-mauling-as-eu-polls-open-27042">original article</a>.
</address>

By [Orlanda Ward][1]_, University College London_ and [Javier Sajuria][2]_, University College London_

Nigel Farage, leader of the UK Independence Party, appears to have stolen the show in the run up to the European elections. But while he has been pilloried in the papers, discussion about him on Twitter appears to have been somewhat more favourable.

Since campaigns for the European elections have been largely fronted by party leaders, we’ve investigated the level of mainstream media coverage given to David Cameron, Nick Clegg, Ed Miliband and Nigel Farage over the past six days. We’ve also looked at how much discussion has been going on about the leaders on Twitter over the same period.

We looked at all geo-tagged UK tweets and all national tabloid and broadsheet newspaper coverage of the Conservative, Lib Dem, Labour and UKIP leaders over the period. We analysed the amount of coverage and discussion each party leader received online and offline each day, and the proportion for each that was positive, negative or neutral.<figure class="align-centre zoomable">

[![][3]][4]<figcaption><span class="caption">Not a fan of the coalition.</span>&nbsp;</p> </figcaption></figure> 

While there has been plenty of mainstream newspaper coverage of major party leaders in the run-up to EU elections, particularly focusing on Farage, this has not been reflected in online discussions. For a start, political discussion only featured in about 2% of the almost 3m tweets we monitored.

Overall, both online and offline, Cameron and Farage have been the most prominent, trailed by Miliband and Clegg on both platforms.

But Farage in particular has been the subject of very different coverage in the online world and the more traditional press. While the UKIP leader’s media coverage spiked immediately following his now [infamous LBC interview][5], his mentions on Twitter suggest that the online reaction was more of a slow burn, though the tone of the discussion did become slightly more negative. Perhaps the LBC episode failed to inflame passions online becuase it simply seemed to confirm what existing views of Farage – both for and against.<figure class="align-centre zoomable">

[![][6]][7]<figcaption><span class="caption">Party leader mentions in newspapers and on Twitter</span>&nbsp;</p> </figcaption></figure> 

What’s more, the intensely negative coverage of Farage in the mainstream media has not been replicated online. If you only read the papers, you’d find that 31% of the comments made about Farage were negative, while between 20-21% of those made about Miliband, Clegg and Cameron could be classed as such.

But the proportion of tweets mentioning Farage that were negative was near identical to Miliband and Clegg at between 22% and 23%. Cameron got an easier ride with just 13% of tweets about him coding as negative.<figure class="align-centre zoomable">

[![][8]][9]<figcaption><span class="caption">Tone of mentions of Nigel Farage</span>&nbsp;</p> </figcaption></figure> 

No less than four simultaneous campaigns have been bubbling away in the UK as we carried out this analysis. While the European and local elections have fired the starting gun for the general election, the Scottish independence debate is also in full swing, not to mention the addition of a possible EU referendum.

This has meant that discussion and coverage this week has been fragmented. Miliband has spent the week laying out his policy for the general election amid claims that he’s been [missing in action][10] when it comes to European campaigning.

Cameron of course spent two days on a pro-union visit to Scotland, and much of rest of his exposure concentrated on the Chilcot Inquiry and coalition tensions. Clegg, meanwhile, has gained attention for all the wrong reasons: [drunken cactus shame][11]; [losing his rag with Michael Gove][12] and [Andrew Marr][13]; Commons whispers of a Lib Dem deposition and some polls suggesting the party may well [fall behind the Greens][14] in Europe.

In contrast, although reporting on Farage was dominated by the fallout from his LBC interview and questions about whether he is or isn’t a racist, it did stay focused on the strength of his party’s electoral prospects and his stance on immigration. What else is there to talk about?

Farage has become the focal point not just for the media, but for the major party leaders this week – that is, when they weren’t focusing on other elections. This short campaign has seen little coherent debate between parties and while their antics of course top the printed press agenda, our data suggests that they are not engaging debate among the wider public.

It also suggests that media lambasting of Farage doesn’t look set to change voters’ minds – at least not those on Twitter.

## Methods note

As a response of some of the questions asked about the methods we used to collect and analyse the data, we offer here some basic explanation.

For the Twitter data, we used the <a href="http://cran.r-project.org/web/packages/streamR/index.html" target="_blank">streamR</a> package to collect the data from the Twitter streaming API. We focused only on geotagged tweets in the UK, which accounted for an average of 500,000 tweets a day. Some <a href="http://www.public.asu.edu/~fmorstat/paperpdfs/icwsm2013.pdf" target="_blank">research</a> shows that the streaming API allows us to get most (if not all) of the geotagged tweets in a given period, but we also n=know that no more than 2% of the tweets contain geographical metadata. This is obviously a bias, and we try to be as explicit as possible about the limitations of our data and methods.

The newspaper data was obtained using <a href="http://www.nexis.com" target="_blank">Nexis</a> and getting all articles that contained the name of one of the UK party leaders. As explained above, the number of mentions for the leader of the Green Party were too low (or nonexistent) and we had to remove her from our sample. After we obtained the articles, we trimmed the sentences where the party leader name was mentioned, and that was our unit of analysis.

In terms of analysis, we made some changes to the methods used by <a href="http://www.pablobarbera.com" target="_blank">Pablo Barberá</a> on his <a href="https://github.com/pablobarbera/workshop" target="_blank">workshop at SMaPP NYU</a>. Most of the R functions created for this purpose were compiled in a (very beta) R package called <a href="https://github.com/jsajuria/euElection" target="_blank">euElection</a>. This package allowed us to obtain a very rough estimate of the tone of the tweets and the newspapers sentences, which is what we used in the article. In simple terms, each word from our units of analysis was compared to a vocabulary of positive and negative words (the &#8220;lexicon). All other words were considered as neutral. Then, we obtain the proportion of tweets/sentences that has a majority of positive, negative or neutral tone. We only selected tweets and sentences that mentioned, at least, the name of the party leaders.

We are happy to receive any feedback or comments you may have on this and other methods issues.

<img loading="lazy" src="https://counter.theconversation.edu.au/content/27042/count.gif" alt="The Conversation" width="1" height="1" />

 [1]: http://theconversation.com/profiles/orlanda-ward-126605
 [2]: http://theconversation.com/profiles/javier-sajuria-126606
 [3]: https://62e528761d0685343e1c-f3d1b99a743ffa4142d9d7f1978d9686.ssl.cf2.rackcdn.com/files/49181/width668/zrzjx7cd-1400699506.jpg
 [4]: https://62e528761d0685343e1c-f3d1b99a743ffa4142d9d7f1978d9686.ssl.cf2.rackcdn.com/files/49181/area14mp/zrzjx7cd-1400699506.jpg
 [5]: http://www.newstatesman.com/staggers/2014/05/what-racism-nigel-farage-s-disastrous-interview-lbc
 [6]: https://62e528761d0685343e1c-f3d1b99a743ffa4142d9d7f1978d9686.ssl.cf2.rackcdn.com/files/49177/width668/ndyhfb45-1400698233.jpg
 [7]: https://62e528761d0685343e1c-f3d1b99a743ffa4142d9d7f1978d9686.ssl.cf2.rackcdn.com/files/49177/area14mp/ndyhfb45-1400698233.jpg
 [8]: https://62e528761d0685343e1c-f3d1b99a743ffa4142d9d7f1978d9686.ssl.cf2.rackcdn.com/files/49178/width668/d598vfrs-1400698240.jpg
 [9]: https://62e528761d0685343e1c-f3d1b99a743ffa4142d9d7f1978d9686.ssl.cf2.rackcdn.com/files/49178/area14mp/d598vfrs-1400698240.jpg
 [10]: http://www.theguardian.com/politics/2014/may/18/ed-miliband-criticism-labour-campaign-tactics
 [11]: http://www.independent.co.uk/news/people/nick-clegg-i-set-fire-to-a-cacti-collection-and-im-not-proud-of-it-9375806.html
 [12]: http://news.sky.com/story/1262116/nick-clegg-and-michael-gove-kiss-and-make-up
 [13]: http://www.telegraph.co.uk/news/politics/liberaldemocrats/10839133/Dont-sneer-Andrew-Clegg-loses-his-cool-with-Marr-over-coalition-question.html
 [14]: http://www.theguardian.com/politics/2014/may/12/support-labour-drops-tories-lead-guardian-icm-poll?CMP=twt_gu