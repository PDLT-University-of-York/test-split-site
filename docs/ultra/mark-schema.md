---
tags:
    - Key guide - admin
    - Assessment
    - Ultra
---

# Mark Schemas

!!! Summary

    Marking schemas map a raw numerical mark to display in another format, eg. A/B/C or Complete/Incomplete.

    This guide is aimed at **Administrators** and **Teaching staff**.

This guide is under construction. For general information, see [Blackboard Help's guide to Grading Schemas](https://help.blackboard.com/Learn/Instructor/Ultra/Grade/Customize_Grading_Interface/Grading_Schemas).

Situations where a mark schema may be useful include:

- formatives - help students focus on the work and feedback rather than a number
    A/B/C
    Complete/Incomplete
- stepped/banded marking - map mark to the relevant stepped grade (eg. 62, 65, 68)

## How a Mark Schema works

Mark Schemas are set up using a table with two columns:

- **Mark Name**: the converted label/letter/number etc. that is displayed (eg. *Excellent*)
- **Mark Range %**: the corresponding raw mark range that maps to the mark name (eg. *75% - 100%*)
<div markdown class="grid">
<div markdown>
Each mark band has a row. For example, this mark schema has four bands:

- Excellent: 75% - 100%
- Good: 50% - <75%
- Satisfactory: 25% - <50%
- Poor: 0% - <25%
</div>
![decorative](images/mark-schema-example.png)
</div>

If this mark schema is applied to an assessment, a raw mark of 55% will be displayed as **Good** within the marking interface and the Gradebook.

## Add and manage Mark Schemas

1. Open the **Gradebook** tab in the top navigation bar in the site. Any tab within the Gradebook is fine.
2. Click the **Settings (cog) icon** in the top right of the Gradebook, then click **Manage mark schemas** on the overlaid Settings menu.
</br>![decorative](images/mark-schema-access-mark-schemas.png)
3. The Mark Schemas page lists all the site's mark schemas.
    - To add a new mark schema: click the **Plus icon**, then enter a name and click **Add**
    - To edit an existing schema: click the schema name
    </br>![decorative](images/mark-schema-add-edit-schema.png)
4. Within a Mark Schema you can edit the name, or click the **three dots icon** adjacent to the name to copy or delete the schema.
</br>![decorative](images/mark-schema-edit-name-copy-delete.png)
5. To add rows: hover between the relevant rows and click the **plus icon** that appears. Enter a Mark Name and the relevant Mark Range.
</br>![decorative](images/mark-schema-add-row.png)
6. To edit existing rows: click the **three dots** icon on the right of the row or click the mark name or values. Update as needed.
</br>![decorative](images/mark-schema-edit-row.png)
7. When the mark schema is finished, click **Save**.

!!! Tip

    There can't be gaps between mark ranges, so when building a new mark schema it may be easiest to first add the correct number of rows and then edit the mark ranges afterwards.

## Associate a Mark Schema with an Assignment