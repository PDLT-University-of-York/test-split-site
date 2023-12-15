---
 tags:
   - Ultra 
   - Advanced
   - Administration
---

# Enrol a student cohort

!!! Summary
 
    Student cohorts can be automatically enrolled on a Learn Ultra course or organisation based on their SITS module code (eg. MAN000xxx), or a larger cohort grouping (eg. All Yr 1 UGs in <dept>). Note: It is not possible to automatically bulk enrol students by programme or route code.

## Background
This guide explains how to automatically enrol a cohort of students on VLE modules using SITS group users.

Most student enrolments on VLE sites make use of “group users” created from records in the University's central records service, SITS. For every academic course with a module code in SITS, a SITS group user exists in the VLE.

The VLE communicates with SITS every morning around 9am, at this point:

* All students enrolled on modules in SITS that have matching SITS group users assigned to VLE sites automatically get/maintain access to those VLE sites.
* All students that have been removed from a module code in SITS in the last 24hrs get automatically removed from any VLE sites with the matching group user.  Students that have gone on to a Leave of Absence (LOA) or have left the University in the last 24hrs also have their access removed at this point. 

Whilst the process of synchronising group users between the VLE and SITS is automatic, the group users themselves must be manually enrolled on the relevant VLE course sites by an instructor - This guide explains how to do that. Numerous group users can be enrolled on the same VLE site without issue, and one group user can be used on multiple sites.

## Text Steps - Enrolling a Cohort via SITS Module Code (aka a "SITS Group User")

From within the course site in which you want to enrol the user:

1. Locate the Class Register in the left hand menu.
2. Click on View everyone on your course.
3. Click the + sign (top right) to add users.
4. Type the module code for the students you wish to enrol, (eg. LAW00006M, IPC00014M). 
5. Carefully select the correct group of students. Check for level, year and semester.
    * Note: If there are multiple entries in the results list ensure you pick the group for the correct academic year and semester - this information is displayed in the user id eg group.sits.module_2023-tft00066M-s1-a
6. Click the + sign next to the group you wish to enrol.
Use the dropdown to switch from Student to Guest. (This is important. Choose Guest and not student when enrolling a group user. When the group is pulled through, each student will become a Student).

The user group will be enrolled. Students will be added to the course overnight at ‘students’, during the next synchronisation with SITS which occurs between 6am and 9am each morning. Remember: [your site must be set as available to students](https://vle-support.york.ac.uk/ultra/site-availability/) for them to be able to access it once enrolled.


## Text Steps - Enrolling a Cohort via Larger Groupings (aka a "People Group User")
Follow steps 1 to 3 above to View everyone on your course > click the + sign.

1. Type a cohort keyword like postgraduate or archaeology to see all the groups available.
2. It can be hard to differentiate between the groups due to the way Blackboard truncates the title of the group users. If you have access to an Original site, it may be easier to find the group users you need there and then copy/paste the people group user over to your newer site - see box below.
3. Go back to Step 1 above in the Ultra site to enrol the group in your site. Remember to enrol the group user as Guest, remember they will enrol overnight and individuals will magically become Students on the site.
 
!!! Note: Finding group users with an Original site 

    1. Visit your old Original site where you have instructor access and click on Users and Groups in the left hand menu.
    2. Click Users.
    3. Click Enrol User > Find Users to Enrol.
    4. Click Browse. In the pop-up window that appears, choose Last Name, Contains, and type the keyword for the group, eg postgraduate or Archaeology
    5. Note the username which will appear as something like ‘group.people.dept_00##.atree_##’ 

## Further Help
* View our [Ultra and other tools help pages](https://vle-support.york.ac.uk/).
* See our ["Introduction to Learning Technologies" Help Pages](https://subjectguides.york.ac.uk/learning-tech)
* [Contact Us, the Digital Education Team](https://elearningyork.wordpress.com/contact/).