# Draw-to-learn-science

## Introduction

A project to study whether drawing is a useful strategy for learning about abstract scientific concepts. In two notebooks, I analyze data collected from 500 individuals who participated in one of two experiments on this topic. Participants were randomly assigned to either study or copy an instructor-created drawing, complete a scaffolded drawing worksheet, or to draw on a blank sheet of paper while reading about an abstract concept or a physical system. We found evidence that drawing without guidance most effectively encourages retention but not transfer when the lesson is abstract. Drawing did not encourage retention or transfer when the lesson was on a physical system.

## Background

Researchers have studied whether drawing helps students learn the structure and function of physical systems. Although the results are mixed and not all find a benefit to drawing (Van Meter and Garner 2005), they generally find that the efficacy of drawing to learn depends on a few factors. These factors include the accuracy of the drawing, the prior knowledge of the learner, and the level of guidance provided during the drawing process (Fiorella & Zhang, 2018), where novices benefit from greater guidance (Van Meter, 2001). However, what if the accuracy of the learners’ drawings did not matter? We propose that when there is no correct way to represent the contents of a lesson in a drawing, it is less important that students draw exactly what an instructor would produce as these representations are arbitrary. This may mean that even without guidance, student-generated drawings may improve learning by more effectively capturing students’ thinking and prompting them to build visual representations that they find memorable.

## Research Questions

1. Is drawing an effective strategy when used to learn science?
2. Does the efficacy of drawing to learn depend on the contents of the lesson?
3. Is drawing a more useful tool when learning about abstract concepts compared to physical systems?

## Hypotheses

1. The efficacy of drawing to learn will depend on the contents of the lesson such that drawing will encourage meaningful learning only when the contents of the lesson cannot be represented as a physical system.
2. Meaningful learning will improve as students generate more of their own drawing (i.e., participants who draw will do better than those who complete a scaffolded worksheet, and those who complete a scaffolded worksheet will do better than those who copied the same worksheet, etc.)

## Files

`Experiment1.ipynb`

- The purpose of Experiment 1 was to test whether greater illustration generativity would benefit the retention and transfer of a passage about an abstract scientific phenomenon. We predicted that retention and transfer performance would improve as participants generated more of their own illustrations. If this were true, we would expect participants who studied a drawing provided to them to perform the worst on both measures of comprehension and participants who drew their own illustration to perform the best.

`Experiment2.ipynb`

- The purpose of Experiment 2 was to replicate the finding that students benefit from guidance when drawing to learning about a physical system. We predicted that retention and transfer performance would be the highest in the complete condition because this is the condition in which the most guidance was provided during the drawing process. Moreover, we predicted that retention and transfer would be higher in the drawing condition compared to the copying and studying conditions because the act of producing a drawing from scratch is thought to improve memory. We did not expect significant differences between the copying and studying conditions.

## Data

Data are excluded from the repository as they are proprietary to the research lab that sponsored this work.

## Results

### Data Checks and Preliminary Analysis

Prior to the main analysis, data were examined to ensure equal distribution of individual differences across groups, focusing on prior knowledge, study time, and visual imagery ability. A one-way ANOVA indicated a significant effect of visualization condition on study time (F(3,217) = 15.411, p < 0.0001). Post hoc Tukey HSD tests showed that the study condition (M = 11.481, SD = 2.23) spent significantly less time compared to the drawing (M = 17.083, SD = 5.646; p < 0.001), complete (M = 15.406, SD = 4.628; p < 0.001), and copy conditions (M = 15.265, SD= 4.812; p < 0.001). No other pairwise comparisons were significant.

### Planned Analyses

Two-way ANOVAs assessed the effects of visualization conditions on multiple-choice, open-response retention, and open-response transfer test scores, controlling for prior knowledge. Significant main effects were found for visualization strategy (F(7,213) = 3.95, p = 0.0004) and prior knowledge (F(3,217) = 4.79, p = 0.030) on the open response retention test, but their interaction was not significant. Tukey HSD tests revealed that the drawing condition significantly outperformed other conditions, with the largest difference between drawing (M = 8.55, SD = 3.55) and copying (M = 5.42, SD = 3.82; p = 0.0007). Drawing also outperformed the study (M = 6.68, SD = 3.63; p = 0.497) and complete conditions (M = 6.33, SD = 4.02; p = 0.029). No significant effects were observed for multiple-choice or open-response transfer tests.

### Exploratory Analysis

Exploratory analyses examined differences in cognitive load (total and subcomponents), passage comprehension prediction based on study time, and cognitive load. A one-way ANOVA showed no significant differences in total cognitive load across groups. However, significant differences were found in extraneous load (F(2,217) = 14.794, p < 0.0001), intrinsic load (F(3,217) = 2.736, p = 0.0445), and germane load (F(3,217) = 5.719, p = 0.0009). Tukey HSD tests indicated that the drawing condition rated the lesson significantly less complex (M = 5.49, SD = 4.03) than the copy (M = 7.825, SD = 6.345; p = 0.0007), complete (M= 10.643, SD = 6.462; p = 0.029), and study conditions (M = 4.474, SD = 3.747; p = 0.0497). For germane load, the study condition (M = 26.579, SD = 7.524) reported significantly more mental effort than the copy condition (M= 23.49, SD = 8.565; p = 0.0003).

Simple linear regressions revealed significant predictors of passage comprehension by study time for multiple-choice gain (F(1,219) = 4.322, p = 0.0389, R² = 0.0194), open response retention (F(1,219) = 22.193, p < 0.0001, R² = 0.092), and open response transfer test (F(1,219) = 9.659, p = 0.0021, R² = 0.0422). No significant regression was found for cognitive load predicting passage comprehension.

### Discussion

The findings suggest that drawing to learn theoretical science enhances recall of key points, with drawing participants scoring higher on open-response retention tests compared to other groups, but showing no advantage in multiple-choice or transfer tests. The largest performance difference was between the drawing and copy conditions, contrary to previous research suggesting guided visualization benefits. Time spent on the passage was a significant factor for retention performance, and self-reported germane load was significantly predicted by visualization condition. These insights underscore the potential benefits of drawing for retention and highlight the importance of considering cognitive load in educational strategies.

## Affiliations

All work was done in collaboration with the [Learning and Instruction in Multimedia Environments (LIME) lab](https://www.lime-lab-ucsd.com/) at the University of California, San Diego.

## References

1. Van Meter, P., & Garner, J. (2005). The promise and practice of learner-generated drawing: Literature review and synthesis. Educational Psychology Review, 17(4), 285-325.
2. Fiorella, L., & Zhang, Q. (2018). Drawing boundary conditions for learning by drawing. Educational Psychology Review, 30(3), 1115-1137.
