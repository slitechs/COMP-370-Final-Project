# COMP 370 movie-post annotation: quality and agreement

## Scope and files

The supplied October 16–17, 2026 UTC collection contains **full distinct Bluesky posts**. The three returned human-coder sheets each contain the same post IDs all shared equally.

After reviewing 80 posts flagged for possible eligibility problems, **14 were removed and 728 retained**. The current files are `eligibility_reviewed_annotations.xlsx` (included posts, removed posts). The full earlier `merged_current_annotations.csv` records human votes, decision type, and source (majority, unanimous or arbitrary choice made by Ella).

One post receives exactly one of six topics: **REACT** (overall appraisal/feeling), **CONTENT** (story, people, meaning), **CRAFT** (filmmaking/performance), **VIEWING** (plans/access/theater experience), **CIRC** (marketing, coverage, commercial discussion), or **HUMOR** (joke/parody as the main point). Film identity and sentiment are separate from the topic. Eligibility is separate from both.

## Agreement before reconciliation
For posts where all three coders agreed, we used their unanimous topic as the final code. When two coders agreed and the third chose a different topic, we used the majority code. When all three chose different topics, I read the post, made an adjudication choice using the taxonomy guide, and recorded my reason in the merged annotation file.
The three human coders agreed unanimously on 54.9% of the posts. On 39.5% of posts, two coders agreed and one disagreed; on 5.6% of posts, all three chose different topics.  The disagreements suggest both **tricky cases** and **overlap between topic definitions**, especially REACT versus CONTENT or CRAFT, and REACT versus VIEWING. For a revised guide, we should add a rule that a developed observation about the story or meaning takes CONTENT, while one about acting or filmmaking takes CRAFT, even if the post also says the film was good. REACT should cover general praise, criticism, or recommendations without a more specific point. We should also add examples showing that a recommendation such as “go see it” is REACT, while a ticket, viewing plan, or account of a screening is VIEWING.

### What the disagreement shows

- **REACT versus CONTENT/CRAFT.** Sophia–Jerome disagreed 29 times on REACT/CONTENT and 25 on REACT/CRAFT; Sophia used CRAFT 39 times across her 347 assigned posts, versus Jerome's 8. Coders differed in whether a specific observation about story, filmmaking, or performance outweighed a brief general verdict.
- **REACT versus VIEWING.** Alexander–Jerome disagreed 18 times on this pair. “Go see it” can function as a recommendation, while a ticket, showtime, or actual screening experience belongs to VIEWING.
- **CIRC versus a substantive point.** A review link or trailer mention alone tends to be CIRC; a post that itself interprets a character, theme, or technique belongs to CONTENT or CRAFT. Counting linked material that coders did not read would change the task.
- **HUMOR versus another topic.** Wordplay and invented scenarios are HUMOR when the joke is the post's main point; “lol” or a witty recommendation does not override a substantive topic.


## Eligibility decisions and removed posts

Among the **80 previously flagged rows** fourteen were excluded; the other 66 were kept. 

| Post ID | Reason for exclusion |
| --- | --- |
| `45befb6454f9c69b` | Portuguese headline and surrounding text. |
| `f56b4027da9efbf1` | Substantially Portuguese post. |
| `efa5c0dca463f405` | Substantially Portuguese post. |
| `24b3f90e91b26e47` | Explicitly about the Ang Lee/Emma Thompson 1995 adaptation. |
| `a2352c356645cc04` | Selected film is a parenthetical aside; another film is evaluated. |
| `3617a2fb94d4d492` | Discusses an unrelated post under a search trend rather than the film. |
| `8603565e58a5b98c` | Uses Whalefall as a hashtag while asking about ocean movies generally. |
| `8931e2bec4fa3400` | Meaning depends on an unseen image; text has no discernible film topic. |
| `1ef53df975f6d358` | Reviews *The Devils*; selected title only identifies other audience members. |
| `6a04a739bb4168d5` | Title correction with no discernible film or viewing point. |
| `4accfc20e291c785` | Selected film is an incidental release mention among unrelated films. |
| `6d90b223b176da20` | Bare film title and “apparently?” give insufficient context. |
| `bdd43e72ee48a004` | Film hashtags plus an opaque link, with no readable topic in the post. |
| `a2519ba51ac65b3f` | Generic follow-me request and opaque link; hashtag does not establish a film-related point. |

The retained dataset has **527 posts mentioning You Can See Everything, 165 mentioning Whalefall, and 44 mentioning Sense and Sensibility**. These mention counts overlap when a post names more than one film; they should not be added to obtain 728. The original collection had 535, 170, and 45 mentions respectively. The focal-film topic percentages should use **527** as the denominator under these decisions. The six topic counts across *all* 728 retained posts are REACT 262, VIEWING 178, CIRC 111, CONTENT 83, CRAFT 48, and HUMOR 46; these are not the focal-film percentages.

## Clarification to the taxonomy

We will keep the six topics and add these explicit rules to our taxonomy guide, with one real post example for each:

1. **Specificity:** If the text develops a claim about plot, depicted people, meaning, acting, editing, or visual form, use CONTENT or CRAFT even when it begins or ends with “great film.” A bare score or emotional reaction is REACT.
2. **Viewing versus recommendation:** A plan, ticket, showtime, availability, film log, or account of the audience is VIEWING. “You should see it” plus praise, without a concrete viewing event or access issue, is REACT.
3. **Coverage versus interpretation:** A bare review link, review announcement, aggregate score, box-office result, or trailer promotion is CIRC. Classify the post's own substantive claim instead when it develops one; never follow the link to decide.
4. **Humor:** Reserve HUMOR for a joke or parody that is the main message. Do not infer a joke from informal language alone.
5. **Eligibility before topic:** A name-only post can be a viewing log or a release announcement if its own text supplies that context. Exclude an opaque link/hashtag, non-English text, an older adaptation, or a passing mention where the post's topic cannot be assigned from its text. Record exclusions independently of topic labels.
