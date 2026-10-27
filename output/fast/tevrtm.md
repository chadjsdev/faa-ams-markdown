---
title: "tevrtm"
source_url: https://fast.faa.gov/docs/tevrtm.pdf
source_type: pdf
converted: 2026-10-27
---


# **Verification Requirements Traceability Matrix (VRTM) Content and Format Guidance** 

|**Document #**|**VVSPT-E5-GDE-017**|
|---|---|
|**Version #**|**3.0**|
|**Version Date**|**November 20, 2018**|



**FAA WILLIAM J. HUGHES TECHNICAL CENTER ATLANTIC CITY INTERNATIONAL AIRPORT, NEW JERSEY 08405** 

### **Document Version Control** 

|**Version**|**Description Of Change **|**Date**|
|---|---|---|
|1.0|Final|08/13/2008|
|2.0|508 Formatting|09/17/2016|
|2.1|Revising to match terminology of T&E<br>Handbook (RLB)|6/25/2018|
|2.2|Release for Peer Review|09/06/2018|
|2.3|Revised as of comments from Peer Review|10/15/2018|
|2.4|Revised as of ANG-E5A comments|11/13/2018|
|2.5|Revised as of Technical Editor updates|11/16/2018|
|3.0|Final|11/20/2018|



ii 

11/20/2018 

VVSPT-E5-GDE-017 V3.0 

### **CONTENTS** 

|1<br>IN|TRODUCTION ................................................................................................................... 1|
|---|---|
|1.1|DEFINITION AND PURPOSE ....................................................................................... 1|
|1.2|BACKGROUND .............................................................................................................. 1|
|1.3|SCOPE ............................................................................................................................. 1|
|1.4|OVERVIEW OF THE TEMP VRTM ............................................................................. 2|
|1.5|OVERVIEW OF THE DT VRTM ................................................................................... 2|
|1.6|OVERVIEW OF THE OT VRTM ................................................................................... 3|
|1.7|RELATIONSHIPS AMONG THE VRTMS ................................................................... 4|
|1.8|REFERENCE DOCUMENTS ......................................................................................... 8|
|1.9|FAA DATABASE CONSIDERATIONS ........................................................................ 8|
|2<br>D|ETAILED TEMP VRTM CONTENT AND FORMAT ...................................................... 9|
|2.1|CONTENT OF THE TEMP VRTM ................................................................................ 9|
|2.2|FORMAT OF THE TEMP VRTM ................................................................................ 10|
|3<br>D|ETAILED DT VRTM CONTENT AND FORMAT .......................................................... 12|
|3.1|CONTENT OF THE DT VRTM ................................................................................... 12|
|3.2|FORMAT OF THE DT VRTM ..................................................................................... 14|
|4<br>D|ETAILED OT VRTM CONTENT AND FORMAT .......................................................... 17|
|4.1|CONTENT OF THE OT VRTM ................................................................................... 17|
|4.2|FORMAT OF THE OT VRTM ..................................................................................... 19|
|5<br>G|LOSSARY .......................................................................................................................... 23|
|6<br>A|CRONYM LISTING .......................................................................................................... 25|



iii 

11/20/2018 

VVSPT-E5-GDE-017 V3.0 

### **Intentionally Blank** 

iv 

11/20/2018 

VVSPT-E5-GDE-017 V3.0 

### **1 INTRODUCTION** 

#### **1.1 DEFINITION AND PURPOSE** 

The Federal Aviation Administration (FAA) Systems Engineering Manual defines Verification Requirements Traceability Matrix (VRTM) as a “matrix correlating requirements and the associated verification method(s). The VRTM defines how each requirement (functional, performance, and design) is to be verified, the stage in which verification is to occur, and the applicable verification method levels.” The VRTM provides the ability to trace a lower-level requirement back to its source, or “parent requirement,” and to maintain status of requirement verification. 

#### **1.2 BACKGROUND** 

The Program Requirements Document (PRD) contains all requirements for a program, whether they will be satisfied by a product development, by procedure changes, or by changes to external systems that may be in control of stakeholders other than the FAA.  The PRD has each program’s set of Critical Operational Issues (COIs), as well as the uniquely identified requirements which trace to the National Airspace System (NAS)-Requirements Document (RD), some of which are identified as Critical Performance Requirements (CPRs).  The traceability matrix in the PRD is required to trace each requirement from the PRD back to “one or more enterprise level requirements listed in the NAS-RD,” and “to a function in the Functional Analysis Document.” (See _Program Requirements Template for AMS Acquisitions_ for further detail). _Please note this process will not be applicable for mission support programs._ 

The Test and Evaluation (T&E) Handbook, included as Guidance in the Acquisition Management System (AMS) for test teams, stipulates three types of VRTMs: The Test and Evaluation Master Plan (TEMP) VRTM, the Development Test (DT) VRTM and the Operational Test (OT) VRTM. 

#### **1.3 SCOPE** 

The scope of this guidance is limited to the following VRTM templates: 

- a) TEMP VRTM 

- b) DT VRTM 

- c) OT VRTM 

This guidance will discuss the relationships of the three VRTMs above to other traceability matrices that are required to be in the following documents: 

- a) PRD 

- b) System Specification Document (SSD), provided by FAA to developer. 

- c) System/Subsystem Specification (SSS), provided by developer. 

Details of requirements for the PRD, SSD and SSS may be found in the references cited in section 1.8. 

11/20/2018 

VVSPT-E5-GDE-017 V3.0 

1 

#### **1.4 OVERVIEW OF THE TEMP VRTM** 

The TEMP VRTM shows coverage of all PRD requirements within the scope of the test program. The TEMP VRTM is used to manage and plan the test program, allocating requirements to either the DT phase, the OT phase, or both.  (See the _TEMP Template for New Investments_ ). 

The TEMP provides the initial decomposition of COIs.  COIs are decomposed in the TEMP by: 

- a) **Decomposing COIs into Measures of Effectiveness (MOEs) and Measures of Suitability (MOSs):** 

MOEs and MOSs are qualitative decompositions of the COI which must be measured to fully determine whether a COI has been satisfied. 

- b) **Further decomposing MOEs and MOSs into Measures of Performance (MOPs):** 

MOPs are measurable, quantitative/qualitative values that characterize and support the evaluation of the COIs, MOEs and MOSs.  Decomposition is preliminary during TEMP development, with final decomposition occurring in the OT Plan. 

- c) **Mapping MOEs and MOSs to PRD requirements in the VRTM:** 

As MOPs are developed by a test team, they must not conflict with the PRD or SSD. PRD requirements, including CPRs, and the SSD requirements may serve as MOPs.  If a conflict is discovered between the PRD and any MOEs, MOSs or MOPs the conflict must be resolved. 

Further information on the COI Decomposition process can be found in the COI Decomposition Guide located on the Verification & Validations (V&V) Repository in the ANG-E T&E Portal. The COI decomposition is documented in Appendix A of the test program’s TEMP. 

The TEMP VRTM is documented in Appendix B of the test program’s TEMP.  This VRTM is indexed by the numbered requirements of the PRD.  The VRTM associates each numbered requirement MOEs, MOSs and MOPs under specific COIs as documented in Appendix A.  The TEMP VRTM also provide a cross reference of program requirements and CPRs to the respective test phase(s) and test activities in which the MOEs/MOSs/MOPs are addressed. 

#### **1.5 OVERVIEW OF THE DT VRTM** 

The developer is responsible for creating and maintaining the DT VRTM, which is used as a framework for DT testing.  For those requirements in the PRD that will be addressed by a system development, FAA creates an SSD describing what must be developed to meet PRD requirements. The SSD traces requirements back to the PRD (see _FAA-STD-067, Preparation of Specifications_ ). 

Developers, (usually after a contract award), deliver a more detailed functional specification, the SSS, to meet the SSD requirements.  The DT VRTM uses the requirement identifiers in the developer’s SSS, which provides traceability back to the SSD in accordance with the Data Item Description (DID) in the contract.  The unique identifiers used by the developer in the SSS for requirements, or their child requirements, usually serve as the primary index for traceability in the SSS.  The DT VRTM must be included in the Contractor’s Master Test Plan (CMTP), lower-level DT plans, procedures documents, and reports, with additional columns completed to trace program requirements to specific documented test procedures, and to test results. 

11/20/2018 

VVSPT-E5-GDE-017 V3.0 

2 

The developer might go through a process of requirement definition and an interpretation of the SSD requirements to develop and deliver the SSS while is developing a DT VRTM. As a result, there is a possibility that the developer will revise the DT VRTM multiple times. 

#### **1.6 OVERVIEW OF THE OT VRTM** 

The OT VRTM traces COIs, and their constituent MOEs, MOSs, and MOPs to the test activities and test cases.  It also identifies requirements from the PRD (including CPRs), and the SSD that relate to each COI/MOE/MOS/MOP.  The OT VRTM may be revised as OT matures through procedure development and test conduct.  During OT reporting, the test case information such as run dates and results, will be entered into the VRTM.  The completed VRTM will be contained in the OT test reports. 

11/20/2018 

VVSPT-E5-GDE-017 V3.0 

3 

#### **1.7 RELATIONSHIPS AMONG THE VRTMS** 

The following diagrams indicate the traceability of requirements from the lowest level for a program, the DT and OT VRTMs, up to the highest level for a program, the PRD. 



The first step in program traceability development is to link the requirements in the SSD to the PRD, as illustrated in Figure 1-1.  This is the responsibility of the FAA Program Manager, and is required before Final Investment Decision (FID). 

11/20/2018 

VVSPT-E5-GDE-017 V3.0 

4 

The Program’s Test Director (or Test Directors if there are more than one), develops the TEMP which traces the PRD requirements applicable to the test program to a phase of testing (usually DT or OT).  The TEMP also includes the initial decomposition of COIs into MOEs, MOSs and MOPs, as illustrated in Figure 1-2. 



**Figure 1-2 – Traceability Between PRD and TEMP** 

11/20/2018 

VVSPT-E5-GDE-017 V3.0 

5 

The developer is responsible for preparing the SSS, which is the basis for the development of the new system.  The DT VRTM in the CMTP maps the SSS requirements to Test Activities and Test Cases, as illustrated in Figure 1-3.  The SSS shows traceability back to the SSD.  This traceability supports mapping from low-level activities during DT back to the PRD and the CPRs. 



**Figure 1-3 – Traceability Between PRD and DT Documents** 

11/20/2018 

VVSPT-E5-GDE-017 V3.0 

6 

OT planning further refines and matures the original decomposition of the COIs, MOEs, MOSs and MOPs documented in the TEMP and associates test activities and test cases back to the COIs in the OT VRTM.  As illustrated in Figure 1-4, the OT VRTM also maintains traceability back to the SSD and PRD requirements.  This diagram therefore illustrates the full traceability of all test activities back to the PRD, from both DT and OT. 

It’s recommended that Test Directors have a forward looking prospective on the traceability of the PRD and the SSD requirements such that traceability to the SSS is achieved as the process through development into DT and OT. 



**Figure 1-4 – Traceability Among Requirements Documents, Test Activities and Test Cases** 

11/20/2018 

VVSPT-E5-GDE-017 V3.0 

7 

#### **1.8 REFERENCE DOCUMENTS** 

- a) _COI Decomposition Guide, version 1,_ FAA Air Traffic Organization NextGen and Operations Planning Services, TSPAT-D3-GDE-001, November 2008 

- b) _DI-IPSC-81431A, System/Subsystem Specification (SSS), Data Item Description_ , (Sample), FAA AMS, January 10, 2000. http://fast.faa.gov/docs/sowgen_docs/dids/DIIPSC-81431A.doc 

- c) _FAA System Engineering Manual, v1.1_ , Air Traffic Organization Operations Planning, Washington, DC, September 11, 2015. https://sep.faa.gov/file/get/2974 

- d) _FAA-STD-067, Preparation of Specifications_ , FAA, December 4, 2009. https://f10011.eos-intl.net/F10011/OPAC/Details/Record.aspx?BibCode=30738591 

- e) _Program Requirements Template for AMS Acquisitions_ , Version 2.2, July 2017, FAA Offices: ANG-B, ANG-B1, ADE-200. http://fast.faa.gov/docs/programreq.docx 

- f) _Test and Evaluation Handbook,_ Version 4.0, FAA William J. Hughes Technical Center, VVSPT-A2-PDD-013, May 2017. 

- _g) Test and Evaluation Master Plan Template for New Investments,_ Version 5.0, FAA William J. Hughes Technical Center, VVSPT-D4-TEM-012, July 2015. 

- h) _Test and Evaluation OT Test Plan Template,_ FAA William J. Hughes Technical Center, Version 3.0, VVSPT-D4-TEM-017, October 2011 

#### **1.9 FAA DATABASE CONSIDERATIONS** 

For full traceability, the FAA Dynamic Object Oriented Requirements System (DOORS) database should make use of all fields in the TEMP, DT, and OT VRTMs.  With this full traceability, System Engineering would have insight into the test program on requirement status.  The test program would be able to use the FAA DOORS database to generate and manage the VRTMs. 

11/20/2018 

VVSPT-E5-GDE-017 V3.0 

8 

## **2 DETAILED TEMP VRTM CONTENT AND FORMAT** 

#### **2.1 CONTENT OF THE TEMP VRTM** 

Table 2-1 briefly describes the content for each column of the TEMP VRTM.  Table 2-3 provides an example of the TEMP VRTM.  Detailed format for each column is provided in the next section. Each VRTM reflects modification date information in the title. 

Each VRTM reflects preparation and modification date information. 

**Table 2-1 – Brief Description of TEMP VRTM Columns** 

|**Column Title**|**Content**|
|---|---|
|PRD ID|A unique identifier from the PRD.|
|REQTEXT|The text of the requirement from the PRD.|
|CPR (N/A or #)|Whether the requirement has been identified as a CPR, which<br>may be referenced by its additional CPR number in Appendix<br>1 of the PRD.|
|TEST PHASE|Identification of the T&E Phases, which will verify the<br>requirement.|
|VERIF METH|Identification of the Verification Method to be used for in<br>each phase.|
|MOE /MOS #*|Identification of any measures under a related COI for this<br>requirement.|
|MOE / MOS||
|TEXT*|The text of the measure identified in the sixth column.|
|MOP #*|The ID of related MOPs for the requirement.|



The TEMP VRTM can optionally contain additional columns such as the named T&E Activity within the phase and the Success Criteria, but these may not be known, until the later phases of planning. 

* _Note: Programs might use a separate spreadsheet to decompose COIs to MOEs, MOSs and MOPs_ 

11/20/2018 

VVSPT-E5-GDE-017 V3.0 

9 

#### **2.2 FORMAT OF THE TEMP VRTM** 

For each column in the TEMP VRTM, Table 2-2, below has a row, which describes the format for the column’s entry. 

**Table 2-2 – Format of TEMP VRTM Columns** 

|**Field/Column /**<br>**Attribute**|**Description**|**Example Values**|
|---|---|---|
|PRD ID|The requirement identifier<br>from the PRD|PRD-515<br>PRD-2112|
|REQ TEXT|The full text of the<br>requirement from the source<br>document.|The system shall be<br>designed using …<br>----<br> Does the SYSTEM<br>provide the ability<br>to…?|
|CPR (N/A or #)|If this TEMP item is a CPR,<br>or child requirement of a<br>CPR, the number from the<br>CPR table in the PRD goes<br>here, otherwise, put“N/A.”|N/A<br>4|
|TEST PHASE|The T&E phase in which the<br>requirement will be verified.|DT, OT|
|VERIF METH|The method that will be used<br>for verification of the<br>requirement. Usually either<br>Analysis, Demonstration,<br>Inspection, or Test.|A,<br>D,<br>I,<br>T|
|MOE /MOS #|Measures under related COIs<br>in which the requirement will<br>be verified.|MOE 1.3<br>MOS 9.1|
|MOE / MOS<br>TEXT|The text of the related MOE,<br>or MOS.|SYSX automatically<br>provides Terminal data<br>received from…|
|MOP #|ID of related MOP.|MOP 1.3.2|



11/20/2018 

VVSPT-E5-GDE-017 V3.0 

10 

#### **Table 2-3 – Example of TEMP VRTM** 

### **TEMP VRTM FOR [** **_PROGRAM_ ] – modified** **_[Date]_** 

|**PRD ID**|**REQ TEXT**|**CPR**<br>**(N/A**<br>**or #)**|**TEST**<br>**PHASE**|**VERIF**<br>**METH**|**MOE /**<br>**MOS #**|**MOE / MOS TEXT**|**MOP #**|
|---|---|---|---|---|---|---|---|
|PRD-0128|SYSX shall provide the latest<br>Terminal data automatically in<br>accordance with registered<br>parameters.|3<br>3|DT<br>OT|D<br>T|N/A<br>MOE<br>1.3|N/A<br>SYSX automatically provides<br>Terminal data received from RVR<br>to NEMS in accordance with the<br>NEMS Asynchronous Messaging<br>ICD.|N/A<br>MOP 1.3.1<br>MOP 1.3.2<br>MOP 1.3.3|
|||3|OT|D|MOS<br>1.4|SYSX automatically provides<br>Terminal data received from ASDE-<br>X to NEMS in accordance with the<br>NEMS Asynchronous Messaging<br>ICD.|N/A|
|PRD-0154|Data communications training<br>systems must simulate data<br>communications operator<br>position functionality at<br>operator positions.|N/A|OT|D|MOS<br>9.1|Training enables Tech Ops<br>personnel to maintain Data<br>Comm operations.|MOP 9.1.1<br>MOP 9.1.2|
|PRD-0201|The system shall have a<br>response time from user input<br>to system output in accordance<br>with the NAS-RD-2013.|5<br>5|DT<br>OT|T, A<br>D|N/A<br>MOE<br>4.1|N/A<br>The system allows the sending<br>user to designate the type of<br>response required|N/A<br>MOP 4.1.1<br>MOP 4.1.2|
|||5|OT|T|MOS<br>4.2|The system displays user response<br>to an electronic message.|N/A|



11/20/2018 

VVSPT-E5-GDE-017 V3.0 

11 

## **3 DETAILED DT VRTM CONTENT AND FORMAT** 

The DT VRTM lists all of the requirements that must be met by the system to satisfy the functional and performance requirements in the program’s SSS.  As described in the DT overview (Section 1.5) the SSS requirements must trace to the SSD. 

The following table describes the required fields/columns of the DT VRTM.  The DT VRTM is under the control of the developer. The government stipulates required content and format to a prime contractor in the DIDs for deliverables that include DT VRTMs. 

#### **3.1 CONTENT OF THE DT VRTM** 

Table 3-1 briefly describes the content for each column of the DT VRTM.  Table 3-3 provides an example of the DT VRTM.  Detailed format for each column is provided in the next section. Each VRTM reflects modification date information in the title. 

**Table 3-1 – Brief Description of the DT VRTM Columns** 

|**Column Title**|**Content**|
|---|---|
|SSS ID|A unique identifier that will allow unambiguous reference to the requirement<br>in each row of this DT VRTM. The developer may use a proprietary format<br>from the SSS.|
|REQTEXT|The text of the requirement,includingsection number.|
|REQ/PARENT<br>TRACE|The immediate source of the requirement (“Parent Requirement”), which<br>would usually be from the SSD, but sometimes comes from the SSS for a<br>“child” or derived requirement.|
|PRD TRACE|The requirement identifier from the PRD that the requirement traces to,<br>usuallyindirectlythrough the SSS,and SSD.|
|CPR (N/A OR #)|Whether the requirement has been identified as a CPR, which may be<br>referenced by its CPR number from Appendix 1 of the PRD.|
|ACTIVITY ID|Identification of the DT Activity, or Activities in which the requirement will<br>be verified.  This column may have multiple entries, in “sub-rows,” for<br>multiple Activities that verify the requirement, such as FAT, SAT, etc.|
|TEST CASE ID|The identifier for the specific test case(s) associated with the activity, which<br>will verifythe requirement.|
|VERIF<br>METHOD|Identification of the Verification Method for each DT test case identified.|
|RUN DATE|Either theplanned or the actual date for the test case execution.|
|TEST RESULT|The result of the test case.  Pass,Fail,Partial|



11/20/2018 

VVSPT-E5-GDE-017 V3.0 

12 

The Test Case ID column of the DT VRTM can optionally be expanded into multiple columns, such as those described in the _T&E Handbook_ (i.e., Test Case Group, Test Case, Step), but DT test case structure would be defined by the developer. As development matures, columns such as Success Criteria may be added. 

11/20/2018 

VVSPT-E5-GDE-017 V3.0 

13 

#### **3.2 FORMAT OF THE DT VRTM** 

For each column of the DT VRTM, Table 3-2 below has a row which describes the format for the column’s entry. 

**Table 3-2 – Format of DT VRTM Columns** 

|Column (or<br>Attribute)|Type|Description|Example Values|Target<br>Document|
|---|---|---|---|---|
|**SSS ID**|Text|The requirement number from the<br>System/Segment Specification<br>(SSS, or “B-level Spec”), usually<br>provided by the developer|Proprietary format<br>SSS-736<br>SSS-12953|DT Plan|
|**REQ TEXT**|Text|The full text of the requirement<br>from the source document.|The SYSTEM must<br>enable all<br>SYSTEM Services<br>identified in Table<br>3-1 …|DT Plan|
|**REQ/PARENT**<br>**TRACE**|Text|The requirement number of the<br>System Specification Document<br>(SSD, or “A-level Spec”), that<br>this requirement traces back to,<br>and if there is an applicable<br>parent SSS ID #|SSD-10864<br>SSS-3 [new child]|DT Plan|
|**PRD TRACE**|Text|The parent PRD requirement that<br>was the indirect source for this<br>DT VRTM item.  This<br>information should be carried<br>forward in the System<br>Specification Document (SSD), to<br>the System/Segment Specification<br>(SSS)|PRD-380|DT Plan|
|**CPR (N/A OR #)**|Text|If this DT VRTM item is a CPR,<br>or child requirement of a CPR,<br>the number from the CPR table in<br>the PRD goes here, otherwise, put<br>“N/A.”|N/A<br>4|DT Plan|



11/20/2018 

VVSPT-E5-GDE-017 V3.0 

14 

|Column (or<br>Attribute)|Type|Description|Example Values|Target<br>Document|
|---|---|---|---|---|
|**ACTIVITY ID**|Text|The name of the test series in the<br>DT program where the<br>requirement will be tested.  This<br>column may have multiple<br>entries, in “sub-rows,” for<br>multiple Activities that verify the<br>requirement, such as FAT, SAT,<br>etc.  The remaining columns<br>would likewise need to have<br>multiple corresponding entries.|Factory Acceptance<br>Testing,<br>Site Acceptance<br>Testing|DT Plan|
|**TEST CASE ID**|Text|The developer’s identifier for the<br>procedures that will be executed<br>to verify the requirement.|Proprietary format.|DT Procedures|
|**VERIF**<br>**METHOD**|Text|The method(s) that will be used<br>for verification of the<br>requirement.  Usually either<br>Analysis, Demonstration,<br>Inspection, or Test.|A<br>I<br>T<br>D<br>A/D<br>T/A|DT Plan|
|**RUN DATE**|Date|The proposed or actual date the<br>test case was executed|Any common date<br>formats.|DT Report|
|**TEST RESULT**|Text|The result of test case execution.|Unverified, Pass,<br>Fail, Partial,<br>Deferred|DT Report|



11/20/2018 

VVSPT-E5-GDE-017 V3.0 

15 

#### **Table 3-3 – Example of DT VRTM** 

### **DT VRTM FOR [** **_PROGRAM_ ] – modified** **_[Date]_** 

|**SSS**<br>**ID**|**REQ**<br>**TEXT**|**REQ/PARENT**<br>**TRACE**|**PRD**<br>**TRACE**|**CPR**<br>**(N/A**<br>**OR #)**|**ACTIVITY**<br>**ID**|**TEST**<br>**CASE**<br>**ID**|**VERIF**<br>**METHOD**|**RUN**<br>**DATE**|**TEST**<br>**RESULT**|
|---|---|---|---|---|---|---|---|---|---|
|SSS-<br>11|3.1 The<br>SYSTEM<br>must enable<br>all<br>SYSTEM<br>Services<br>identified in<br>Table 3-1 …|SSD-111|PRD-<br>379|7<br>7<br>7|FAT<br>I & I<br>SAT|4.5.6<br>4.5.7<br>4.5.8|T<br>T<br>D, A|01/19/2018<br>03/20/2018<br>05/20/2018|Pass<br>Pass<br>Pass|
|SSS-<br>12|3.2 The<br>SYSTEM<br>must disable<br>individual<br>SYSTEM<br>Services …|SSD-112|PRD-<br>380|N/A|FAT|2.2.1|D|01/22/2018|Fail|
|SSS-<br>34|4.1 The<br>system shall<br>provide a<br>subset of the<br>SYSB<br>services to|SSD-7|PRD-<br>997|2|*|*|*|*|Partial|
|SSS-<br>841|…<br>4.2.1 The AI<br>Service<br>Engine shall<br>provide<br>access to<br>web<br>services<br>only to<br>consumers<br>on-ramped<br>to<br>SYSTEM2.|SSD-7/<br>SSS-34|PRD-<br>997|2<br>2|FAT<br>SAT|3.4.1<br>3.4.2|T, A<br>D|01/20/2018<br>05/20/2018|Fail<br>Pass|



* Indicates a Parent where verification occurs at the Child level 

11/20/2018 

VVSPT-E5-GDE-017 V3.0 

16 

### **4 DETAILED OT VRTM CONTENT AND FORMAT** 

The OT VRTM contains the final decomposition of the COIs from the TEMP allocated to OT Activities. 

The following table describes the required fields/columns of the OT VRTM. The OT VRTM is under the control of the government Test Director. 

#### **4.1 CONTENT OF THE OT VRTM** 

Table 4-1 briefly describes the content for each column of the OT VRTM.  Table 4-3 provides an example of the OT VRTM.  Detailed format for each column is provided in the next section. Each VRTM reflects modification date information in the title. 

**Table 4-1 – Brief Description of the OT VRTM Column** 

|**Column Title**|**Content**|
|---|---|
|COI/MOE/MOS/MOP<br>ID|A unique identifier that will allow unambiguous reference to the<br>entry in each row of this OT VRTM.|
|COI/MOE/MOS/MOP<br>TEXT|The text of the COI/MOE/MOS/MOP.|
|RELATED PRD<br>REQS|Indication of which requirements in the PRD, are related to this<br>COI,MOE,MOS,or MOP.|
|PRD TEXT|The full text of the requirement from the PRD document.|
|RELATED SSD<br>REQS|Indication of which requirements in the SSD, are related to this<br>COI,MOE,MOS,or MOP.|
|CPR (N/A OR #)|Whether any of the related requirements have been identified as<br>CPRs, which may be referenced by the CPR numbers from<br>Appendix 1 of the PRD.|
|**ACTIVITY #2**<br>ACTIVITY ID|The OT Activity, or Activities in which the MOE/MOS/MOP will<br>be verified.  This column may have multiple entries, in "sub-rows,"<br>for multiple Activities that verify the item, such as Integration<br>Testing, Operational Effectiveness and Operational Suitability<br>Testing (OE/OS), etc.|
|TEST CASE ID|The identifier for the specific test case(s) associated with the Test<br>activity.|
|VERIF METHOD|The Verification Method for each OT test case identified.|
|RUN DATE|Either the planned or actual date for the test case execution.|
|TEST RESULT|The result of the test case’s execution. Pass,Fail,Partial,Limited|



As the program matures, additional OT VRTM columns, such as Success Criteria, maybe added. 

11/20/2018 

VVSPT-E5-GDE-017 V3.0 

17 

The Test Case ID column of the OT VRTM can optionally be expanded into multiple columns, such as those described in the _T&E Handbook and the T&E OT Test Plan Template_ (i.e., Test Case Group, Test Case and Step). 

11/20/2018 

VVSPT-E5-GDE-017 V3.0 

18 

#### **4.2 FORMAT OF THE OT VRTM** 

For each column in the OT VRTM, Table 4-2 below has a row, which describes the format for the column’s entry. 

**Table 4-2 – Format of OT VRTM with Example Entries** 

|**Field/Column/Attribute**|**Type**|**Description**|**Example**<br>**Values**|**Target Document**|
|---|---|---|---|---|
|**COI/MOE/MOS/MOP**<br>**TEXT**|Text|The full text of the<br>COI, MOE, MOS<br>or MOP|Does the<br>SYSTEM<br>provide the<br>ability to<br>capture and<br>process NAS<br>data?|OT Plan|
|**COI/MOE/MOS/MOP ID**|Text|The COI number<br>from the TEMP or<br>a decomposed<br>MOE, MOS or<br>MOP number|COI_1|OT Plan|
|**RELATED PRD REQS**|Text|Any related PRD<br>requirements.|PRD221,<br>PRD124,<br>PRD514,<br>PRD515|OT Plan|
|**RELATED PRD TEXT**|Text|The full text of the<br>applicable PRD<br>Requirement|The System<br>must have the<br>ability to<br>receive,<br>process and<br>maintain<br>flight data.|OT Plan|
|**RELATED SSD REQS**|Text|Any related SSD<br>requirements.|SSD6, SSD7,<br>SSD10,<br>SSD27,<br>SSD458|OT Plan|
|**CPR (N/A OR #)**|Text|If this OT VRTM<br>item relates to a<br>CPR, or child<br>requirement of a<br>CPR, the number<br>from the CPR<br>table in the PRD<br>goes here,<br>otherwise, put<br>“N/A.”|N/A<br>4|OT Plan|



11/20/2018 

VVSPT-E5-GDE-017 V3.0 

19 

|**Field/Column/Attribute**|**Type**|**Description**|**Example**<br>**Values**|**Target Document**|
|---|---|---|---|---|
|AC**ACTIVITY ID**<br>TIVITY #2|Text|The name of the<br>Activity or<br>Activities, in the<br>OT program<br>where the<br>MOE/MOS/MOP<br>will be tested.<br>This column may<br>have multiple<br>entries, in “sub-<br>rows,” for<br>multiple Activities<br>that verify the<br>MOE/MOS/MOP,<br>such as<br>Integration<br>Testing,<br>Operational<br>Effectiveness and<br>Operational<br>Suitability Testing<br>(OE/OS), etc.  The<br>remaining<br>columns would<br>likewise need to<br>have multiple<br>corresponding<br>entries.|NAS<br>Integration<br>Testing<br>Stability<br>Testing<br>Op.<br>Effectiveness<br>Testing|OT Plan|
|**TEST CASE ID**|Text|The identifier for<br>the procedures<br>section and steps<br>that will include<br>this<br>MOE/MOS/MOP.<br>This column may<br>be broken out into<br>multiple columns,<br>to include Case<br>Group, or Step, as<br>per the templates<br>for OT plans and<br>procedures.|1.5.4.1|OT Procedures|
|**VERIF METHOD**|Text|The method(s)<br>that will be used<br>for verification of<br>the<br>MOE/MOS/MOP<br>Usually either|A, D, I, T|OT Plan|



11/20/2018 

VVSPT-E5-GDE-017 V3.0 

20 

|**Field/Column/Attribute**|**Type**|**Description**|**Example**<br>**Values**|**Target Document**|
|---|---|---|---|---|
|||Analysis,<br>Demonstration,<br>Inspection, or<br>Test.|||
|**RUN DATE**|Date|The proposed or<br>actual date the test<br>case was executed|Any common<br>date format.|OT Report|
|**TEST RESULT**|Text|The result of test<br>case execution.|COIs: Yes,<br>No, Limited<br>MOEs,<br>MOSs,<br>MOPs:<br>Untested,<br>Pass, Fail,<br>Partial,<br>Deferred|OT Report|



11/20/2018 

VVSPT-E5-GDE-017 V3.0 

21 

#### **Table 4-3 – Example of OT VRTM** 

### **OT VRTM FOR [** **_PROGRAM_ ] – modified** **_[Date]_** 

|**COI/MOE/**<br>**MOS/MOP**<br>**ID**|**COI/MOE/MOS/MOP TEXT**|**RELATED**<br>**PRD**<br>**REQS**|**PRD**<br>**TEXT**|**RELATED**<br>**SSD REQS**|**CPR**<br>**(N/A**<br>**OR #)**|**ACTIV-**<br>**ITY ID**|**TEST**<br>**CASE**<br>**ID**|**VERIF**<br>**METHOD**|**RUN**<br>**DATE**|**TEST**<br>**RESULT**|
|---|---|---|---|---|---|---|---|---|---|---|
|COI-01|Does the SYSTEM provide the<br>ability to capture and process<br>NAS data?|*|*|*|*|*|*|*|*|Limited|
|MOS-01.1|SYSTEM provides the ability to<br>receive, process, and maintain<br>flight data.|PRD-221|The System must<br>have the ability<br>to capture….|*|3, 5|*|*|*|*|Partial|
|MOP-01.1.1|Receive flight data messages….|PRD-2211|The System must<br>have the ability<br>to Receive….|SSD4,<br>SSD458|3|Stability<br>Test|3.5.4.1|D|9/9/2018|Pass|
|MOP-01.1.2|Perform format, logic, and range<br>checks…|PRD-2212|The System must<br>have the ability<br>to perform….|SSD6,<br>SSD10,<br>SSD27,<br>SSD458|5|Failure<br>Mode|3.5.4.2|T|9/9/2018|Fail|
|MOS-01.1.2|Provide service volume Service<br>Prediction Report updates on a<br>periodic basis, configurable to<br>between 1 to 10 minutes.|PRD-124|The System must<br>provide Service<br>Volume report….|<sup>SSD28</sup>|5|ATC<br>Ops|3.5.4|I|9/9/2018|Fail|
|MOE-01.2|Does the SYSTEM provides flight<br>data to subscribers on demand?|PRD-514|The System must<br>provide flight<br>data..|SSD12|N/A|ATC<br>Ops|3.5.5|D|10/15/2018|Pass|
|MOE-01.3|SYSTEM provides NOTAM data<br>to subscribers on demand.|PRD-515|The System must<br>provide NOTAM<br>data….|<br>SSD15|5|*|*|*|*|Pass|
|MOP-01.3.1|Provide NOTAM updates on a<br>periodic basis, configurable to<br>between 1 to 10 minutes|PRD-515|NATAM Data<br>must be provided<br>on a periodic….|SSSD15|5|ATC<br>Ops|3.5.6<br>3.5.7|I<br>T|9/16/2018<br>9/16/2018|Pass<br>Pass|



* Test Activities usually occur at the lowest level of decomposition.  COIs must be reassessed at conclusion of T&E. 

11/20/2018 

VVSPT-E5-GDE-017 V3.0 

22 

### **5 GLOSSARY** 

**Analysis (A):** Verification that is accomplished through use of one or more of the following analysis techniques to prove that an item meets specified requirements: 

- 1) Mathematical representation such as math models, algorithms, and equations 

- 2) Charts 

- 3) Graphs 

- 4) Circuit diagrams 

- 5) Data reduction/recording 

- 6) Representative data (may include data collected from previous or other equipment and system verifications) 

**Critical Operational Issue (COI):** A key operational effectiveness or operational suitability issue that must be examined during operational test to determine the system’s capability to perform its mission. 

**Critical Performance Requirements (CPRs):** Primary requirements of a solution representing attributes or characteristics considered essential to meeting the mission need that the investment program is seeking to satisfy. Critical performance requirements and associated values are specified in the program requirements document. 

**Demonstration (D):** Verification that is accomplished by operation, adjustment, or reconfiguration of items performing their designed functions under specific scenarios. The items may be instrumented and quantitative limits of performance monitored, but only observational data rather than actual performance data is required to be recorded for verification. Demonstration is often used to verify compliance with requirements in servicing, reliability, maintainability, transportability, and human factors engineering. 

<u>Note: Demonstration does not require any actions beyond those identified in the Test Steps section</u> of the associated test procedures. 

**Inspection (I):** Verification that is accomplished by a visual examination of the item, reviewing descriptive documentation, and comparing the appropriate characteristics with predetermined standards to determine conformance to requirements without the use of laboratory equipment or procedures. Examples of verification by inspection are: 

- 1) Visual analysis of the item under test, such as displays, cables, and processors. 

- 2) Reviewing descriptive documentation such as Contract Data Requirements List (CDRL) items, vendor data, and engineering drawings. 

- 3) Comparing the appropriate characteristics with a predetermined or reference standard such as FAA and industry standards. 

**Measure of Effectiveness (MOE):** First-level, qualitative decomposition of an operational effectiveness component associated with a COI. [AMS]  MOEs are qualitative decompositions of the COI which must be measured to fully determine whether a COI has been satisfied. [Derived from T&E Handbook] 

11/20/2018 

VVSPT-E5-GDE-017 V3.0 

23 

**Measure of Performance (MOP):** Quantitative values that characterize MOEs or MOSs.  These values are measurable by a test process. [AMS]  MOPs are measurable, quantitative/qualitative values that characterize and support the evaluation of the COIs, MOEs and MOSs.  Decomposition must be considered preliminary for the pTEMP and iTEMP. [T&E Handbook] 

**Measure of Suitability (MOS):** First-level, qualitative decomposition of an operational suitability component associated with a COI. [AMS]  MOSs are qualitative decompositions of the COI, which must be measured to fully determine whether a COI has been satisfied.  [derived from T&E Handbook] 

**Test (T):** Verification that is accomplished, with or without instrumentation, through systematic exercising of the application item under appropriate conditions with the collection, analysis, and evaluation of quantitative data. 

<u>Note: Acceptability of the item is determined by comparison of the data with pre-established</u> quantitative criteria, requirements, and occurrences. 

**Test Activity:** A category of test hierarchy between Test Phase and Test Case Group, with an identifiable title and reporting requirements. 

**Test Case:** A subset of test procedures that specify a) a set of product requirements to be verified and validated; b) the resources required to execute the test case; c) the specific steps that must be taken to perform the test case.  A test case is identified by paragraph number in a Test Procedures document. 

11/20/2018 

VVSPT-E5-GDE-017 V3.0 

24 

### **6 ACRONYM LISTING** 

|AMS|Acquisition Management System|
|---|---|
|ASDE|Airport Surface Detection Equipment|
|CDRL|Contract Data Requirements List<br>|
|CMTP|Contractor Master Test Plan|
|COI|Critical Operational Issue<br>|
|CPR|Critical Performance Requirement|
|DID|Data Item Description|
|DT|Development Test|
|FAA|Federal Aviation Administration|
|FAT|Factory Acceptance Test|
|FID|Final Investment Decision|
|ICD|Interface Control Document|
|MOE|Measures of Effectiveness|
|MOP|Measures of Performance|
|MOS|Measures of Suitability|
|NAS|National Airspace System|
|NEMS<br>|Network Management System<br>|
|OS|Operating System|
|OT|Operational Test|
|PRD|Performance Requirements Document|
|RD|Requirement Document|
|RVR|Runway Visual Range|
|SAT|Site Acceptance Test|
|SSD|System Specification Document|
|SSS|System/Subsystem Specification|
|SYSX|System Data and Infrastructure|
|T&E|Test and Evaluation|
|TEMP|Test Evaluation Master Plan|
|V&V|Verification and Validation|
|VRTM|Verification Requirements Traceability Matrix|



11/20/2018 

VVSPT-E5-GDE-017 V3.0 

25 


