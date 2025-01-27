---
tags:
    - Key guide - teaching
    - Ultra
---

# Content visibility & release conditions

!!! Summary

    Manage visibility of content items for all users or based on certain conditions.

!!! principle "Relevant [VLE site design principles](../ultra/site-design-principles.md)"

    - 5.1 Recommended: Ensure that students can see and access module materials and content.

Items in the Course Content area can be set to **Visible to students** or **Hidden from students**. By default, all new items are automatically hidden from students.

You can check that items are shown or hidden correctly using the Student Preview tool.

!!! Tip 
    
    It is best practice to make all materials available at the start of the module.
    
    If this isn't possible, they should be released **at least a week in advance** to allow students to prepare appropriately.

## Show/hide a single item

1. Open the item's visibility menu from either:

    - *Course content area*: under the item title
    - *Within the item*: in the top right, near the cog settings icon

![Decorative](images/content-visibility-dropdown-locations.png)

2. Select the required visibility option:

    - **Visible to students**: all students can access.
    - **Hidden from students**: no students can access the item. You can choose whether it is completely hidden or whether to show the item without allowing access.
    - **Release conditions**: visibility managed based on certain conditions (see section below).

![Decorative](images/content-visibility-options.png)

!!! Warning

    Making a Learning Module or Folder visible using this method does not automatically make the items inside visible too (ie. hidden nested items will remain hidden).

## Show/hide multiple items

<div markdown class="grid">
<div markdown>
Use the Batch Edit function to quickly change the visibility of multiple items at once. For example, you can use this to make a Learning Module and the items nested within it visible with only a few clicks.

This is accessed in a different way to single item visibility. See our [Batch Edit guide](../ultra/batch-edit.md) for details.
</div>
![Access Batch Edit through the three dots icon in teh top right of the Course COntent area](images/batch-edit-batch-edit.png)
</div>

## Release conditions

![Decorative](images/content-visibility-release-conditions.png)

Items can also be shown based on certain conditions:

| Condition      | Details | Example uses |
| -------------- | ------- | ------------ |
| Select members | Show to specific users or groups | **Teaching**: release different topic to each project group </br> **Assessment**: limit access to resit submission point only to resit students
| Date/time      | Show/hide at a specific time | **Teaching**: Release module materials at appropriate time </br> **Assessment**: show submission point from a specific date |
| Performance    | Show if students submit, complete or receive a certain score for a markable item | **Teaching**: release workshop materials after completing a pre-workshop quiz </br> **Assessment**: release extension activities only for high quiz scores |

For greater control, conditions can be combined (eg. date and specific group) and multiple rules can be set (eg. different dates for different groups).

### Create a rule

1. Open the item visibility drop-down menu and and select **Release conditions**.
2. Set conditions:
    - *Select members*: click the **Specific members or groups** option, then the relevant Individual member(s) and/or Group(s).
    </br>![Decorative](images/content-visibility-release-condition-members.png)
    - *Date/time*: click the check box then enter **Access from** and/or **Access until** dates.
    </br>![Decorative](images/content-visibility-release-condition-date.png)
    - *Performance*: click the check box then select the relevant **Markable item** (Test, Assignment, Discussion etc.) and **Mark Requirement**. Mark options are based on how that specific item is marked.
    </br>![Decorative](images/content-visibility-release-condition-performance.png)
3. Click **Save**.

<div markdown class='grid'>
<div markdown>
When will content appear?

- After saving the rule, check the summary is correct.
- If you have added Date/time or Performance conditions, select whether to **Show** (default) or **Hide** the item in the content area before the release conditions are met.
</div>
![Decorative](images/content-visibility-when-appear.png)
</div>

### Edit or delete a rule

To make changes after setting up a rule:

- If using multiple rules, click the relevant rule to show the options.
- *Edit conditions*: make changes as above and click **Save**.
- *Delete the rule*: click the **three dots icon** alongside the rule name and select **Delete**.

!!! Note 

    If all release conditions are removed, the item visibility will default to *Hidden*. This can be changed manually.

### Multiple rules

Multiple rules can be added to the same item to set different release conditions for different students. For example, use two rules to give one group early access to an item:

- Rule 1: release to the early access group on date 1
- Rule 2: release to all users on date 2

To add multiple rules:

1. Set up Rule 1 as above. It may be helpful to also click the **pencil icon** and set a descriptive rule name.
2. Click the **Add new rule** button under *When will content appear?*.
3. Repeat as needed.