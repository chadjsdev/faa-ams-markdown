---
title: "isgsa"
source_url: https://fast.faa.gov/docs/isgsa.docx
source_type: docx
converted: 2026-10-27
---
# isgsa

**U.S. Department of Transportation**

**Federal Aviation Administration**

Information Security Guidance

For

System Acquisitions (ISGSA)

FAA Information Security and Acquisition Management System Guidance Document

**January 2024**

Information Security Guidance for System Acquisitions (ISGSA)

ANG-B31 Document

Document Version Control Log

| **Origination/ Revision Number** | **Description** | **Date** | **Primary Author(s)** |
| --- | --- | --- | --- |
| 1 | First version published in FAST | October 2015 | AEB Security Risk Management Workgroup led by ANG-B31 |
| 2 | Changes to document formatting | April 2017 | ANG-B31 and AAP-130 |
| 3 | Changes to update document to FAA Order 1370.121 and reference the ATO ISS assessment templates. | October 2018 | ANG-B31, AIS-200, and AJW-B42 |
| 4 | Changes to address issues found during the application of the guidance to the preparation of assessments. | October 2020 | ANG-B31 with feedback from AJW-B42, AIS-200, and AJM-1310 |
| 5 | Changes to address: (1) lessons learned in the application of the guidance to the preparation of assessments and (2) FAA Order 1370.121B | January 2022 | ANG-B31 in consultation with AJW-B42, AIS-200, and AJM-1310 |
| 6 | Changes to address: (1) Ensure identification of Sensitive Flight Data and their protections in the acquisition phases of FAA systems and (2) Document current ISS assessment practices not included in the guidance but sanctioned by the assessment stakeholders. | January 2023 | ANG-B31, AJR-2, AJW-B42 |
| 7 | Changes to: (1) State explicitly that the ISGSA does not apply to national security systems, and (2) make minor changes in ISS assessment templates that have been used in ISS assessments for ATO acquisitions and proven to be very useful. | January 2024 | ANG-B31 with AJW-B42, AJR-2, and AIS-200 concurrence. |
|  |  |  |  |
|  |  |  |  |

Table of Contents

[Information Security Guidance for System Acquisitions (ISGSA) 2](#_Toc152148822)

[1. Introduction 5](#_Toc152148823)

[1.1 Statutory Background 5](#_Toc152148824)

[1.2 Purpose 6](#_Toc152148825)

[1.3 Scope and Applicability 7](#_Toc152148826)

[1.4 Relationship to the FAA Acquisition Management Process 7](#_Toc152148827)

[2. Laws, policies, guidance and standards related to the ISGSA 8](#_Toc152148828)

[3. Information Security Assessments Supporting System Acquisitions 10](#_Toc152148829)

[3.1 ISS Risk Factors Assessment 13](#_Toc152148830)

[3.2 Preliminary ISS Assessment 15](#_Toc152148831)

[3.3 Initial ISS Assessment 16](#_Toc152148832)

[3.4 Final ISS Assessment 17](#_Toc152148833)

[3.5 ISS Assessments Required by Investment Types 18](#_Toc152148834)

[4. Process for conducting the Information System Security Assessments 19](#_Toc152148835)

[4.1 The Assessment Stakeholders 19](#_Toc152148836)

[4.2 The Assessment Tasks 19](#_Toc152148837)

[4.3 The Assessment Process 20](#_Toc152148838)

[Appendix 1 Acquisition ISS Assessments Templates 23](#_Toc152148839)

[Appendix 2 Glossary 24](#_Toc152148840)

[Appendix 3 Acronyms 27](#_Toc152148841)

# Introduction

This section provides the **Information Security Guidance for System Acquisitions (ISGSA)** statutory background, purpose, scope and relationship to the FAA acquisition management policy and guidance –formally known in the FAA as Acquisition Management System (AMS). Section 2 summarizes the federal laws and regulations the ISGSA helps satisfy and the federal guidance and standards on which it is based. Section 3 provides a description of the ISS assessments supporting the acquisition planning phases and the templates that facilitate such assessments. Appendix 1 provides instructions for downloading the assessment templates, Appendix 2 provides a glossary of terms, and Appendix 3 a list of acronyms.

## 1.1 Statutory Background

Federal agencies are required by the executive and legislative branches of the U.S. government to provide security protections to information and information systems commensurate with their information security risk. The executive branch requires it as part of the policies for the management of federal information resources in the Office of Management and Budget (OMB) Circular A-130 (2016). The legislative branch promulgated a specific information security law – The 2014 Federal Information Security Modernization Act (FISMA). FISMA reiterates the OMB Circular A-130 requirement to provide protection commensurate with the information security risk to information and information systems, explicitly extends the requirement to protect systems operated by other entities on behalf of the agency, and assigns this responsibility to the head of the agency:

*FISMA Clause 3554, paragraph (a)*

*(a) IN GENERAL.—The head of each agency shall— ‘‘(1) be responsible for— ‘‘(A) providing information security protections commensurate with the risk and magnitude of the harm resulting from unauthorized access, use, disclosure, disruption, modification, or destruction of— ‘‘(i) information collected or maintained by or on behalf of the agency; and ‘‘(ii) information systems used or operated by an agency or by a contractor of an agency or other organization on behalf of an agency;*

FISMA also requires that federal agencies set up a security program to ensure information security is addressed throughout the lifecycle of each agency information system:

*FISMA Clause 3554, paragraph (b)*

*‘‘(b) AGENCY PROGRAM.—Each agency shall develop, document, and implement an agency-wide information security program to provide information security for the information and information systems that support the operations and assets of the agency, including those provided or managed by another agency, contractor, or other source, that includes— ‘‘(1) periodic assessments of the risk and magnitude of the harm that could result from the unauthorized access, use, disclosure, disruption, modification, or destruction of information and information systems that support the operations and assets of the agency, which may include using automated tools consistent with standards and guidelines promulgated under section 11331 of title 40; ‘‘(2) policies and procedures that— ‘‘(A) are based on the risk assessments required by paragraph (1); ‘‘(B) cost-effectively reduce information security risks to an acceptable level; ‘‘(C) ensure that information security is addressed throughout the lifecycle of each agency information system; …*

Accordingly, the Department of Transportation (DOT*) Cybersecurity Compendium* (supplement to the DOT Order 1351.37) and FAA Order 1370.121B: Information Security and Privacy Policy, established an FAA Security Program that requires FAA information security requirements and associated costs be addressed throughout the lifecycle of FAA systems, including their planning and acquisition phases. Lastly, the FAA AMS, Section 4.11, requires FAA organizations to use this guidance, the ISGSA, in the conduct of systems acquisitions.

## Purpose

The ISGSA assists FAA organizations in complying with FAA Order 1370.121B and its underlying government requirements by providing robust and specific guidance to define Information Security and Privacy (IS&P) requirements during planning and acquisition. Experience has shown that postponing the definition of requirements to the security authorization process is unwise as it will lead to retrofitting some requirements, which is expensive, and deferring the implementation of others, which leaves systems vulnerable to attack. The ISGSA is based on the National Institute of Standards and Technology (NIST) Special Publication (SP) 800-37 “Guide for Applying the Risk Management Framework to Federal Information Systems –A Security Lifecycle Approach.”

The ISGSA provides guidance for identifying information system security controls[[1]](#footnote-1) (requirements) based on information security risk assessments performed during the AMS planning phases for the acquisition of new information systems, services, and any new AMS investment on existing systems or services. The guidance identifies tasks, stakeholders, and the process for conducting the security risk assessments, and includes four templates to document assessment results. The instructions for downloading the ISS assessment templates can be found in Appendix 1 of this document.

In addition this guidance will facilitate: (1) the identification of information security risk for use by the Joint Resources Council (JRC), (2) the preparation of security cost and benefit factors for the investment analysis phase which in turn will help budgeting IS&P requirements on the chosen alternative solution, and (3) the prioritization of common controls over system-specific controls whenever appropriate which will foster economies of scale and standardized security.

## Scope and Applicability

Adhering to FISMA clause 3554 paragraph (b), quoted in the introduction, the ISGSA applies to the acquisition of any information system or information service that supports the operations and assets of the FAA, including systems provided or managed by another agency, contractor, or other provider. Accordingly, the ISGSA assessments apply to all FAA investment initiatives with an information service or information system component except national security systems. The ISGSA does not apply to a national security system (NSS) because NSS security controls must be identified using the Committee on National Security Systems (CNSS) Instruction No. 1253[[2]](#footnote-2) by personnel and equipment with the necessary security clearances.

Investments that do not have an information service or system component must complete an abbreviated ISS assessment (either the Risk Factors, the Preliminary, the Initial, or Final ISS assessment) following instructions in the introduction section of the corresponding ISS assessment template. Also note that “Not being connected to a network”, “the system is isolated,” or “the system is standalone” are not valid reasons for seeking assessment exception because isolated systems are subject to threats introduced by vectors other than a network, e.g. the supply chain threat, auxiliary detachable storage devices, and insider threat.

The work completed using the ISGSA templates will dovetail into a number of solution implementation activities including: (1) the in-service review where final security requirements will be made a checklist item; (2) the preparation of the investment program baseline where assessment results will input to the determination of ISS cost, schedule, performance, and benefits; and (3) the System Security Authorization where ISS assessment results will be input to the system security plan, System Privacy Threshold Assessment, system characterization document, and system architecture.

## Relationship to the FAA Acquisition Management Process

The lifecycle process for FAA assets is governed by the AMS, which is published online at <http://fast.faa.gov>, the FAA Acquisition System Toolset (FAST). Section 4.11 of the AMS refers FAA organizations seeking to acquire information systems to this document, the ISGSA, for specific guidance to define IS&P requirements during the AMS planning phases. Since the ISGSA must fit within the FAA acquisition management process (prescribed in the AMS), the ISGSA applies to investment initiatives arising from service or capability shortfalls with an information service component.

A service or capability shortfall is said to have an information service component if the service need is concerned with generating, sending, receiving, processing or storing operational information. The rationale for the applicability of the ISGSA to investment initiatives is as follows: the AMS approach is to pursue investment initiatives to fulfill service needs or capability shortfalls, yet not all shortfalls will in the end be fulfilled by the acquisition of an information service (and an underlying information system). Nevertheless, if the shortfall has an information service component, the potential security impact of the information types (flight plans, people’s names, mail delivery schedules, weather forecasts, etc.) underlying such a service can be categorized, using the Federal Information Processing Standard 199, independently of the solution to the service need[[3]](#footnote-3). The resulting security category (also referred to as the security category impact level) will be ascribed initially to the investment initiative (or prospective capability, i.e. the resulting capability that fulfills the service/capability shortfall) and will be transferred to the system fulfilling the service need, if the service need is eventually fulfilled by the information system.

Therefore the ISGSA is designed to support the information security planning of investment initiatives (with an information service component) in each of its four planning phases: (1) Service Analysis (SA), (2) Concept and Requirements Definition (CRD), (3) Initial Investment Analysis (IIA), and (4) Final Investment Analysis (FIA).

If the information service component of the service need is evident from the start, as is the case with services needs that may be satisfied by a cloud service, the investment initiative will require information risk assessments for each planning phase starting with the SA planning phase. On the other hand, if the information service component of a service need is uncertain during the SA planning phase, the information risk assessment for this phase may be omitted and folded into the information risk assessment for the CRD planning phase. Furthermore, according to the AMS Table of Acquisition Categories, some investment types are not required to go through all the AMS planning phases and thus are not required to submit the corresponding assessment reports. However, in most cases the skipped assessment template needs to be processed in conjunction with the assessment template for the next AMS planning phase as indicated in Section 3.5 below.

# Laws, policies, guidance and standards related to the ISGSA

The ISGSA assists FAA organizations in complying with federal laws and policies including:

* FAA Order 1370.121B: Information Security and Privacy Policy.
* Information security policy in AMS Section 4.11
* Federal Information Security Modernization Act (2014)
* Office of Management and Budget Circular A-130 (2016): Managing Information as a Strategic Resource
* Homeland Security Presidential Directive-7
* Homeland Security Presidential Directive-12

The ISGSA was derived from the following NIST guidance, which NIST prepared explicitly to help federal agencies comply with FISMA.

* NIST SP 800-37 “Guide for Applying the Risk Management Framework to Federal Information Systems –A Security Lifecycle Approach”
* Federal Information Processing Standard (FIPS) 199 “Standards for Security Categorization of Federal Information and Information Systems”
* Federal Information Processing Standard 200 “Minimum Security Requirements for Federal Information and Information Systems”
* NIST SP 800-53 Revision 5 “Security and Privacy Controls for Federal Information Systems and Organizations”
* NIST SP 800-53B “Control Baselines for Information Systems and Organizations”[[4]](#footnote-4)
* NIST SP 800-60 Volume I “Guide for Mapping Types of Information and Information Systems to Security Categories” and NIST SP 800-60 Volume II “Appendices to Guide for Mapping Types of Information and Information Systems to Security Categories”

Instructions in the information security templates also recommend enriching the development of information security requirements by using internal FAA lines of business guidance and DOT policy:

* DOT Departmental Cyber Security Policy 1351.37 and Departmental Cybersecurity Compendium
* FAA Order JO 1370.114: Implementation of FAA Telecommunications Infrastructure Services and Information Security Requirements in the National Airspace System
* FAA Order JO 1370.123 National Airspace System (NAS) Identity and Access Management (IAM) Policy.
* FAA Order 1600.75 Protecting Sensitive Unclassified Information (SUI).
* FAA Order 1200.22E External Requests for National Airspace System (NAS) Data.
* FAA System Engineering Manual.

# Information Security Assessments Supporting System Acquisitions

This section provides a description of the ISS assessments supporting each of the four AMS planning phases identified in Figure 1, FAA Lifecycle Management Process: (1) Service Analysis and Strategic Planning, (2) Concept and Requirements Definition, (3) Initial Investment Analysis and (4) Final Investment Analysis.

![http://fast.faa.gov/images/layout/AMSLogo_md.png](data:image/png;base64...)

Figure 1 FAA Lifecycle Management Process

The assessments will be conducted using assessment templates specific to each acquisition phase and according to the assessment process prescribed in Section 4. The assessment names, their main objectives, the AMS planning phases when they are prepared and the AMS decisions that require them are summarized in the table below.

| **ISS Assessment** | **AMS Planning Phase / AMS Decision / Decision Entity** | **Assessment Main Objectives** |
| --- | --- | --- |
| **ISS Risk Factors Assessment** | Service Analysis (SA)/  CRD Readiness Decision (CRDRD)/  FAA Enterprise Architecture Board | -Determine a provisional investment initiative security category, i.e., a provisional ranking of the damage that would result if the confidentiality, integrity, or availability of the information capability is lost.  -Characterize the security threat profile, the unauthorized persons or entities with the motivation, means, and opportunity to access and misuse the capability.  -Provide input to the cloud suitability assessment and solution concept of operations. |
| **Preliminary ISS Assessment** | Concept and Requirements Definition/  Investment Analysis Readiness Decision (IARD)/  Joint Resources Council (JRC) | -Determine the final investment initiative security category, which in turn determines the security requirements baseline from FAA Order 1370.121B  -Provide the security component for the preliminary Program Requirements Document (pPRD) based on an initial tailoring of the chosen security requirements baseline and attendant risk assessments.  -Provide the factors for a rough ISS cost estimate of alternative solutions and factors for a rough estimate of the annual operational benefits gained by implementing security requirements.  -Provide input to the determination of the investment initiative Acquisition Category (ACAT). |
| **Initial ISS Assessment** | Initial Investment Analysis/  Initial Investment Decision (IID)/  JRC | - Provide the security component of the initial PRD (iPRD) based on final tailoring of the 800-53B controls (with attendant risk assessments) and sufficiently detailed to conduct a market capability survey via a Screening Information Request.  -Update the cost and benefit factors of the preliminary ISS assessment for input to the initial business case. |
| **Final ISS Assessment** | Final Investment Analysis/  Final Investment Decision (FID)/  JRC | -Finalize the security requirements based on response to market capability survey.  -Provide input to Solution Implementation phase artifacts: the system characterization document and system security plan.  -Provide input to the Privacy Threshold Assessment. |

## ISS Risk Factors Assessment

The ISS Risk Factors Assessment is conducted during SA leading to the CRDRD. The assessment must be prepared using the ISS Risk Factors Assessment Template and information prepared separately by the service organization for the Preliminary Shortfall Analysis Report. The assessment inputs, results, as well as the processes and products the results feed are exhibited in Figure 2, ISS Risk Factors Assessment Information Flows. The results of the assessment include: (1) the Provisional Investment Initiative Security Category and the Security Threat Profile, both results feeding the Cloud Suitability Assessment; (2) a Preliminary Capability Description (from the information security vantage point), feeding the Solution Concept of Operations, which is an artifact of the CRD phase. The instructions for downloading the ISS Risk Factors Assessment Template can be found in Appendix 1 of this document.

![](data:image/x-emf;base64...)

Figure 2 ISS Risk Factors Assessment Information Flows

In contrast to the NIST Risk Management Framework (RMF), the ISGSA calls for an explicit expression of the threat profile because its goal is not only to identify information security requirements, but also provide a picture of the information security risk (potential damage and threat profile) to the Cloud Suitability Assessment and the Acquisition Category (ACAT) determination. Although the NIST RMF deals explicitly with potential damage, i.e. the FIPS-199 security category, it accounts for the threat profile only in the background: (1) predating any assessment, the typical threat profile facing federal agencies has already been factored into the NIST SP 800-53B security control baselines, and (2) during the tailoring of the security baseline, the baseline controls are adjusted to the specific threat to the prospective capability. The ISGSA follows the NIST RMF for identifying information security requirements, but in addition has guidance for expressing <u>explicitly</u> the threat profile. Armed with the security category (potential damage) and the threat profile, cloud suitability assessors may obtain an explicit estimate of the investment initiative information security risk using the SEM Risk Issue and Opportunity (RIO) approach. However the greatest value of the threat profile is in the tailoring of the security baseline based on an explicit characterization of the investment initiative threat, i.e. the threat profile, rather than based on an undocumented, and perhaps casual incomplete, understanding of threats facing the investment initiative.

## Preliminary ISS Assessment

The Preliminary ISS Assessment is conducted during CRD leading to the IARD. The assessment must be prepared using the Preliminary ISS Assessment Template, the ISS Risk Factors Assessment Report, if available, and information prepared separately by the service organization for other CRD artifacts. The assessment inputs, results, as well as the processes and products the results feed are exhibited in Figure 3, Preliminary ISS Assessment Information Flows. The results of the assessment include: (1) the partially tailored ISS requirements which will constitute Section 5.3 of the pPRD, (2) the investment initiative security category and the security threat profile, both of which are provided as inputs to the determination of the initiative’s ACAT and (3) the information security cost factors applicable to each solution alternative as input to the Range of Alternatives (RoA) report. In Figure 3, the two-headed arrow between the EIS and ISS assessments signifies that not only the ISS assessment can be an input to the EISS assessment but also the results of the EIS assessment may add to the results of the ISS assessment. The instructions for downloading the Preliminary ISS Assessment Template can be found in Appendix 1 of this document. Although not shown in Figure 3 but described in the Preliminary Assessment template, identification of the information types are coordinated with the FAA Records Management Office, and information types that fall within the Personally Identifiable Information (PII) is provided to the Privacy Threshold Assessment.

Preliminary

ISS

Assessment

Preliminary

ISS

Assessment

Template

•

Assessment Steps based on

FIPS and NIST Guidance

•

Assessment outline and common text

CRD

Reports

Preliminary ISS

Assessment

Report

Appendix C:

ISS

Requirements

ISS Risk

Factors

Assessment

Report

ACAT

RoA

•

Investment Initiative

Security Category

•

Security Threat Profile

•

Cost factors applicable

to each alternative

•

Requirements not met by

solution alternatives, if any

Starting basis for

Preliminary

assessment

Report with

Partially

Tailored

Requirements

•

1370.121B

Baseline

•

LOB Tailored

Requirements,

e.g. ATO

Matrices

Mature Information:

•

Service Need

•

Information types

•

Environment, users

•

Any relevant historical

ISS

information

pPRD

Section 5.3

EIS

Assessment

EA

Products

Shortfall

Analysis

Functional

Analysis

Solution

Conops

Figure 3, Preliminary ISS Assessment Information Flows

## Initial ISS Assessment

The Initial ISS Assessment is conducted during IIA leading to the IID. The assessment must be prepared using the Initial ISS Assessment Template, the Preliminary ISS Assessment Report, and information prepared separately by the service organization for other IIA artifacts. The assessment inputs, results, as well as the processes and products the results feed are exhibited in Figure 4, Initial ISS Assessment Information Flows. The results of the assessment include: (1) fully tailored ISS requirements which will constitute Section 5.3 of the initial Program Requirement Document (iPRD); and (2) the factors for ISS costs and benefits applicable to each solution alternative. In Figure 4, the two-headed arrow between the EIS and ISS assessments signifies that not only the ISS assessment can be an input to the EISS assessment but also the results of the EIS assessment may add to the results of the ISS assessment. The instructions for downloading the Initial ISS Assessment Template can be found in Appendix 1 of this document.

ISS Initial

Assessment

Initial ISS

Assessment

Template

•

Assessment Steps based on

FIPS and NIST Guidance

•

Assessment outline and common text

Preliminary

ISS

Assessment

Report

Starting Basis for

Initial

ISS

assessment

•

1370.121B

Baseline

•

LOB Tailored

Requirements,

e.g. ATO

Matrice

s

•

Impact of partial solutions (if any) to

investment initiative

security

category and ISS requirements

•

Cost factors applicable to each

alternative

•

ISS Component ROM for each

alternative

Initial ISS

Assessment

Report

Screening

Information

Request

Initial

Business

Case

Factors for the ISS

cost and benefits

estimate component

applicable to each

alternative

iPRD

Section 5.3

Report with

Fully

Tailored

Requirements

EIS

Assessment

ISS

Requirements

pPRD/ EA

Products

RoA

ROM

Figure 4 Initial ISS Assessment Information Flows

## Final ISS Assessment

The Final ISS Assessment is conducted during the FIA phase leading to the FID. The assessment must be prepared using the Final ISS Assessment Template, the Initial ISS Assessment Report, and information prepared separately by the service organization for other FIA artifacts. The assessment inputs, results, as well as the processes and products the results feed are exhibited in Figure 5, Final ISS Assessment Information Flows. The results of the assessment include final ISS requirements based on responses to the SIR, which will constitute Section 5.3 of the final Program Requirements Document (fPRD). The results are also input to: (1) the EIS assessment and (2) the Security Authorization templates, e.g., the System Security Plan, the System Authorization Boundary (or System Description), the System Architecture. In Figure 5, the two-headed arrow between the EIS and ISS assessments signifies that not only the ISS assessment can be an input to the EISS assessment but also the results of the EIS assessment may add to the results of the ISS assessment. The instructions for downloading the Final ISS Assessment Template can be found in Appendix 1 of this document.

Final ISS

Assessment

Final ISS

Assessment

Template

•

Assessment Steps based on

FIPS and NIST Guidance

•

Assessment outline and common text

Initial ISS

Assessment

Report

Base for Final

ISS assessment

•

1370.121B

Baseline

•

LOB Tailored

Requirements,

e.g. ATO

Matrices

Response to

Screening

Information

Request

Changes due to funding,

new interfaces, or other

•

Investment Purpose

•

Information types

•

Environment, users

iPRD/ EA

Products

iBCAR

SSP

ISR/ISD

ISS

Requirements

with final

adjustments

Final ISS

Assessment

Report

Appendix C:

ISS

Requirements

fPRD

Section 5.3

Report with

Requirements Final

adjustments

EIS

Assessment

Figure 5 Final ISS Assessment Information Flows

## ISS Assessments Required by Investment Types

The AMS Table of Acquisition Categories in Section 1.2.5 of the FAA Acquisition Management Policy provides the definitions for investment types along with the JRC decisions applicable to them. Investment initiatives with an information service or information system component need ISS assessments for any of the CRDRD, IARD, IID, or FID decisions.

Some investment types are not required to go through the IIA planning phase and jump from the CRD to the FIA planning phase; such investment types will perform the final ISS assessment using the preliminary ISS assessment, the initial ISS assessment template, and the final ISS assessment template because the ISS assessments were designed to be built progressively as described in sections 3.1 through 3.4 of this guidance. However ATO investments will be able to perform the final ISS assessment using just one template, the ATO tailored final ISS assessment template, because this ATO tailored template has all the information from the ATO tailored preliminary and initial ISS assessment templates.

# 4. Process for conducting the Information System Security Assessments

This section prescribes how the templates should be used to perform the ISS assessments that support each of the four AMS planning phases: SA, CRD, IIA and FIA.

## The Assessment Stakeholders

The ISS assessments supporting investment initiatives that may lead to the acquisition of an FAA information capability are performed by the work and interaction of stakeholders internal to the organization sponsoring the investment initiative and external FAA stakeholders that provide recommendation for concurrence with assessment results. The internal stakeholders include:

(1) The originating organization requester (sponsor): This is an individual or team acting on behalf of an organization requesting, proposing, or sponsoring the investment initiative. This stakeholder may include the ISO and is responsible for performing the assessment.

(2) The originating organization information security lead: This stakeholder, usually the organization Information System Security Officer (ISSO), ensures the assessment is performed according to the assessment process described in Section 4.3 below. If the investment does not have an ISSO, one can be assigned. The AJW-B4 organization can assign an ISSO for an ATO investment; the AIS-200 can assign an ISSO for a non-ATO investment.

(3) The originating organization Authorizing Official Designated Representative (AODR). This is the stakeholder with the prerogative to approve or reject the assessment report.

FAA organizations external to the originating organization will collaborate with the originating organization to ensure assessment results address: (1) compliance with agency-wide policies and (2) identify and address potential security issues introduced by the new investment that may impact them. Based on this collaboration, FAA external organizations will provide recommendation for concurrence. The FAA stakeholders that provide recommendation for concurrence with the assessment results include the:

(4) ATO AODR

(5) Information Security & Privacy Organization (AIS)

(6) NextGen ANG-B31 organization

(7) Program Management Organization (PMO)/ Communications, Information & Network Programs (CINP)

Note that an organization cannot play both the role of originating and external organization. For example, if an investment initiative is sponsored by NextGen, then NextGen is the originating organization and will not play the role of an external organization.

## 4.2 The Assessment Tasks

Each ISS assessment, regardless of which acquisition planning phase it supports, is accomplished through the performance of five consecutive tasks:

* Preparation
* Development
* Collaboration
* Approval
* Dissemination of results

The description of these tasks and how the stakeholders participate in them is described in the next section.

## The Assessment Process

The assessment process is summarized in Figure 6, *Process for Performing ISS Assessments in Support of Acquisition of FAA Systems*, provided at the end of this section. The assessment process is performed by the work and interaction of the stakeholders identified in a previous section. The stakeholders work and interactions are grouped in five consecutive tasks which, as shown in Figure 6, include stakeholder feedback loops.

**PREPARATION**: The originating organization arranges a strategy meeting with the originating organization information security lead to plan the assessment. The planning actions of the meeting include: (1) Review the input flows and products corresponding to the assessment to be undertaken; these flows can be found in Section 3 of this guidance, (2) Identifying points of contact that will provide information on the input flows, and (3) establishing the originating organization LOB/Staff Office (SO) expectations on assessment results.

**DEVELOPMENT**: The originating organization performs the assessment according to the ISS assessment template seeking and using feedback from the originating organization information security lead or originating organization AODR to ensure assessment results meet the originating organization LOB/SO standards and policies.

**COLLABORATION**: The originating organization writes a draft of the ISS assessment report using the corresponding ISS assessment template, and submits it to the FAA external stakeholders for review and recommendation for concurrence as follows.

The ATO AODR, via AJW-B4 (if the ATO AODR is an external stakeholder for the investment) reviews the assessment and provides a recommendation for concurrence based on potential security issues introduced by the new investment that may impact the ATO, including the NAS.

The AIS Organization (if AIS is an external stakeholder for the investment) reviews the assessment and provides a recommendation for concurrence based on compliance with agency security and privacy policy and standards.

The NextGen ANG-B31 (if ANG-B31 is an external stakeholder for the investment) organization reviews the assessment and provides a recommendation for concurrence based on:

* A review of the assessment that ensures the assessment identified all relevant information types, including SUI and SDF information types.
* A review of the information types identified in the assessment to ensure the confidentiality, integrity, and availability of each information type has controls protecting them from threats identified in the assessment.
* Compliance with ISGSA relevant policies (see Section 2 above), the Enterprise Architecture, and the NAS Requirements Document.

The PMO/CINP (if the PMO is an external stakeholder for the investment) organization reviews the assessment and provides a recommendation for concurrence based on compliance with FAA Telecommunications Infrastructure policies and requirements.

The originating organization updates the assessment report to address any issues found by external stakeholders and resubmits the draft to them; external stakeholders then update their review and recommendation for concurrence. If an external stakeholder concern is not addressed satisfactorily, the external stakeholder may raise this concern at the JRC decision meeting.

APPROVAL: The originating organization writes the final assessment report and submits it to the LOB/SO AODR for approval. The AODR reviews the assessment and may request final changes, or reject the assessment. Otherwise, the AODR approves the assessment.

DISSEMINATION OF RESULTS: Upon approval of the assessment, the originating organization disseminates assessment results as indicated in the corresponding assessment information flow diagram below.

The originating organization security lead is responsible for implementing the ISS assessment and also for notifying its completion to either the NextGen Information Security Branch ANG-B31 (for NAS and ATO Mission Support investments) or the Information Security & Privacy Service AIS-200 (for non-ATO Mission Support investments). The latter, i.e., ANG-B31 or AIS-200, in turn will confirm completion of the assessment to the JRC Secretariat. Also, the originating organization, originating organization security lead, and Program Management Office each file a copy of the ISS assessment report.

**PREPARATION DEVELOPMENT**

**COLLABORATION APPROVAL**

**DISSEMINATION**

**Originating**

**Organization**

**Originating**

**Organization**

**ISSO\***

**Originating**

**Organization**

**AODR**

**ATO**

**AODR**

**AIS**

**-**

**200**

**ANG**

**-**

**B31**

.

Perform

assessment and

obtain results using

template

Complete

assessment report

draft

Complete

assessment final

report

Provide report and

results to other

processes,

files copy

of assessment report

Ensure results

comply with

LOB/SO standards

and policies

Approve report

Ensure results

comply with

LOB/SO standards

and policies

Coordinate for ISS

Strategy meeting

**Conduct Strategy**

**meeting**

Review & provide

recommendation

for concurrence

Confirms

assessment

completion

,

files

copy of assessment

report

PMO files

copy of

assessment report

**With ISSO/ACG**

ANG-B31/AIS-200 keeps track of collaboration

comments and their adjudication

\* To get an ISSO assigned contact AJW-B4 for ATO investments and AIS-200 for non-ATO investments

**INTERNAL TO ORIGINATING ORGANIZATION**

ANG-B31/AIS-200 confirms assessment

Completion to JRC Secretariat

**PMO**

Figure 6 Process for Performing ISS Assessments in Support of Acquisition of FAA Systems

# Appendix 1 Acquisition ISS Assessments Templates

There is one ISGSA assessment template for each of the four AMS planning phases as shown in the table below.

|  |  |
| --- | --- |
| **AMS Planning Phase** | **Template** |
| Service Analysis & Strategic Planning | ISS Risk Factors Assessment Template |
| Concept & Requirements Definition | Preliminary ISS Assessment Template |
| Initial Investment Analysis | Initial ISS Assessment Template |
| Final Investment Analysis | Final ISS Assessment Template |

Subject to review by ANG-B to ensure compliance with the ISGSA, a Line of Business or Staff Office (LOB/SO) Authorizing Official (AO) may tailor the ISGSA assessment templates to suit the LOB/SO specific needs. However, if the LOB/AO tailoring requires modification of the ISGSA, the LOB/SO tailoring and ISGSA modifications will require ASAG review and AEB approval. LOB/SO investment initiatives must use the corresponding LOB/SO tailored template, if one exists. Note that any retailoring of LOB/SO tailored templates is also subject to this review process.

The ISGSA assessment templates and the approved LOB/SO tailored templates can be found within the FAST information security page: <https://fast.faa.gov/EMP_Information_Security.cfm>

A direct link to download the non-ATO assessment templates is: <https://fast.faa.gov/EMP_Information_Security_Assessment_Templates.cfm>

A direct link to download the ATO assessment templates is: <https://my.faa.gov/org/linebusiness/ato/operations/naseo/ATO_Cybersecurity_Group/issp/ato_ams_iss_templates.html>

# Appendix 2 Glossary

AVAILABILITY: Ensuring timely and reliable access to and use of information. [FIPS 199; 44 U.S.C., SEC. 3542]

CONCEPT AND REQUIREMENTS DEFINITION: During concept and requirements definition, service teams conduct a final assessment of the maturity of marketplace technology and customer requirements. Only low-risk, high-value investment increments proceed to investment analysis. The decision to proceed to initial investment analysis (Investment Analysis Readiness Decision) is made by the JRC.

CONFIDENTIALITY: Preserving authorized restrictions on information access and disclosure, including means for protecting personal privacy and proprietary information. [FIPS 199; 44 U.S.C., SEC. 3542]

INFORMATION TYPE: A specific category of information (e.g., privacy, medical, proprietary, financial, investigative, contractor sensitive, security management), defined by an organization, or in some instances, by a specific law, executive order, directive, policy or regulation. [FIPS 199]

INITIAL INVESTMENT ANALYSIS: During initial investment analysis, an investment analysis team prepares the information that enables the Joint Resources Council to select the best alternative that meets the required performance and offers the greatest value to the FAA and its customers. The investment planning focus is the business case analysis to determine the best overall solution. The decision to proceed to the final investment analysis planning phase (Initial Investment Decision) is made by the JRC.

INTEGRITY: Guarding against improper information modification or destruction, and includes ensuring information non-repudiation and authenticity. [FIPS 199; 44 U.S.C., SEC. 3542]

NATIONAL SECURITY SYSTEM: Any system (including any telecommunications system) used or operated by an agency or by a contractor of an agency, or other organization on behalf of an agency—(i) the function, operation, or use of which involves intelligence activities; involves cryptologic activities related to national security; involves command and control of military forces; involves equipment that is an integral part of a weapon or weapons system; or is critical to the direct fulfillment of military or intelligence missions (excluding a system that is to be used for routine administrative and business applications, for example, payroll, finance, logistics, and personnel management applications); or (ii) is protected at all times by procedures established for information that have been specifically authorized under criteria established by an Executive Order or an Act of Congress to be kept classified in the interest of national defense or foreign policy. [44 USC 3552]

MARKET SURVEY: The term “market survey” is used in two different contexts in AMS. In terms of the procurement and contracting process, it refers to any method used to survey industry to obtain information and comments, and to determine competition, capabilities, and estimated costs. In terms of the lifecycle management process, market surveys are an integral part of investment analysis. After initial requirements are established, market surveys are used as a basis for identifying all potential material and nonmaterial solutions to mission need [AMS definitions].

SECURITY CATEGORY: The characterization of information or an information system based on an assessment of the potential impact that a loss of confidentiality, integrity, or availability of such information or information system would have on organizational operations, organizational assets, or individuals [FIPS 199]. In this guide, security category also applies to investment initiatives with an information service need component.

SECURITY CONTROL BASELINE: The set of minimum security controls defined for a low-impact, moderate-impact, or high-impact information system that provides a starting point for the tailoring process [FIPS 200].

SECURITY THREAT: Any circumstance or event with the potential to adversely impact organizational operations (including mission, functions, image or reputation), organizational assets, individuals, other organizations or the nation through an information system via unauthorized access, destruction, disclosure, modification of information and/or denial of service. Also, the potential for a threat-source to successfully exploit a particular information system vulnerability [FIPS 200; CNSS Instruction 4009 Adapted].

SERVICE ANALYSIS: An investment initiative begins with research and service analysis when the FAA develops and evaluates new concepts and technology for possible application to the aviation service environment. The investment planning focus is on FAA service needs and service shortfalls, and only the best new concepts validated to be technically, operationally, strategically, and financially mature and beneficial will proceed to the next AMS planning phase. The decision to proceed to the next planning phase (Concept and Requirements Definition Readiness Decision) is made by the FAA Enterprise Architecture Board.

SERVICE ORGANIZATION: A service organization is any organization that manages investment resources regardless of appropriation to deliver services. It may be a service unit, program office or directorate, and may be engaged in air traffic services, safety, security, regulation, certification, operations, commercial space transportation, airport development, or administrative functions.

TAILORING: The process by which security control baselines are modified by: (i) identifying and designating common controls; (ii) applying scoping considerations on the applicability and implementation of baseline controls; (iii) selecting compensating security controls; (iv) assigning specific values to organization-defined security control parameters; (v) supplementing baselines with additional security controls or control enhancements; and (vi) providing additional specification information for control implementation. [NIST 800-53 Rev.5 Glossary].

THREAT SOURCE: The intent and method targeted at the intentional exploitation of a vulnerability, or a situation and method that may accidentally trigger a vulnerability. It is synonymous with threat agent. [FIPS 200]

THREAT: Any circumstance or event with the potential to adversely impact organizational operations (including mission, functions, image or reputation), organizational assets, individuals, other organizations or the nation through an information system via unauthorized access, destruction, disclosure, modification of information and/or denial of service. Also, the potential for a threat-source to successfully exploit a particular information system vulnerability [FIPS 200; CNSS Instruction 4009 Adapted].

VULNERABILITY: Weakness in an information system, system security procedures, internal controls or implementation that could be exploited or triggered by a threat source. [FIPS 200; CNSS Instruction 4009 Adapted]

# Appendix 3 Acronyms

|  |  |
| --- | --- |
| ABA | Financial Services Organization |
| AIS | The Information Security & Privacy Organization |
| AMS | Acquisition Management System |
| AO | Authorizing Official |
| AODR | Authorizing Official Designated Representative |
| ATO | Air Traffic Organization |
| CINP | Communications, Information & Network Programs |
| CRD | Concept and Requirements Definition |
| CRDRD | CRD Readiness Decision |
| DOT | Department of Transportation |
| EIS | Enterprise Infrastructure Services |
| FAA | Federal Aviation Administration |
| FAST | FAA Acquisition System Toolset |
| FEAB | FAA Enterprise Architecture Board |
| FIA | Final Investment Analysis |
| FID | Final Investment Decision |
| FIPS | Federal Information Processing Standard |
| FISMA | Federal Information Security Management Act |
| fPRD | final Program Requirements Document |
| FTI | FAA Telecommunications Infrastructure |
| IaaS | Infrastructure as a Service |
| IARD | Investment Analysis Readiness Decision |
| IIA | Initial Investment Analysis |
| IID | Initial Investment Decision |
| iPRD | initial Program Requirement Document |
| ISGSA | the Information Security Guidance for System Acquisitions |
| ISO | Information System Owner |
| ISSO | Information System Security Officer |
| JRC | Joint Resources Council |
| LOB | Line of Business |
| MMAC | Mike Monroney Aeronautical Center |
| NAS | National Airspace System |
| NAS RD | NAS Requirements Document |
| NESG | NAS Enterprise Security Gateway |
| NIST | National Institute of Standards and Technology |
| NSS | National Security System |
| OMB | Office of Management and Budget |
| PaaS | Platform as a Service |
| PII | Personally Identifiable Information |
| PMO | Program Management Organization |
| pPRD | preliminary Program Requirements Document |
| RMAG | Remote Management Access Gateway |
| RoA | Range of Alternatives |
| SA | Service Analysis |
| SaaS | Software as a Service |
| SEM | System Engineering Manual |
| SLA | Service Level Agreement |
| SO | Staff Office |
| VSE | Vendor Security Enclave |

1. Depending on the context, the term security control means a requirement or a safeguard (planned or implemented) satisfying the corresponding requirement. Thus by and large security controls will mean requirements during acquisition and safeguards after implementation. [↑](#footnote-ref-1)
2. CNS Instruction 1253, Categorization and Control Selection for National Security Systems [↑](#footnote-ref-2)
3. The Federal Information Processing Standard 199 applies not only to non-classified federal information systems but also to non-classified information within the federal government. [↑](#footnote-ref-3)
4. The control baselines and the guidance for their tailoring were included in the 800-53 publication up until its revision 4; however, in NIST SP 800-53 Rev 5 that tailoring has been moved to the NIST SP 800-53B publication. [↑](#footnote-ref-4)
