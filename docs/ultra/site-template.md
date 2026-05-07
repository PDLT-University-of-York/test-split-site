---
tags:
    - Key guide - teaching
    - Key guide - admin
    - Accessibility
    - Ultra
---

# VLE site template: compliance reporting

!!! summary
	To assist with departmental site QA review processes, a template compliance report is produced at the end of each semester. This report is intended as a starting point, and is not a direct judge of site or module quality.

Templates have been collaboratively developed with departments. These apply the [Site Design Principles](../ultra/site-design-principles.md) to specific teaching needs whilst also ensuring broad consistency across the institution.

Each module site should use the provided template; this is key for supporting accessibility and improving wider student experience.

## Current report

!!! tip
    The dashboard is only available to users logged into a UoY Google account.    

The current report is a snapshot of templating compliance and Ally data available on **06/05/2026**. The report dashboard is embedded below, including:

- Page 1 - Templating & Ally: faculty overview
- Page 2 - Templating: Faculty & department summary
- Page 3 - Templating & Ally: Site details

There are filters in the top bar and buttons to move between pages in the bottom right. To view detail more clearly, you can [open the report dashboard in a new window](https://datastudio.google.com/reporting/aeddd47e-f614-4a0f-aa48-1aa9dc1a3ab3/page/p_1oclt0g92d). There is also use a bottom panel within the embed to navigate through pages or open the report in full screen.

<iframe width="100%" min-width="600px" height="350px" src="https://datastudio.google.com/embed/reporting/aeddd47e-f614-4a0f-aa48-1aa9dc1a3ab3/page/p_1oclt0g92d" frameborder="0" style="border:0" allowfullscreen sandbox="allow-storage-access-by-user-activation allow-scripts allow-same-origin allow-popups allow-popups-to-escape-sandbox"></iframe>

## Report methodology

The report performs a series of automatic checks against site content and compares this to the relevant departmental template. This produces two metrics which can be used to identify sites where the template (and therefore the Site Design Principles) may not be applied appropriately:

<div class="grid cards show-bullets" markdown>

- **Letter grade**

    ---

    A qualitative threshold-based summary of template compliance:

	- A: any issues are very minor
	- B: minor issues only
	- C: some medium issues that should be addressed
	- D: major issues that must be addressed
	- E: significant major issues, consider rebuilding from template

- **Numerical score** 

    ---
    
    A more nuanced summary reflecting specific issues present:
    
    - weighted average scored from 0-100%
    - increasing points are deducted for each minor, medium and major issue identified

</div>

These metrics are calculated based on three broad compliance areas:

??? Abstract "Structure"

    The Site Design Principles require content to be organised in a way that guides students through the module; in most cases a sequential weekly organisation (or unit, block etc.) is expected to support this. This could be separate sequential sections or sequential pages within a single module content section.

    The compliance reporting uses section and item naming and locations to attempt to classify the *visible* content structure. This is then evaluated based on how well it aligns with the expected template structure.

    **Site structure evaluation**

    - Good
    - Satisfactory (minor issues)
    - Partial (medium issues)
    - Needs attention (major issues)
    - Not classifiable (major issue)

??? Abstract "Required items"

    There are various templated items to ensure key information required by the Site Design Principles is available and easy to find in each site. Four items are expected at the top-level of the site, and six pages are expected within these sections:

    - Panopto/Replay Lecture Capture integration link
    - Reading List integration link
    - Module information section
        - Module overview or Welcome page
        - Staff contact details page
        - Accessibility information page
        - Library and technical support information page
    - Assessment section
        - Assessment overview page
        - Assessment criteria page

    The compliance report identifies and classifies the required items based on location and visiblility.

    **Required item status:**

    - visible: correct location
    - visible: unexpected location (medium issue)
    - hidden (major issue)
    - missing (major issue)
    - not included in template

    Specific departmental templates may not include all of these items, or they may be in different locations depending on local teaching needs. This is accounted for in the reporting.

??? Abstract "Other factors"

    The compliance reporting also identifies other content features that can suggest wider issues in terms of site organisation and template adherence. These include:

    - items that may suggest the Reading List is not being used appropriately (medium issue)
    - summative assessments located outside the assessment section (medium issue)
    - visible placeholder items, archived items or empty sections (medium issue)
    - high amounts of hidden items, unorganised items or repeated sequential items, eg. two 'Week 2' sections (minor issue)
    - Primary Instructor is not set (minor issue)

## FAQs

??? Question "Which sites are included in the report?"

    The report includes sites from the current academic year that use the standard [DEP00001C-S1-A] naming format. Sites that do not have any enrolled students are excluded, along with sites for online exams.

    Some sites may legitimately have very little content, eg. placement year modules, or other reasons why the template may not really apply. Any possible template exemption is flagged on the site report page. These sites are not excluded from departmental and faculty averages.

??? Question "Why doesn't the report update to show changes to sites?"

    The report is produced manually; it presents a snapshot of site data, and does not automatically update based on changes to sites after this point.

    Within each site, the [Ally score and report](../ultra/ally-accessibility-report.md) *does* update after site changes.

??? Question "Why is structure shown as *No content identified* when there are materials in the site?"

    Structure classification largely relies on matching item names to various item types, so **it may not be possible to classify structures with non-systematically named items**.
    
    For example, systematically-named sections ("Week 4: Navigational skills") are easily classified, but content sections named only by the topic ("Navigational skills") or the lecturer's name are much more difficult to identify. This will affect the templating score as a major issue, but it is also important to address as non-systematic item naming makes it more difficult for students to navigate content easily.

    The structure classification is also **based on visible content** only, so if all items are hidden then the content is not identified.

??? Question "Why is a required item shown as missing when it is present in the site?"

    The report matches item names in the site to a list of possible names for each required item. We have included a long list of reasonable matches for each required item, but if items are named differently they ay not be identified. If an item name matches multiple items, only one match is applied. For consistency, it's best practice to **use the item names from the template**.

    The report also only identifies **required pages within the Module Information or Assessment section or at the top-level of the site**. For example, if the assessment criteria is included but within a weekly section, it will not be picked up by the report. This reflects the need for students to be able to easily locate key items.

For further questions or feedback relating to the dashboard, reporting methodology or interpreting outcomes, please [contact our team](../help/contact-us.md) for assistance. 