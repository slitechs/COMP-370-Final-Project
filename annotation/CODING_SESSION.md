# Coding session for three independent coders

**Dataset:** 742 unique Bluesky posts from the supplied October 16–17 collection. **Task:** give each assigned post one topic about what its text mainly discusses. The whole dataset is assigned across the three coders; the 150 shared posts let us measure agreement. Each coder receives only their own workbook and the same six-topic guide.

## Orientation together, before final coding

1. Explain the first research question: the eventual result is the topic percentage among eligible posts mentioning *You Can See Everything*. Movie names and positive/negative sentiment are separate from the topic code.
2. Read `COMP370_movie_taxonomy_guide.md` together. Practice only on the guide’s 200-post pilot examples. Work through the difference between a general reaction and a specific story or craft observation, and between a screening and a box-office result.
3. Ask the coders to use **only the text in the worksheet**. Do not open URLs, inspect images, or look at anyone else’s codes. Agree that the guide is version 1.0 for this round; note the orientation date. If the group changes a definition, issue version 1.1 to everyone before anyone resumes.

## Each coder works independently

Open your assigned `coder_N.xlsx`. The first tab gives instructions; the **Final coding** tab contains your posts. Read the full `post_text`, select exactly one of `REACT`, `CONTENT`, `CRAFT`, `VIEWING`, `CIRC`, `HUMOR` from the dropdown in `topic_code`. Use `uncertain_or_reason` if two categories seem plausible or the text may be off-topic, non-English, or about an older adaptation. Keep the `post_id` and `post_text` untouched. Save and return your own file. Do not exchange answers until all three files have been returned.

A passing mention of a film does not necessarily make a post eligible. If the text cannot be understood or might refer to the older *Sense and Sensibility*, write **ELIGIBILITY REVIEW** and a short reason in the notes. The coordinator will decide inclusion before analysis. If a plausible topic can still be assigned, record it; do not guess about unseen linked material. The source collection already flags some questionable posts for separate eligibility review.

## Coordinator after all three submit

Check that there are 348, 347, and 347 complete coding rows and that 150 post IDs have three codes. Preserve each person's original file. Run the merge and disagreement review described in `TEAM_WORKFLOW.md`; discuss 2–1 disagreements and document decisions for 1–1–1 splits. Apply recorded eligibility decisions. Compute percentages and TF-IDF only from the reconciled, eligible human-labeled data. State in the report that an AI assistant performed the 200-post exploratory open coding and drafted the guide; the three named group members independently annotated the final assigned posts.
