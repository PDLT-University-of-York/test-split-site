# Test

!!! Summary

    Test is a quiz and exam tool with a wide range of uses from informal knowledge checks to summative exams.

    This guide covers how to use and set up a Test, and is primarily aimed at **teaching staff**.

!!! principle "Relevant [VLE site design principles](../ultra/site-design-principles.md)"

    - 3.4 Essential: Site and materials content is accessible.
    - 4.1 Essential: The assessment section contains all information about module assessments.
    - 4.2 Essential: Assessment instructions are clearly labelled and explain the task and requirements.

![Example Test with multiple choice and fill in the blank question types](images/test-example.png)

## When to use Test

Test has a lot of flexible features that makes it useful in many situations:

- a wide range of question types, most with automatic marking and feedback
- create questions within the test, import questions from file or reuse questions from existing banks or tests
- possibility for (automatic) partial, negative and extra credit
- randomise the order of questions and/or answer options
- question banks and pools: present a random selection of questions for each student
- calculated formula/numeric questions: use randomised values to automatically generate a large bank of different questions

This makes Test a useful tool in many situations, from short practice quizzes up to summative exams.

=== "Knowledge check"

    **A short, one-off self-assessment.**

    Some examples:

    - **self assessment/knowledge check**: a few questions to check understanding of weekly content. You can do this using Test or by adding questions directly within a [Document](../ultra/documents.md).
    - **track completion** of required content (eg. safety materials): honesty-based True/false question to self-declare completion.
    - **demonstrate preparation** for workshops or practicals: a few questions on preparatory content or True/False to self-declare completion.

    Test completion can also be used as a criteria for setting [Release Conditions](../ultra/content-visibility.md) for other items. For example, access to laboratory session materials could be restricted until students have successfully completed a preparatory quiz.

    Common features:

    - Tend to be short: **up to 5 questions**
    - Question display: usually all possible questions
    - Question types: all **questions should be automatically marked** so no input is needed from teaching staff
    - Set up effort: low, usually quick and simple to set up

=== "Practice quiz"

    **An informal quiz that can be taken multiple times.**

    Some examples:

    - practice quizzes: providing an active opportunity to practice 'right answer' content (eg. match terminology, complete calculations)
    - revision quizzes covering part of or all module content

    Common features:

    - Question display: commonly a random subset drawn from a larger question bank so that students can retake the quiz, but can also present the same questions each time.
    - Question types: all **questions should be automatically marked** so no input is needed from teaching staff
    - Set up effort: low to medium, depending on how questions are created and whether random subsets are used.

=== "Formal exam"

    **Formal summative or formative exams**

    Some examples:

    - Open book exam: students complete the exam during a given time window at a place of their choosing. Can't be invigilated.
    - Closed book exam: students complete the exam at a set time in an on-campus computer lab. Can be invigilated.
    - It is good practice to also run a formative/mock exam to familiarise students with the online exam process.
    
    Common features:
    
    - Question display: usually random subset(s) drawn from larger question banks to support robust assessment, but can also present the same questions to each student in closed book exams.
    - Question types: preferably automatically marked (to allow **non-anonymous** workflows, which are significantly easier to administer), but can include manually marked questions.
    - Set up effort: medium to high, as requires very careful set up and checking.

    !!! Warning

        If you are setting up a summative Test, also review this more detailed guide:   
        [Staff Help: Considerations Around & Setting up a **Summative** VLE Test](https://docs.google.com/document/d/1sn85oHTEuxNuw3_6R_TqdGlgrlWAgyCEtv7FXyd0his/edit?usp=sharing)
        
        You **must** [contact the Digital Education Team](mailto:vle-support@york.ac.uk) well in advance if you want to run a summative and/or synchronous exam (in person or online) using Ultra Test.

Find out more about how Test has been applied across the University:

??? case-study "Case study: Ultra Test for formative and summative assessment [Computer Science]"

    Tommy Yuan shares his experiences of using the Ultra test tool for formative and summative assessment. Topics include how it can save time for lecturers and administrators, and reduce the likelihood of collusion and academic misconduct.

    Watch their presentation:<iframe src="https://york.cloud.panopto.eu/Panopto/Pages/Embed.aspx?id=0ed26b92-2446-45e4-9815-b141010d308f&autoplay=false&offerviewer=true&showtitle=false&showbrand=false&captions=false&interactivity=all" height="405" width="720" style="border: 1px solid #464646;" allowfullscreen allow="autoplay" aria-label="Panopto Embedded Video Player" aria-description="Tommy Yuan: VLE Test for assessment" ></iframe>

    [VLE Test for assessment (Panopto viewer)](https://york.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=0ed26b92-2446-45e4-9815-b141010d308f) (6 mins 59 secs, UoY log-in required)

    See the [full case study for more details and the transcript](../training/case-studies/cs-yuan.md).
    You can also browse our [full set of case studies](../training/case-studies/index.md).

??? case-study "Case study: Ultra Test for practice quizzes [Language & Linguistic Science]"

    Ellie Rye provides a walkthrough of the 'Structure of English' Ultra site, describing how they applied the Ultra template to present teaching content, and reflects on the use of Discussions and Tests for formative practice quizzes.

    Watch their presentation:<iframe src="https://york.cloud.panopto.eu/Panopto/Pages/Embed.aspx?id=affd8a23-7d50-4d21-87d0-b15600b04234&autoplay=false&offerviewer=true&showtitle=false&showbrand=false&captions=false&interactivity=all" height="405" width="720" style="border: 1px solid #464646;" allowfullscreen allow="autoplay" aria-label="Panopto Embedded Video Player" aria-description="Ellie Rye, LLS, Structure of English" ></iframe>

    [Structure of English (Panopto viewer)](https://york.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=affd8a23-7d50-4d21-87d0-b15600b04234) (8 mins 21 secs, UoY log-in required)

    See the [full case study for more details and the transcript](../training/case-studies/lls-rye.md).
    You can also browse our [full set of case studies](../training/case-studies/index.md).

### Question types

| Question type | Description | Grading type |
| ----------- | ----------- | ----------- |
| [Multiple Choice](https://help.blackboard.com/Learn/Instructor/Ultra/Tests_Pools_Surveys/Question_Types/Multiple_Choice_Questions)  | Pick the correct answer(s) from options given. Options can be fixed or randomised, can give partial or negative credit. | auto graded |
| [Fill in the Blank](https://help.blackboard.com/Learn/Instructor/Ultra/Tests_Pools_Surveys/Question_Types/Fill_in_the_Blank_Questions) | Input the missing word(s) in the given text. Set if answers should be exact, match part of a specified answer or match a pattern. | auto graded |
| [Matching](https://help.blackboard.com/Learn/Instructor/Ultra/Tests_Pools_Surveys/Question_Types/Matching_Questions)| Match corresponding items from two groups. Options can be fixed or randomised, can give partial or negative credit. | auto graded |
| [True/False](https://help.blackboard.com/Learn/Instructor/Ultra/Tests_Pools_Surveys/Question_Types/Matching_Questions)| Choose True or False in response to a given statement. | auto graded |
| [Calculated Formula](https://help.blackboard.com/Learn/Instructor/Ultra/Tests_Pools_Surveys/Question_Types/Calculated_Formula_Questions)  | Calculate the answer to a given formula (eg. 3x + 4y = ?). Values (x/y) are randomly generated so each student has a different question.| auto graded |
| [Calculated Numeric](https://help.blackboard.com/Learn/Instructor/Ultra/Tests_Pools_Surveys/Question_Types/Calculated_Numeric_Questions)  | Similar to Fill in the Blank questions, but for numeric answers. Can set the answer as an extact number or within a range.| auto graded |
| [Hotspot](https://help.blackboard.com/Learn/Instructor/Ultra/Tests_Pools_Surveys/Question_Types/Hotspot_Questions)  | Drop pin(s) on an image. Consider accessibility carefully. | auto graded |
| [Essay](https://help.blackboard.com/Learn/Instructor/Ultra/Tests_Pools_Surveys/Question_Types/Hotspot_Questions)  | Type a response (of any length) in the answer box. Can provide a model answer for feedback. | manually graded |

## Accessible Test Content

As with all teaching content, accessibility is very important when building test questions and answer options. [All the usual considerations around accessibility apply to tests](../accessibility/accessible-ultra-content.md), but it is **particularly** important that you take into consideration accessiblility when using tables, images or mathematical content in test questions.

- Guidance on creating accessible images, table and maths can be found on [our "Ultra Accessibility" VLE page](https://vle.york.ac.uk/ultra/courses/_106795_1/outline). (Don't have access? [Contact us](mailto:vle-support@york.ac.uk)).
- [Examples of quality alternative text on graphs, diagrams and other complex images can be found here](https://www.routledge.com/our-customers/authors/publishing-guidelines/accessible-content/general-samples).

## Create a Test

=== "Knowledge check"

    **Location**

    Knowledge checks are best located alongside the relevant materials, usually within a weekly content section.

    ![decorative](images/test-in-weekly-content.png)

=== "Practice quiz"

    **Location**

    Locate the quiz where it will make most sense to students. This could be:

    - practicing specific content: alongside weekly materials.
    - general revision: in the Assessment section.

    You can use a [Course Link](../ultra/course-links.md) to show a quiz in more than one location.

=== "Formal exam"

    **Location**

    Consider the location of the exam and also information about how to take the exam.

    - Exam itself: usually created in a separate exam site to aid set up and for exam security.
    - Details of the exam: include in the Assessment section of your module site.

1. Hover where you want the Test to appear, click the plus icon, then **Create**, then select **Test**.
2. Give the Test a descriptive **name** at the top left.
3. Click the plus icon to add **questions** (see Test questions section below).
4. Set the **Due date** and adjust other settings as needed (see Test settings section below).
5. Once confident that the Test is ready, set the test as **Visible to students** or specify  **Release conditions** in the top right.

![decorative](images/test-create.png)

!!! Tip

    You can build and trial the Test in your personal Ultra sandpit site, and when it is ready use the [Copy Content tool](../ultra/copy-content.md) to add it to your module/exam site in the relevant location.

## Add Test questions

There are various ways to add questions to a Test. Which method is most appropriate depends on the amount of questions to add, whether to display all questions or a random subset, and whether questions have already been added elsewhere in the site.

=== "Knowledge check"

    **Method to add questions**

    As knowledge checks have a small number of questions that are all displayed to students, it's likely easiest to **manually add questions** to your Test.

=== "Practice quiz"

    **Method to add questions**

    If all questions are displayed:

    - small number of new questions: manually add questions
    - large number of new questions: upload questions in a .tsv file
    - use questions from another Test or Question Bank: re-use questions

    If subset(s) of possible questions are displayed:

    - add questions to a Question Bank or another Test and then set up a Question Pool(s) in this Test
    
=== "Formal exam"

    **Method to add questions**

    If all questions are displayed:

    - small number of new questions: manually add questions
    - large number of new questions: upload questions in a .tsv file
    - use questions from another Test or Question Bank: re-use questions

    If subset(s) of possible questions are displayed:

    - add questions to a Question Bank or another Test and then set up a Question Pool(s) in this Test
    

### Manually add questions

You may find it helpful to draft your questions in another document first.

1. Click the **plus + icon**.
2. Select the relevant question type.
</br> ![decorative](images/test-manually-add-questions.png)
3. Enter the question and answers as needed for that question type (see the linked guides in the Question Types section for more information)
4. Optional question settings (availability depends on question type):
    - set partial or negative credit for different answers
    - set the question as extra credit
    - add automated feedback
    - change the points awarded (default = 1 point)
    </br>![Multiple choice question manually built in the editor, highlighting optional features listed.](images/test-question-options.png)
5. Click **Save**.
6. Repeat for all questions. 

### Upload questions from file

You can draft questions in a spreadsheet and **upload them in .tsv format** to your Test.

Prepare the file

1. Make a copy of the [Ultra tsv template for Tests Google Sheet](https://docs.google.com/spreadsheets/d/17G_QC4bgFbiLmgIFyIl-jOfLbLLFr8yAxCMF3flwGoM/copy)
2. Enter your questions by editing the *BB test* tab (contains examples of the formatting required for each question type).
</br>![Multiple choice question in the .tsv format](images/test-upload-tsv-example.png)
3. Download the questions in .tsv format: File > Download > Tab-separated values (.tsv)

Upload the file

1. Return to the Test and click the **plus + icon**.
2. Select **Upload questions from file**.
</br>![decorative](images/test-upload-questions.png)
3. Select your .tsv file.
4. Once the upload is processed, review the status message for any errors.

For more details and examples of the required file format, see [Blackboard's guide to uploading questions](https://help.blackboard.com/Learn/Instructor/Ultra/Tests_Pools_Surveys/Reuse_Questions/Upload_Questions).

Optional question settings: these can't be specified in the .tsv file, so first upload your file and then manually update each question.

### Reuse questions

Copy questions that already appear in another Test or Question Bank in the site. This creates copies of questions, so any edits made to re-used questions are not updated in the original question. 

!!! Tip

    Reusing questions will display all of the selected questions in the Test. If you want to display only a subset (eg. 2 of 10 possible questions), use a Question Pool instead.

1. Click the **plus + icon**.
2. Select **Reuse questions**.
</br>![decorative](images/test-reuse-questions.png)
3. Select the questions to copy, using the filter options if needed: search by keyword, browse by source (Tests and Question Banks), browse by question type.
4. Click **Copy questions**.
5. Once the copy is processed, review the status message for any errors.

### Question pools
 
Add a random subset of questions that already appear in another Test or Question Bank in the site. This is useful for creating robust assessments and also for practice quizzes that students may take multiple times.

Question pools do not copy questions; any edits made to questions in a pool will appear everywhere that question is used. Deleting a question from a Question pool does not delete the question in other locations.

!!! Warning

    For fairness and to create a valid assessment, all questions in the pool must be of equivalent difficulty. To include questions at different levels, use a pool for each level.

1. Click the **plus + icon**.
2. Select **Add question pool**.
</br>![decorative](images/test-add-question-pool.png)
3. Select the questions to add, using the filter options if needed: search by keyword, browse by source (Tests and Question Banks), browse by question type.
4. Click **Add questions**.
5. Enter the number of questions to display and optionally update the points awarded per question. Click **Save**.
</br>![decorative](images/test-question-pool-options.png)
6. In edit mode a summary of the pool is shown where you can view the questions and edit settings. Students will see the questions pulled from the pool.
</br>![Pool summary showing that 2 of 7 questions are displayed to students, with option to view all questions](images/test-question-pool-finished.png)

For more details, see the [BlackBoard Help guide to Question pools](https://help.blackboard.com/Learn/Instructor/Ultra/Tests_Pools_Surveys/ULTRA_Reuse_Questions/Question_Pools).

<iframe width="560" height="315" src="https://www.youtube.com/embed/cuWBxlV2FVM?si=nJxIyIk57ixUln30" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
[Use Question Pools in Assessments in the Ultra Course View [YouTube]](https://youtu.be/cuWBxlV2FVM?si=ulkRHUN9G8-YGIWq)

## Test Settings

There are various settings possible for Tests, including;

- due date and attempt management
- randomising questions and answers
- presenting marks and feedback to students

!!! Tip

    Randomising questions will present all questions in the Test in a random order. If you want to randomly select a subset of questions, use a Question Pool.

Edit settings in the **Assessment settings** panel:

- Click the **cog icon** to open the full Test settings
- The settings summary gives quick access to some settings: Due date, Mark category, Marking, Attempts allowed, Originality Report

![decorative](images/test-settings.png)

=== "Knowledge check"

    **Suggested settings**

    - Details & Information
        - tick *No due date*
        - leave other options unticked
    - Presentation Options
        - if using LaTeX, tick *Display one question at a time* for more consistent rendering
        - leave other options unticked
    - Formative Tools
        - tick *Formative assessment*
        - leave *Display formative label to students* ticked
    - Marking & Submissions
        - Mark category: leave as *Test* or change to *Quiz* (this will change the icon displayed in the Course Content area)
        - Attempts allowed: set to Unlimited
        - Assessment mark: leave *Post assessment marks automatically* ticked
        - leave other options unticked
    - Assessment results: no action needed
    - Assessment security: no action needed
    - Additional Tools: no action needed
    - Description: add an optional short description to display under the item's name in the Course Content area.

=== "Practice quiz"

    **Suggested settings**

    - Details & Information
        - tick *No due date*
        - leave other options unticked
    - Presentation Options
        - if no randomisation needed: leave all unticked
        - if randomisation is needed: tick *Randomise questions*, *Randomise answers* or *Randomise pages* as desired
        - if using LaTeX, tick *Display one question at a time* for more consistent rendering
    - Formative Tools
        - tick *Formative assessment*
        - leave *Display formative label to students* ticked
    - Marking & Submissions
        - Mark category: leave as *Test* or change to *Quiz* (this will change the icon displayed in the Course Content area)
        - Attempts allowed: set to Unlimited
        - Assessment mark: leave *Post assessment marks automatically* ticked
        - leave other options unticked
    - Assessment results: no action needed
    - Assessment security: no action needed
    - Additional Tools: no action needed
    - Description: add an optional short description to display under the item's name in the Course Content area.
    
=== "Formal exam"

    It's essential that settings are correct for formal exams. This will depend on the structure of your Test and other requirements.
    
    [Contact us](mailto:vle-support@york.ac.uk) to advise on appropriate settings for your specific exam.


## Print or save a Test

You can print or save your Test as a PDF, either with or without answers. This could be useful to:

- deliver and mark the Test as a paper-based assessment
- save the Test for your records
- provide a copy of the Test for external examiners, reviewers etc.

!!! Note

    It is not currently possible to print Tests containing a Question Pool.

1. Click **Print** at the top of the Test.
2. Select **Questions only** or **Questions with answers**
![decorative](images/test-print.png)
3. Save as PDF or send to the printer.
