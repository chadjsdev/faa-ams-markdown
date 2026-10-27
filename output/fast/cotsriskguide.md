---
title: "cotsriskguide"
source_url: https://fast.faa.gov/docs/cotsriskguide.doc
source_type: doc
converted: 2026-10-27
---
# cotsriskguide

**FAA COTS Risk Mitigation Guide**

**March 2012**

**Gordon Shaffer AJE-200**

**En Route Lifecycle Engineer**

**(202-366-6429)**

**Gordon.Shaffer@faa.gov**

**Gerald McPherson TRW Systems**

**Systems Engineer**

**(202-314-1277)**

**Gerald.CTR.McPherson@faa.gov**

**Table Of Contents**

**Para No.                      Page No.**

**COTS And Risk Management …………………………………………………. 1**

**Introduction…………………..………………….…………….………… 1**

**COTS-Based Acquisitions………………………………………………. 1**

**COTS Product Benefits………………………………………………….. 1**

**COTS Product Risk Factors……………………………………………. 2**

**COTS Risk Factor No. 1:  Rapid  and synchronous changes.. 3**

**COTS Risk Factor No. 2: Different obsolescence impacts…. 3**

**COTS Risk Factor No. 3: Proprietary data………..…….…….. 4**

**COTS Risk Factor No. 4: Higher lifecycle costs………..…….. 4**

**COTS Risk Factor No. 5: Multiple configurations……..……... 5**

**COTS Risk Factor No. 6: Different quality practices...…….… 5**

**COTS Risk Factor No. 7: “As is” configuration..………..……. 7**

**COTS Risk Factor No. 8: Commercial standards…….……..... 7**

**COTS Risk Factor No. 9: Time-limited manufacturer support………………………………………………………….... 7**

**COTS Risk Factor No. 10: Information security susceptibility…………………………………………….………. 8**

**COTS Software Risks………………………………………….. 8**

**1.5 COTS Risk Mitigation Strategies………………………………..…..... 8**

**1.6 Applying COTS Risk Mitigation Strategies………………………….. 10**

**1.6.1 COTS Risk Mitigation Strategy No. 1: Involve COTS**

**knowledgeable individuals in all analytical processes…...…. 11**

**1.6.2    COTS Risk Mitigation Strategy No. 2: Involve users early**

**and throughout the program lifecycle to identify and**

**resolve COTS-related constraints……..…………………..… 12**

**1.6.3    COTS Risk Mitigation Strategy No. 3: Perform continuous**

**COTS product market research…...…....…………………… 13**

**1.6.4    COTS Risk Mitigation Strategy No. 4: Integrate market**

**research results with field data and new requirements…….. 14**

**1.6.5    COTS Risk Mitigation Strategy No. 5: Develop and**

**maintain flexible performance requirements suited to**

**the use of COTS products………………………………….…. 15**

**1.6.6    COTS Risk Mitigation Strategy No. 6: Institute and**

**maintain ongoing COTS product testing capability….…….. 16**

**1.6.7    COTS Risk Mitigation Strategy No. 7: Develop and**

**maintain non-technical COTS selection factors……….….… 18**

**1.6.8    COTS Risk Mitigation Strategy No. 8: Use COTS-sensitive**

**analytical and budget processes……………..……………….. 19**

**1.6.9    COTS Risk Mitigation Strategy No. 9: Integrate COTS-based**

**technology evolution planning within the Integrated Program**

**Plan (IPP)……………………………….….………………..… 20**

**1.6.10   COTS Risk Mitigation Strategy No. 10: Emphasize strong and**

**COTS-relevant configuration management practices….…... 21**

**1.6.11   COTS Risk Mitigation Strategy No. 11: Use a COTS-**

**experienced systems integration agent…………..……….…. 22**

**1.6.12   COTS Risk Mitigation Strategy No. 12: Leverage the**

**commercial infrastructure wherever feasible.. ………….…. 23**

**1.6.13   COTS Risk Mitigation Strategy No. 13: Avoid the**

**modification of COTS products when possible……………... 24**

**1.7   COTS Risk Mitigation for Fielded Systems………………………….…. 25**

**1.8   Summary.………..…………………….………………………………….. 26**

**Appendix A**

**References.…………………………………………………………………………….  A-1**

**Appendix B**

**Understanding COTS Obsolescence And Technology Evolution Planning...……. B-1**

**Appendix C**

**COTS Risk Mitigation Strategies and the Work Breakdown Structure…...…….. C-1**

**Appendix D**

**Obsolescence Risk Analysis....…….……………………………………………….… D-1**

**Appendix E**

**COTS Technical Performance Factors……………………………………………...  E-1**

**Appendix F**

**COTS Non-Technical Selection Factors..………………………………………….... F-1**

**Appendix G**

**Glossary of Terms………………………………………………………………….....  G-1**

**Appendix H**

**Acronym List …………………………………………………………………………  H-1**

**List of Figures**

**Figure No.                 Page No.**

**1-1  Acquisition Strategy Selection and COTS Risks……………………... 1**

**1-2  COTS Risk Mitigation Strategies/FAA Acquisition**

**Management System…………………………………………………... 10**

**B-1  COTS Product****Obsolescence Progression………………………….. B-1**

**B-2  COTS Obsolescence Management Strategies……………………… B-4**

**B-3  COTS Product Obsolescence Support Options………………….…. B-5**

**B-4 COTS Risk Mitigation/Technology Evolution Planning Process Flow……………………………………………………………………  B-7**

**D-1                  Risk Management Process Flow…………………………………….. D-1**

**D-2                  Market Research/Product Supportability Information Template.. D-2**

**D-3                  Obsolescence Analysis Worksheet Template…..……..…………… D-4**

**D-4                   FAA Risk Worksheet Template……..……………………………..  D-5**

**D-5                   Risk Mitigation Waterfall Schedule Template…….……………... D-6**

**D-6                   Risk Mitigation Action Prioritization…….……………………..…  D-6**

**D-7                   Budget Defense Rationale Template………………………………. D-8**

**D-8                   System Obsolescence Risk Profile…………………………………. D-9**

**D-9                   Automated Information System Architecture Diagram ...……… D-10**

**D-10                 AIS Operator Display Monitor (ODM) Market Research**

**Information………………………………………………………….  D-11**

**D-11                 Sample Obsolescence Analysis Answers for the ODM..………… D-12**

**D-12                FAA Risk Worksheet for AIS ODM………...………….………….  D-14**

**D-13                ODM Risk Mitigation Waterfall Chart……………………………  D-17**

**D-14                ODM Budget Defense Rationale…………………………………...  D-18**

**D-15                AIS System Obsolescence Risk Profile……………………………. D-29**

**List of Tables**

**Table No.                 Page No.**

**COTS Product Risk Factors…………………………….…………….. 2**

**1-2  COTS Risk Mitigation Strategies………….………………………… 9**

**1-3                    COTS Risk Mitigation Strategies for Fielded Systems…………….. 26**

**B-1  COTS Product Obsolescence Support Options…………………….. B-6**

**C-1  COTS Risk Mitigation Strategies, AMS and Standard WBS…….. C-1**

**D-1                   Market Research Information Element Definitions..…..…………. D-3**

**D-2                   FAA Programmatic Risk Likelihood Definitions………………… D-16**

**D-3                   FAA Technical Consequence Definitions…………………………. D-16**

**E-1  COTS Technical Performance Factors……………………………... E-2**

**F-1  COTS Non-Technical Selection Factors……………………………. F-2**

**1.0  COTS And Risk Management**

**1.1  Introduction**

     Since the introduction of the Federal Aviation Administration’s (FAA) Acquisition Management System (AMS) in 1996, the agency has fielded numerous COTS-based systems into the National Airspace System (NAS). This has been in response to the AMS policy statement that ***"stresses preference for commercial and non-developmental solutions to mission needs”.*** However, due the lack of any available internal or external guidance on how to manage the unique risks associated with COTS-based acquisitions, the FAA as well as many other Government agencies has had a variety of experiences, many of them resulting in added risk to system cost, schedule and performance. Since all future FAA acquisitions will be prioritizing the use of COTS/NDI solutions, this guide is intended to capitalize on these many “lessons-learned” from government and industry and embed them in a practical manner within the context of an acquisition management process to more effectively acquire and provide lifecycle support for COTS-based systems.  

 

**1.2 COTS-Based Acquisitions**

     AMS policy states that “Commercial off-the-shelf (COTS) is a product or service that has been developed for sale, lease or license to the general public and is currently available at a fair market value.”, For the purposes of this document, a COTS “product” includes both hardware and software.

     Acquisition strategies can range from custom-developed systems containing few COTS products to COTS-based systems (CBSs) containing mostly or exclusively COTS products as illustrated in Figure 1-1 (Acquisition Strategy and COTS Risks). As the government migrates from custom-developed systems and acquires more COTS-based system acquisitions, they will contain a mix of COTS, modified COTS, non-developmental items (NDI), glueware, middleware, custom interfaces, etc., Regardless of the percentage of COTS product use, the COTS risk mitigation strategies described in this guide apply to both new COTS-based system (CBS) acquisitions as well as systems using COTS products that have already been fielded.   

**Figure 1-1. Acquisition Strategy and COTS Risks**

     This guide is designed to provide any acquiring activity with a standard methodology for acquiring and supporting COTS products and is specifically structured to:

Identify and understand the benefits and risks associated with using COTS products 

Describe practical COTS-specific risk mitigation strategies

Provide COTS product obsolescence risk analysis and lifecycle management techniques

**1.3 COTS Product Benefits**

     An acquisition strategy that uses a high percentage of COTS products can provide the following potential benefits: 

Avoid the risks typical of the custom development approach

Reduce front-end development cost "spikes" in the budget

Allow for a more rapid infusion of current technology, tools and open system standard interfaces to support NAS modernization and sustainment 

Expand product competition across a broader market/vendor base

Use products which are built to world-wide commercial standards which foster a greater availability of inter-operable product choices

Leverage industry and market supported skill sets

     The first benefit listed above suggests that a COTS-based acquisition strategy can be viewed as a risk management approach with the goal of reducing or eliminating the potentially severe risks and resultant adverse effects typical of custom-developed systems. However, while the use of COTS products can help to deal with these “custom acquisition” risks, using COTS products also introduces other forms of risk, stemming directly from the unique characteristics of COTS products. This increased use of COTS products by the FAA and other government organizations is creating a new acquisition operations and support environment which requires that a standard approach be established for identifying and managing (i.e., mitigating) the unique risks of COTS products over the lifecycle of the system. 

     Understanding the risks associated with the use of COTS products, their mitigation strategies and how they enhance program management decision-making is discussed in the following paragraphs.

**1.4  COTS Product Risk Factors**

     The need for COTS risk mitigation activities stems from the unique market-driven risk factors (or characteristics) of the COTS products. These risk factors can be distilled into two categories – “known” risks and “unknown” risks.

     The “known” COTS hardware and software product risk factors, which are identified in Table 1-1 (COTS Product Risk Factors), are based on an extensive analysis of common government/industry lessons-learned as distilled from numerous technical documents (Refer to  HYPERLINK  \l "AppendixA" Appendix A, References).

 

**Table 1-1. COTS Product Risk Factors**

|  |  |
| --- | --- |
| **Number** | **COTS Risk Factor (Characteristic)** |
| 1 | Rapid and asynchronous changes |
| 2 | Different obsolescence impacts |
| 3 | Proprietary data. |
| 4 | Higher lifecycle costs |
| 5 | Multiple configurations |
| 6 | Different quality practices |
| 7 | “As is” configuration |
| 8 | Commercial standards |
| 9 | Time-limited manufacturer support |
| 10 | Information security susceptibility |

     Because of the rapid and asynchronous changes (risk factor #1) associated with COTS products, the procuring activity must also deal with the “unknown” future risks of obsolescence (i.e., diminishing levels of product support). This market-driven situation forces a shift in acquisition practices from rigid product source control to a more flexible and proactive technology evolution planning approach.

      COTS product risk factors or characteristics are described in the following paragraphs. Specific COTS software risks will be discussed in paragraph 1.2.11.

**1.4.1  COTS Risk Factor No. 1: Rapid and asynchronous changes**

     Commercial markets are driven by competition for larger profits and therefore for expanded market share. In the information technology sector in particular, the ongoing and rapid sequence of technological advances (e.g., greater power or speed, miniaturization, capacity, bandwidth, etc. of the underlying components) has both permitted and stimulated a correspondingly fast-paced development and introduction to the market of increasingly more capable COTS products. This competitive environment combined with rapid advances in the underlying technologies both drive and allow COTS product manufacturers to anticipate customer demands and quickly develop and release new versions of their products. As a result, they become increasingly obsolete over time i.e., diminishing levels of product support. 

     To compound the challenge of managing product obsolescence, various types of products (e.g., processors, displays, power supplies, memory, etc.) have different service lives and market release cycles and are therefore out of phase or asynchronous with each other. 

     Refer to  HYPERLINK  \l "AppendixB" Appendix B (Understanding COTS Obsolescence and Technology Evolution Planning) for more detailed information on COTS hardware and software obsolescence.

**1.4.2  COTS Risk Factor No. 2: Different obsolescence impacts**

     When a COTS product is projected to be nearing end-of-life (EOL) (i.e., out of production) or end-of-service (EOS) (i.e., no longer supported by the manufacturer), the effects of these projected product supportability changes must be examined at the product and system level to determine what action if any is needed. It is not a foregone conclusion that all products declared to be EOL or EOS need to be replaced immediately by newer versions of those products. Effects can range from no impact to high impact. The obsolescence support options that are available to address these impacts can range from taking no action to making a major system redesign. The categories of obsolescence impacts are defined as follows:

No impact – Applies when a COTS product is considered reliable and there are sufficient spares or repair parts (at acceptable prices, within the market or on-hand) to support the projected failure-driven demand over a pre-determined timeframe. In this case the product’s projected EOL/EOS status has no impact on the product or on any system using that product and therefore requires no action; 

Low impact – Applies when the supportability status of a COTS product is projected to become unacceptable and the product must be eventually replaced. A low impact situation exists if the manufacturer’s next generation product is form, fit and function (F3) compatible i.e., interchangeable); if there are other manufacturer products that are F3 compatible; and if there are no collateral impacts to interfacing products within the system. This situation typically requires compatibility testing for the new product and a documentation change to identify the new product as a suitable alternative replacement part upon failure of the old part;

Medium impact – This category of impact, like the low impact category, also applies when the supportability status of a COTS product is projected to become unacceptable and the product must be eventually replaced. A medium impact situation exists if the manufacturer’s next generation product is only fit/function or form/function (F2) compatible; if other manufacturer sources have only F2 products available; if minor software changes are required and/or if related changes to interfacing products are required. This situation can be addressed using several options including a lifetime buy of that product or product spares; technology refreshment; purchasing of the manufacturer’s data rights; extending a maintenance agreement; or including the change in a major redesign or integrated system change; 

High impact – This category of impact, like both the low and medium impact categories, applies when the supportability status of a COTS product is projected to become unacceptable and the product must be eventually replaced. However, a major impact situation exists if there are no F3 or F2 compatible replacement products or technologies available on the market. This situation typically calls for a major redesign. This situation can be addressed using several options including a lifetime buy of that product or product spares; technology refreshment; purchasing of the manufacturer’s data rights; extending a maintenance agreement; or including the change in a major redesign or integrated system change. A more detailed discussion of product obsolescence support options is contained in  HYPERLINK  \l "AppendixB" Appendix B (Understanding COTS Obsolescence And Technology Evolution Planning).

**1.4.3  COTS Risk Factor No. 3: Proprietary data**

     A COTS product manufacturer remains in business because it owns and controls the research and manufacturing processes needed to meet market demands and to keep product costs competitive. The information a COTS product manufacturer typically labels as proprietary (i.e., not for sale) includes software/firmware source code, specific manufacturing processes, detailed specifications, schematics and drawings, etc. Such information is typically required and delivered as part of a government custom development program. However, with COTS products, data is limited to specification sheets and commercial-style operations and maintenance documentation. As a result, the COTS product must be viewed as a “black box” with defined interface and performance characteristics but allowing no insight into the internal composition of that product. The maintenance concept for systems using COTS products must also change accordingly. For COTS hardware this typically involves adopting a lowest replaceable unit (LRU) e.g., circuit card, power supply, display, disk drive etc. swapping procedure and returning the failed item to a manufacturer for repair or replacement. For COTS software, the lack of source code forces a higher level of functional testing and documentation.

**1.4.4  COTS Risk Factor No. 4: Higher lifecycle costs**

     Accelerating the introduction of COTS products into government information management and military systems has been advertised as a “faster, better, cheaper” way of meeting requirements. Using COTS is a “faster” way of meeting a requirement because COTS products are readily available. Because COTS products are marketed to meet a large and diverse consumer demand for information management solutions they are characterized as being “better” able to meet general information management needs and are becoming increasingly reliable as well. Since the marketplace forces competition among the product manufacturers, using COTS products does indeed afford a “cheaper” acquisition alternative to custom development. The fact that COTS product development costs have already been assumed by the manufacturer consequently lowers the front-end development costs of a COTS-based system acquisition for the acquiring activity. However, unless a risk management program includes proactive mitigation strategies specifically oriented towards COTS-unique risks, the initial cost benefits can be offset by the often more costly fixes of the ineffectively managed risks.

     Examples of the cost considerations for a COTS-based acquisition strategy that need to be included as part of a total cost of ownership analysis include: 

Inadequate planning costs – Probably the major lifecycle cost-driver associated with the use of COTS products is the lack of effective COTS-specific planning and budgeting. When a program fails to apply COTS risk mitigation strategies, the program then loses the advantage of proactive planning and becomes increasingly reactive to emerging technology changes and COTS product obsolescence situations. These situations limit management options and force programs to adopt sub-optimized and consequently more costly solutions.  

Test and integration costs – Although development costs are reduced compared to the development costs for a custom approach, the effort (and therefore the manpower and facility-driven costs) required to successively test, integrate and deploy multiple COTS products into a system can be substantially greater over a system’s operational life than is the case with custom solutions. Underestimating the schedule re quirements for test and integration activities and the assets needed to support those activities can add cost and schedule risk to an acquisition program. Additionally, the possibility of fielding multiple system configurations also needs to be assessed to ensure that test assets are reconfigurable and capable of accurately replicating problems identified in the field. Integrating different COTS and legacy products with varying characteristics typically requires that “glue code” be developed to allow the products to interact effectively. If this development effort is underestimated (e.g., an assumption of “plug and play”) it will also add to program risk. Each product must be tested for compliance to performance requirements, conformance to open system standards and compatibility with the system with which it will be integrated.

   

Modification costs – Although not a preferred solution, in some cases a COTS product must be modified to meet a unique requirement (e.g., a legacy interface). There is a cost to actually modify the COTS product itself. There is also a cost to assume lifecycle management responsibility for that specific product because modifying a COTS product typically voids (unless functions are incorporated as part of the commercial product line) any warranty and vendor support. This forces the lifecycle support for that product to be the responsibility of the acquiring activity. Costs for documentation, maintenance, training and spares costs will increase in this situation and must be planned for in the lifecycle budgeting for that modified product.

Configuration management costs – A consequence of using rapidly changing COTS products within a given system is the strong likelihood that an acquisition of multiple copies of that system will include more than one configuration of the COTS products used in the system. This situation not only demands a rigorous application of configuration management (CM) processes to document and manage system baselines but also requires that test facilities can replicate all fielded configuration baselines. The inability to institute strong CM practices to document product and system changes and to determine the impact of product changes to all affected configurations adds technical and cost risks to an acquisition program. 

Continuous system engineering costs – Because COTS-based systems are dynamic in nature, continuous systems engineering activity is needed to perform market surveillance/research/investigation; analyze obsolescence projections; determine the available options to limit obsolescence impacts; and integrate the resulting information with new requirements and field data as part of the overall integrated program planning. A continuous systems engineering approach also requires a continuous systems engineering test environment personnel to be able to perform conformance (to commercial standards), compliance (with specified requirements) and compatibility (form, fit and function (F3) interchangeability) testing of new products and technologies. An advantage to using a COTS approach is the ability to package smaller, more evenly planned changes using technology refreshment and other change management options. This continuous system engineering effort is an additional lifecycle cost that must be planned for to ensure a proactive risk management approach.     

Obsolescence management costs – The continuous system engineering activities needed to manage obsolescence can result in more frequent engineering changes to the system. The development, deployment and configuration management of these changes is an added cost that must be included in all COTS-based system program planning. The costs for these efforts are initially developed as part of the obsolescence management strategy chosen for a program early in the acquisition planning cycle and are then continuously refined as system product obsolescence information is gathered and analyzed.

**1.4.5  COTS Risk Factor No. 5: Multiple configurations**

     During the course of developing and producing a COTS product, the manufacturer is subjected to constantly changing market availability of components (i.e. microchips, diodes, resistors, capacitors, etc.) and subassemblies (i.e. disk drive, memory device, display etc.). For example, one production lot can be functionally equivalent to the next lot but contain different components and subassemblies. If a product contains firmware or if it is a software product, revisions can be made to subsequent product releases to correct deficiencies or to add unique features to enhance product marketability. A COTS product manufacturer may or may not elect to identify these configuration changes to its customers. 

     Another driver of multiple configurations are the rapid releases of new COTS products over time (e.g., during integration and deployment). Purchasing an older product version may not be possible after a point in time therefore requiring the insertion of a newer product version. Depending on system complexity, the number of systems to be fielded and the length of time it takes to deploy them, the potential number of configurations could be significant if not managed as a risk. 

**1.4.6  COTS Risk Factor No. 6: Different quality practices**

     Not all COTS products are created equal. While many individual COTS products from different manufacturers might satisfy a particular set of functional requirements, there can be marked differences from one product to the next. Differences in the components manufacturers choose to use, quality assurance practices, manufacturing processes, labor force composition, market share, product support, upward/downward compatibility, corporate longevity, etc. can all affect the quality and therefore desirability of the products that are offered for sale. The “buyer beware” maxim applies when choosing among apparently similar products. 

**1.4.7  COTS  Risk Factor No. 7: “As is” configuration**

     Until recently the government drove technology development for military applications with large infusions of research and development (R&D) funding for custom-developed systems. The government could afford to specify exactly what was desired and therefore promoted a “buyers” market of firms interested in meeting this demand. However, military down-sizing and, more importantly, the rapid increase of consumer demand for information processing technologies has fostered a “sellers” marketplace that is no longer driven by government R&D but by a much larger (and more profitable) commercial customer-base. This means that the products made available on the open market are manufactured to meet more general consumer demands, instead of being configured to meet specific and often-inflexible government requirements. In other words “What You See Is What You Get” (WYSIWYG). The alternate choices are then limited to custom development or COTS product modification activities. Either option can be costly because the acquiring activity pays for the unique configuration and lifecycle support of that product. 

**1.4.8  COTS Risk Factor No. 8: Commercial standards**

     COTS products are typically designed and built to a variety of commercial standards that provide high-level guidance on such product characteristics as performance, quality and inter-operability. Whereas different manufacturers can develop products featuring similar or even identical performance characteristics, the ability of different products to operate with each other (i.e., their interoperability within a system) can be limited due to the use of proprietary or non-standard interfaces. The rapid obsolescence and replacement of COTS products requires stable hardware interfaces and software protocols that are designed to be “open” (i.e., to allow flexibility and adaptability) to the use of products from different sources. Such interfaces and protocols (e.g., SCSI, SQL, RS232, TCP/IP, SNMP) are provided with many COTS products using open systems interface standards such as those agreed upon by industry through such organizations as the International Organization for Standardization (ISO) and the Institution of Electrical and Electronics Engineers (IEEE). These standards allow for product improvements in areas such as quality and functionality while maintaining interface stability through the use of consistent interface design standards. 

     However, despite the benefits there are several risks inherent with the use of commercial standards. Commercial standards, like the products they affect, are also subject to continuous change to reflect technology and market realities. Maintaining awareness of the evolution of commercial standards is important. Additionally, knowing which standard to specify can sometimes be difficult if there are two or more closely competitive technologies that will all meet a particular need. One could end up specifying one standard but the market decides to choose another (e.g., BETA video tapes versus VHS video tapes). There are also situations where products built to one standard will not be inter-operable with those built to another standard. Care must be exercised when specifying which standards to impose to maximize the system’s ability to evolve over time without major redesign.     

**1.4.9  COTS Risk Factor No. 9: Time-limited manufacturer support**

     As new COTS products are introduced into the commercial market, the manufacturer must determine at what point it is no longer profitable or desirable to support the older generation products. The manufacturer must make a trade-off between selling its newest product line while at the same time not alienating the older generation product consumer base. Manufacturers for both hardware and software COTS products will strive for upward/downward product compatibility and typically support two to three previous generations of products before declaring EOS. 

     As discussed in risk factor number 1, successive generations of COTS products are rapidly introduced on the market to meet or stimulate consumer demand. Due to this rapid product turnover, it is not in the best interests of the manufacturer to stockpile or warehouse large quantities of an existing product or repair parts that may be superceded by a next generation product the manufacturer wishes to sell. To avoid both costly warehousing expenses and unmarketable excess inventory, the manufacturer minimizes his stock of product to meet current consumer demand and limits the support period for that product by using a “just-in-time” parts ordering strategy. This commercial market management strategy must be taken into account when determining the quantities of COTS products to buy for system production purposes as well as for spares and technical support to ensure lifecycle support and configuration commonality.  

**1.4.10  COTS Risk Factor No. 10: Information security susceptibility**

     When the government develops its own custom systems, it can specify and develop system information security characteristics very precisely. But the use of COTS products developed to commercial standards introduces potentially significant information security risks. For instance, the increased inter-operability among different products that meet commercial standards raises the chances that unauthorized access can be gained. Also, the use of commercial standards allows a greater number of people to be familiar with the software protocols used to manage information as well as the information security tools and approaches that are available and in use. This knowledge can be used to access or disrupt information flow. The “open-ness” of a particular architecture, the degree to which it links with other external COTS-based systems (e.g., the Internet), and the nature of the security measures in place will determine the extent to which the products and systems using them are susceptible to unauthorized access. 

**1.4.11 COTS Software Risks**

     Although the above COTS risks cover both hardware and software products, there are additional software-related factors that need to be addressed when acquiring and integrating systems using these products. They include:

Availability of software support skills;

COTS software compatibility with underlying hardware platform;

Complexity of COTS software interfaces (e.g. operating system) with other COTS software products/applications, middleware, glue code, custom/legacy interfaces;

Modifying system functionality without unknowingly exceeding a COTS software product tolerance;

Introducing “unknown unknowns” into the system with untested products (e.g., unused code, timing differences, component and firmware changes etc.);

Licensing options and costs; and

Sole-source dependency for critical software components and data rights availability.

     Identifying and understanding COTS risks is the first step to ensure that the acquiring activity can achieve the benefits of using COTS products. The next step is to manage the risks through the planning and implementation of proactive COTS risk mitigation strategies. 

**1.5  COTS Risk Mitigation Strategies**

     To effectively address COTS risks, the acquiring activity needs to implement a set of inter-related risk mitigation strategies that reflect government/industry-recognized lessons-learned (refer to  HYPERLINK  \l "AppendixA" Appendix A). These strategies are identified in Table 1-2 (COTS Risk Mitigation Strategies). For new start programs, these risk mitigation strategies are implemented early in the acquisition process and continue throughout the system’s lifecycle. Legacy system application of these strategies is discussed in the summary paragraph 1.7. Implementation tool kits have been developed for applying these strategies to both new start and legacy systems. They are available at  HYPERLINK "http://www.faa.gov/aua/resources/cots" http://www.faa.gov/aua/resources/cots at the link entitled “TOOL KIT”. 

**Table 1-2.  COTS Risk Mitigation Strategies**

|  |  |  |  |
| --- | --- | --- | --- |
| **Number** | **COTS Mitigation Strategies** | **Application**  **Benefits** | **Risk Factors**  **Addressed** |
| 1 | Involve COTS-knowledgeable   individuals in all analytical processes | Facilitates the application of COTS mitigation strategies and informed decision making | #1-6 and #8-10 |
| 2 | Involve users early and throughout the program lifecycle to identify and resolve COTS-related constraints | Reduces chances of surfacing user acceptance issues late in system development and deployment | #1, #3,  #4, #6, #7 and #10 |
| 3 | Perform continuous COTS product market research | Allows product team to project and plan for changes in technology, product configurations and obsolescence-related issues | #1, #2, #4, #5 and   #7-10 |
| 4 | Integrate market research results with field data and new requirements | Optimizes and prioritizes cost, schedule and performance factors between obsolescence-driven system changes and system upgrades | #3, #4, #9 and #10 |
| 5 | Develop and maintain flexible performance requirements suited to the use of COTS products | Allows for appropriate level of specified function description and the inclusion of COTS technical performance factors | #7-8 and #10 |
| 6 | Institute and maintain ongoing COTS product testing capability | Allows project to assess new COTS products/technologies for specification compliance, form/fit/ function compatibility and standards conformance | #1-5,  #7-8 and #10 |
| 7 | Develop and maintain non-technical COTS selection factors | Addresses important manufacturer/ product selection factors (e.g., quality) not contained in performance/ functional specifications | #1 and   #3-10 |
|  |
|  |
| 8 | Use COTS-sensitive analytical and budget processes | Allows analyses, trade studies, plans and budgets to reflect unique market-driven COTS characteristics and obsolescence projections | #1-10 |
| 9 | Integrate COTS-based  technology evolution planning within the Implementation Strategy and Planning Document (ISPD) | Provides centralized planning that captures system evolution strategy, obsolescence projections and risk mitigation decisions | #1-10 |
| 10 | Emphasize strong and COTS-relevant configuration management practices | Reduces the possibility of untested COTS product changes affecting system performance and supports multiple system configurations | #1-2 and #4-5 |
| 11 | Use a COTS-experienced systems integration agent | Facilitates acquisition, develop- ment, deployment and support activities with proven COTS-capable personnel and services | #1-10 |
| 12 | Leverage the commercial infrastructure wherever feasible | Prevents costly duplication of already existing COTS product support infrastructure | #4 and #9 |
| 13 | Avoid modification of COTS products when possible | Prevents loss of product support and increased lifecycle costs | #3 and #7 |

**1.6  Applying COTS Risk Mitigation Strategies**

     This section describes what each mitigation strategy consists of, why the strategy must be implemented, when to apply the strategy and how to implement the strategy. 

     In addition to stressing a preference for COTS products, the FAA AMS defines system acquisition and lifecycle support phases. It also describes the system engineering activities that takes stakeholder requirements and translates them into a system design. The COTS risk mitigation strategies are implemented within this context as illustrated in Figure 1-2 (COTS Risk Mitigation Strategies/FAA Acquisition Management System).

**Figure 1-2.  COTS Risk Mitigation Strategies/FAA Acquisition Management System**

**1.6.1 COTS Risk Mitigation Strategy No. 1: Involve COTS-knowledgeable individuals in all analytical processes.**

     **WHAT/WHY** - Throughout a system’s acquisition and lifecycle phases, analyses are conducted to determine needs, identify alternative means of satisfying the needs, project lifecycle costs, conduct trade studies, perform risk versus benefit comparisons, select products or to consider support strategies/options. When a COTS-based solution (either under consideration or already selected) is being analyzed, the effort requires personnel who understand the unique risks of COTS products in addition to other factors (e.g., new requirements, technology trends, market conditions, interfacing systems, standards, budget constraints, politics, etc.). The use of COTS-knowledgeable individuals allows for risk mitigation strategies to be more effectively planned and supports more informed management decision-making. This mitigation strategy addresses COTS risk factors 1-6 and 8-10.

**WHEN** - The responsible organization performing the analyses should ensure that COTS-knowledgeable individuals from the applicable systems engineering disciplines are included in all phases of the system’s lifecycle beginning with Mission Analysis. This ensures a cohesive COTS-oriented approach to all analyses that controls the risks of using COTS products. 

     During Mission Analysis, this strategy is useful to support the requirements definition activities for new or fielded systems through ongoing market research activities. These activities include the assessment of COTS-based technological opportunities and COTS product obsolescence projections to identify potential operational capability shortfalls. During this phase, early assessments of program risk are being made which should include identifying those COTS-related risks that may need to be addressed as part of a COTS-based system acquisition strategy. 

     During the early phase of Investment Analysis a cohesive COTS-oriented approach to alternatives analysis activities is needed to plan for the downstream risks of COTS use. Engineers and cost estimators must (1) identify the risks inherent to COTS products and the effects they have on the candidate COTS-based alternative solutions; (2) select which COTS technical performance factors to specify; (3) select which COTS non-technical selection factors to develop for source selection and product selection; and (4) educate team members about COTS risks mitigation strategies and their application to the project. 

     During the later phase of Investment Analysis, the design alternatives are down-selected and analyzed for affordability, the requirements are being finalized and contract requirements are being developed. During this phase, COTS-knowledgeable individuals must: (1) incorporate the COTS obsolescence management strategies and risk mitigation activities into the analytical and cost models when developing the baselines for any candidate COTS-based alternative solutions; (2) analyze the final system specification requirements to ensure that the functional descriptions are at the appropriate level for COTS products and incorporate applicable COTS technical performance factors; (3) analyze and develop COTS-related contractor tasking for incorporation into contract documentation (e.g., market research, technology evolution planning, etc.); (4) finalize the COTS non-technical selection factors for source selection evaluation as well as for product selection; (5) analyze and develop a COTS-oriented procurement methodology including the early provision of COTS-related requirements to industry using Requests for Information (RFIs), screening information requests (SIRs), bidder conferences, etc; and (6) assess COTS-product manufacturer or vendor proposals including the conduct of evaluation testing as required (e.g., operational concept demonstrations).

      During solution implementation COTS-knowledgeable individuals will: (1) support system integration testing for COTS-based systems; (2) review COTS-specific contract deliverables (e.g., trade studies, lifecycle cost estimates, technology evolution planning, market research data, etc.); and (3) refine the technology evolution planning and costs-estimates based on actual system/product configuration and COTS product information. 

     Once the system is deployed the analytical processes will: (1) monitor the performance of COTS-based systems; (2) ensure that fielded products perform as required in a real world environment according to users' needs; (3) perform market research on the system’s COTS product obsolescence projections and test alternative replacement COTS products for system compatibility; (4) execute modifications or improvements in response to projected obsolescence situations; and (5) identify funding requirements in time to limit potential system operational impacts due to product obsolescence.

**HOW** - Implementing this risk mitigation strategy begins with identifying the COTS-knowledgeable resources available to the acquiring activity. A COTS-knowledgeable individual is someone who understands the inter-relationships among commercial market forces, market research, technology trends, commercial standards, COTS product risks and risk mitigation strategies. Individuals become “COTS-knowledgeable” through:

General experience gained with other COTS-based acquisitions

Specific COTS experience gained within their subject matter expertise

Training specifically focused on the understanding and management of COTS risks (e.g., FAA COTS Risk Mitigation Workshop)

     Depending on the phase of the acquisition and the risk mitigation activities that need to be implemented as part of the system engineering process, the acquiring activity can solicit COTS-knowledgeable individuals from:

Within the acquiring organization

Within the parent organization

A program support contractor

Consultants

Consortiums 

Centers of excellence

A systems integration agent

     At a minimum, certain key program personnel (e.g., chief system engineer, project lead, cost estimator, contract specialist, logistician) should be COTS-knowledgeable to be better able to implement the COTS risk mitigation strategies. The information contained in this guide and the workshop courseware is intended to satisfy this strategy.

     It is important to note that the planning mechanism to identify the funding needed to obtain the COTS expertise and to implement the COTS risk mitigation strategies is the program’s Work Breakdown Structure (WBS). For more guidance on how to identify the resources needed for COTS-knowledgeable personnel and risk mitigation activities refer to  HYPERLINK  \l "AppendixC" Appendix C, COTS Risk Mitigation Strategies and the Work Breakdown Structure. 

     If this strategy is ignored the program will be unable to effectively identify and mitigate COTS risks thereby impacting system performance, cost and schedule.

**1.6.2 COTS Risk Mitigation Strategy No. 2: Involve users early and throughout the program lifecycle to identify and resolve COTS-related constraints.**

     **WHAT/WHY-** Early end-user (i.e., members of the operational and maintenance workforce) involvement is a common risk mitigation strategy to ensure that the requirements accurately reflect user needs. Because COTS products are developed to meet market-based needs, they are sold by the manufacturer in an “as is” configuration that may not meet all of the users documented requirements. These differences must be reconciled with the user community early in the requirements definition process to familiarize the users with the commercial technologies or products that are available to meet their needs and to determine the absolute “must have” requirements versus the more flexible (and therefore negotiable) “nice to have” requirements. This activity can include prototyping efforts and operational concept demonstrations to provide user hands-on familiarization with the capabilities of the candidate COTS products. 

     User familiarization allows for requirement prioritization and the early identification and resolution of potential suitability issues to avoid costly changes and delays during system development and deployment activities. It also allows the user community the time to become familiar with COTS characteristics and to adapt their practices in a more COTS-oriented manner. Continued and formal user participation throughout the development, integration, test and deployment activities can minimize user acceptance issues in the field. Once a system is placed in-service, this practice is continued as the system evolves and undergoes changes and updates requiring COTS products. This risk mitigation strategy addresses COTS risk factors 1, 3, 4, 6, 7 and 10.

**WHEN –** Early user involvement is exactly that; it begins early during mission analysis and continues throughout the program’s lifecycle. 

 **HOW -** The method by which users are involved in an FAA program is documented in the AMS FAA Acquisition System Toolset (FAST) under *Toolsets/Union Guidance*. It is recommended that a formal Memorandum of Understanding (MOU) be negotiated with the participating unions to describe the roles and responsibilities of the assigned participant(s). The MOU can address such topics as rotation; responsibilities; formal decision-making; empowerment; level of participation and authority; accountability and so on. A program is typically responsible for funding the user representatives’ assignments to the program office. The WBS is the vehicle to identify the requirement for this activity.

     If this strategy is ignored unexpected user acceptance issues will occur thereby impacting system schedule and cost.

**1.6.3 COTS Risk Mitigation Strategy No. 3: Perform continuous COTS product market research.**

**WHAT/WHY -** Market research is a process of collecting information about existing and emerging technologies, products, manufacturers, suppliers and their trends. It consists of market surveillance and market investigation. Market surveillance is a continuous canvassing of the commercial market to identify existing and future technologies, vendors’ products and market trends that can potentially meet existing and emergent requirements from a strategic perspective. 

     Market investigation is a more focused process of identifying and determining if specific COTS products can meet particular functional requirements. Market investigation also includes system obsolescence profiling to proactively plan for the continued support or replacement of soon-to-be obsolete products. This product level information and the associated budget requirements form the basis for sustaining the existing operations/functionality of a COTS-based system. Market research activities allow the acquiring activity to: 

Proactively anticipate obsolescence situations due to rapid and asynchronous          product changes;                                                                

Plan and budget using a broader range of product obsolescence management options rather than incur higher lifecycle costs due to more limited and costly reactive solutions;                                                                                                                       

Maintain insight into technology trends as well as internal product changes by the manufacturer to be able to test the effects of those changes to the system if necessary;               

Assess the quality of a manufacturer, the impact of the product change to a system, its suitability for the user, its information security characteristics and its supportability; and                                                                                                                                  

Determine the projected manufacturer support period and inventories for a particular product.

     This mitigation strategy addresses COTS risk factors 1, 2, 4, 5 and 7-10.

**WHEN –** Market research occurs in all of a system’s lifecycle phases. Market surveillance activities begin during Mission Analysis supported by the ongoing market investigation activities for fielded system product obsolescence. The surveillance continues through Investment Analysis until a system design is established and a product configuration set is identified. When a contract is awarded, the market investigation activities focus on system product obsolescence projections and the availability of alternate form, fit and function (F3) compatible substitute products. Once the system is deployed and continues to evolve, market investigation continues to provide product obsolescence information (refer to  HYPERLINK  \l "AppendixB" Appendix B, Understanding COTS Obsolescence and Technology Evolution Planning) and alternate product candidates for technology refresh activities. 

**HOW -** Market surveillance methods can include internet searches, attending trade shows, reading technology publications, hiring consultants, the use of screening information requests (SIRs) to prospective manufacturers/suppliers, visits to manufacturer/supplier facilities and product demonstrations. Market investigation methods can include beta testing, prototyping, compliance/conformance/compatibility testing, and manufacturer/supplier queries on product obsolescence status. Examples of obsolescence data and obsolescence profiles to be collected and developed as part of the market investigation activity are contained in  HYPERLINK  \l "AppendixD" Appendix D (COTS Obsolescence Risk Analysis).

     If this strategy is ignored there will be a greater likelihood of poor product and technology selections as well as an inability to effectively predict and mitigate COTS product obsolescence impacts. This can negatively impact program performance, schedule and cost. This strategy is considered to be the most important for either new start or fielded systems.

**1.6.4 COTS Risk Mitigation Strategy No. 4: Integrate market research results with field data and new requirements.**

     **WHAT/WHY -** In addition to collecting market information on suitable technologies and/or product obsolescence projections, data from the field on system supportability and performance and information on new requirements must be collected and analyzed together. Field data consists of reliability, maintainability and availability (RMA) data, information about logistics and supportability issues, failure trends, more efficient methods to provide a service, etc. New requirements can come in the form of functionality enhancements, budget constraints, political priorities, changes to external system interfaces, etc. The field data and new requirements information is combined with the data obtained from the market research process to analyze and determine optimal design and support alternatives (cost, schedule and performance) as part of the overall integrated program planning. This strategy is designed to: 

Ensure that product obsolescence information becomes a part of the overall system evolution planning;

Allow for technical and schedule relationships to be identified among system change factors to optimize integrated change packaging opportunities;

Establish the basis for a more complete and informed system change activity prioritization;                                                                                                                

Determine if site supportability needs such as training, spares availability, documentation, 2nd level engineering support and configuration management are impacted by the use of COTS products. 

     Information on approaches to integrating COTS obsolescence data with field data and user requirements is contained in  HYPERLINK  \l "AppendixD" Appendix D (COTS Obsolescence Risk Analysis). This mitigation strategy addresses COTS risk factors 3, 4, 9 and 10.

**WHEN –** Once a need is established and Investment Analysis activities begin, alternative solutions are examined using information derived from market research data (available technologies and products), field data (e.g., product obsolescence data, RM&A data etc.) and new user requirements. Other data that must be considered when developing alternative acquisition approaches include the availability of suitable technologies, market conditions, interfaces, standards, budget constraints and the political climate. The use of this integrated information set continues through Solution Implementation and the In-Service Management phase as engineering changes to the system are prioritized and implemented. 

**HOW –** The program must ensure that it is getting all of the aforementioned information on a continuous basis and documenting decisions based on that information within the ISPD. Using a technique similar to that identified in paragraph D.4 (Figure D-6) of this guide, it is necessary to place all program change candidates on a single schedule to determine if there are any schedule and/or technical relationships that can be combined into an integrated change package. This methodology also allows for the program to prioritize among the various categories of changes, presuming that sustainment activities will outweigh new capability.

     If this strategy is ignored the program will be subject to more frequent and sub-optimized engineering changes thereby resulting in cost and schedule risks.

**1.6.5 COTS Risk Mitigation Strategy No. 5: Develop and maintain flexible performance requirements suited to the use of COTS products.**

**WHAT/WHY -** COTS products are typically proprietary in nature with little if any user insight into the internal composition of those products. Since product development is based on commercial market needs and is under the manufacturer’s control, requirements must be written at the product/system interface level with a focus on performance or functional characteristics (i.e., what should the product/system be capable of doing as opposed to how the product/system should do it). The functional characteristics should be quantifiable and testable. They should also be prioritized so as to distinguish between absolute requirements (must have) and less absolute (nice to have) requirements so as to provide flexibility when selecting among a variety of COTS product candidates. 

     This flexibility is especially important with COTS products since they are sold and supported by manufacturers in an “as is” state which may not meet all the requirements as stated. It must be understood that if a COTS product modification is needed to meet a requirement that this would typically void any warranty and a unique product may be created that requires uniquely developed (and often more costly) lifecycle support (refer to paragraph 1.4.13).   

     A maintenance concept must also be included in the specification. If it is not compatible with a manufacturer’s support approach, the maintenance concept must be traded off against other factors (e.g., cost, existing business practices, user disruption, schedule, etc.) and once selected, should be adhered to throughout the program’s lifecycle to avoid added costs.

     Instituting this mitigation strategy throughout the lifecycle of a system allows the acquiring activity to:                                                                                       

Prioritize the requirements to maximize COTS product selection flexibility;                                                                                                                                                                   

Specify the desired commercial open system standards and determine COTS          product compliance; and                                                            

Identify COTS product information security susceptibility characteristics.

     This mitigation strategy addresses COTS risk factors 7, 8 and 10. 

**WHEN –** Early during the Investment Analysis phase, high-level mission needs are functionally analyzed to derive more granular requirements and to ultimately develop the system specification for use in a procurement request. The specification continues to be updated in a manner incorporating this strategy to reflect system engineering changes both during development as well as throughout the system lifecycle. 

**HOW -** Technical considerations that are unique to COTS products (e.g., commercial standards, inter-operability, modularity, etc.) also need to be addressed within the functional/performance specification and are addressed in  HYPERLINK  \l "AppendixE" Appendix E (COTS Technical Performance Factors). Incorporating COTS-unique technical requirements into the overall functional/performance specification can help to maximize the number of commercially available solutions. 

     Requirements should also be developed with a quantifiable range of acceptable performance limits (e.g., high and low values) to allow for the integrator to make the best possible match (within constraints) between COTS product capabilities, the requirements and the COTS non-technical selection factors (refer to  HYPERLINK  \l "AppendixF" Appendix F).

     Performance requirements development guidelines are documented in the AMS FAST under *Toolsets/Procurement Toolbox* and are also contained in the FAA System Engineering Manual under Requirements Management. 

     If this strategy is ignored the risk of selecting less capable COTS products increases thereby impacting program performance objectives.

**1.6.6  COTS Risk Mitigation Strategy No. 6: Institute and maintain ongoing COTS product testing capability.**

**WHAT/WHY -** COTS products change rapidly and have undisclosed designs, and so manufacturer claims about the capabilities of their products need to be verified (“Trust but verify.” – Ronald Reagan). COTS products being considered for ongoing system technology refreshment purposes also need to be tested within a system context to ensure that the manufacturer claimed functionality is verified. Therefore facilities for a variety of continuous developmental and sustainment testing activities (a spiral-like evolutionary process) are required when acquiring and supporting COTS-based systems. 

     Full system-level testing must be performed in a test facility that provides or emulates the external interfaces and actual operating environment in which the COTS-based system will be introduced. This raises the probability that the COTS products perform as they did in the development environment and that they do not introduce any unknown performance characteristics into interfacing systems. Once a COTS-based system is baselined and fielded the constituent products are immediately and continuously subject to market-driven obsolescence factors in addition to functional enhancements, upgrades, pre-planned product improvements (P3I), etc. As engineering changes are introduced into the continuously evolving COTS-based system, a dedicated testing environment must be maintained to replicate integration testing steps to determine new product and integrated change package performance and to support a robust configuration management process throughout the system’s lifecycle. 

     Instituting this mitigation strategy throughout the lifecycle of a system allows the acquiring activity to assess:                                                                                                            

Compliance with performance requirements;                                                               

Conformance with the specified commercial standards (e.g., open system               standards); 

Compatibility/interchangeability of candidate replacement products from different manufacturers to minimize single source dependence and to determine suitable technology refresh products; 

Ensure all system configurations (more are possible with COTS product use) can be recreated; and

Determine if new manufacturer changes to a COTS product configuration cause any unforeseen impacts (i.e., “unknown-unknowns” to system performance).

     This mitigation strategy addresses COTS risk factors 1-5, 7, 8 and 10.

                                                                                                                                      

**HOW –** Test facilities that need to be developed must be identified as part of the program’s Work Breakdown Structure (WBS) and budget to ensure the funding is in place for equipment, facilities and personnel. There are several methods for establishing an ongoing COTS product test capability including:

Using or expanding existing test capability;

Developing a new test facility; and

Augmenting the above with a dedicated development facility.

     Once the test capability has been established (or existing capability identified) for the above purposes, test facilities can be organically operated and maintained; contractor operated and maintained; or a combination of the two. 

     Given the lack of technical information about a COTS product (i.e., “black box”) and the variety of product types, the testing of COTS product functionality is somewhat different. System performance remains the key verification parameter for testing however individual products will have different levels of testing due to complexity and criticality. For example a disk drive will not need to be tested to the same degree as a server. 

     **WHEN –** In the early phases of a new system acquisition, the program must ensure that systems representing the current NAS architecture are available for prototyping, beta-testing and early operational concept demonstrations. This capability can also be used to assist in down-selecting proposed design alternatives. Developmental facilities are needed later during solution implementation for beta testing and prototyping of new products as well as for integration testing of COTS product inter-operability and specification compliance. After system deployment, the test facilities continue to assess COTS product alternatives for technology refresh and ensure that COTS-based engineering changes are not inserting any “unknown” product characteristics that negatively impact system performance.  

     If this strategy is ignored the program will be unable to correctly characterize COTS product performance and verify manufacturer claims. The program will also be unable to have risk mitigations in place to avoid obsolescence impacts and will be ineffective at supporting multiple system configurations.

**1.6.7  COTS Risk Mitigation Strategy No. 7: Develop and maintain non-technical COTS selection factors.**

     **WHAT/WHY -** In addition to the functional requirements contained in a functional/performance specification, there are other factors that need to be considered when assessing the viability of COTS products under consideration. Characteristics such as product maturity, manufacturer history/stability, market share, upward/downward compatibility, manufacturer flexibility, support history, etc. need to be weighted as to their relative importance to and influence on performance requirements. It is this strategy that allows for the acquiring agency to become a “smart consumer”. These factors can influence the choice of one product over another along with performance and cost considerations. Instituting this mitigation strategy throughout the lifecycle of a system allows the acquiring activity to:                                                                                                             

Select products that exhibit stable change rates; 

Avoid selecting “trailing edge” technologies and products;                                                                                                                            

Identify to what extent a manufacturer’s product is proprietary;                                                                                                          

Reduce lifecycle costs by ensuring products are selected to optimize          supportability characteristics to the extent permitted by other factors;                                                    

Determine and plan around product type market;                                                                                                          

Identify those product manufacturers who will apprise the user/integrator of internal product changes;                                                      

Select a manufacturer who has a proven history of stability, good quality assurance   practices, customer satisfaction, upward/downward compatibility, etc.;                                                                                                          

Select products that *most closely* meet overall specified requirements to the          extent permitted by other factors;                                                                                              

Analyze the degree to which a product meets the specified commercial          standards and what “extra” features may be offered outside the core          requirements of those standards;                                                             

Compare the support that various manufacturers provide for their products and identify the support that provides for the most stability and predictability; and                                                                                                                             

Assess the degree to which a product provides information security features and          how a system’s architecture can be designed to provide information security.

     This mitigation strategy addresses COTS risk factors 1 and 3-10.

**WHEN –** During Investment Analysis, as requirements are being developed and matured into a system specification, COTS selection factors should be developed for inclusion as part of the request for proposal and the contract requirements. This set of criteria can be used to assess an integrator’s proposed architecture and approach. It can be used after contract award to continue selecting new or replacement COTS products and after deployment to select products associated with technology refresh and engineering changes throughout the system’s lifecycle.

**HOW -** The vendor and product characteristics that need to be considered when comparing products for a particular application are listed in  HYPERLINK  \l "AppendixF" Appendix F (COTS Non-Technical Selection Factors). These factors should be weighted for their importance along with performance and cost factors so that an overall score of multiple characteristics can be used as a product discriminator.

     If this strategy is ignored the likelihood of selecting COTS products with undesirable characteristics increases. Although selected products might meet the performance requirements, if the non-technical factors are not also considered they can impact system cost and schedule. 

**1.6.8  COTS Risk Mitigation Strategy No. 8: Use COTS-sensitive analytical and budget  processes.**

     **WHAT/WHY -** Throughout the lifecycle of a COTS-based system, a series of analyses including risk analysis, trade studies, cost-benefit analysis, lifecycle cost modeling and obsolescence analyses are performed to support the decision-making and budget processes. Additional factors must be incorporated into these analyses to effectively capture the risks that are unique to COTS. Doing this will allow the acquiring activity to:

Support informed management decision-making by more accurately reflecting          overall COTS characteristics;                     

Develop and maintain program COTS acquisition and support strategies, decisions, assumptions and cost estimates; 

Ensure that a continuous system evolution approach is adopted;

Project and prioritize product obsolescence issues;

Identify and mitigate risk factors inherent in the use of COTS products; and

Reduce the potential for disruption of system performance and lifecycle budgets 

      by unexpected product obsolescence.

     This mitigation strategy addresses COTS risk factors 1-10.

**WHEN –** Analysis activities begin with Mission Analysis with the determination of a program need. If a fielded COTS-based system is being considered for upgrade or replacement to meet the need, the ongoing market research for COTS product obsolescence provides a basis for what changes might be needed to meet the new need.

     As alternatives are developed during Investment Analysis, COTS product obsolescence management and risk mitigation strategies are identified in the ISPD and system design proposals allow for more granular budget estimates using product-level information. During development activities, many analyses continue to occur around design/product choices, supportability issues and lifecycle cost estimation. After system deployment supportability analyses continue through market research activities, technology refresh actions and engineering changes are being analyzed and tested for system impact. 

**HOW -** There are several means by which analyses can more accurately reflect COTS-based system characteristics and support budget planning. Because there are few available tools at this point that can reflect COTS characteristics, it is incumbent on acquiring activities to adapt their own tools and processes to incorporate the characteristics. For instance risk analyses must be tailored to take into account such factors as market conditions, technology longevity and supportability, manufacturer market share and stability, the optimum technology refresh cycle, numbers of system configurations, the mitigation strategies that are implemented etc. 

     Cost-benefit analyses and trade studies must be tailored to reflect quantifiable tradeoffs among the decision variables and risk parameters. One approach is to assign weights to the COTS non-technical selection criteria (see  HYPERLINK  \l "AppendixF" Appendix F – COTS Non-Technical Selection Factors). This allows a program office (and in later phases the systems integrator) to make decisions about combinations of COTS product and system features that most closely satisfy requirements in a cost-effective manner. Cost-benefit comparisons among design/product alternatives can also be coupled with cost modeling efforts e.g., Constructive COTS (COCOTS) Integration Cost Model (refer to  HYPERLINK "http://sunset.usc.edu/COCOTS/cocots.html" http://sunset.usc.edu/COCOTS/cocots.html) to make it more likely that a near-term low-cost benefit doesn’t translate into a long-term support cost liability. 

     Obsolescence analyses, based on market investigation activities are continuously performed to refine earlier budget estimates and to identify emergent or unplanned COTS product support changes due to changing business or market conditions e.g., bankruptcies, mergers, product line changes etc. 

     In a manner similar to adapting the analytical processes, the budgeting process must also reflect the unique aspects of acquiring and supporting COTS products. Using COTS-experienced cost estimators and system engineers, early cost estimates can be derived from the selected obsolescence management strategy and the economic service life values contained in *Toolsets/Investment Analysis/Special Topics/Economic Service Life* at  HYPERLINK "http://fast.faa.gov/" http://fast.faa.gov. Every COTS-based system will have a different composition of products, technologies and constraints (e.g., change tolerance). Initial estimates are rough in magnitude to reflect an overall strategy and are refined as market investigation activities are initiated. 

     Using the program WBS (refer to  HYPERLINK  \l "AppendixC" Appendix C, COTS Risk Mitigation Strategies and the Work Breakdown Structure) as a starting point, budgets must include funding for such COTS-related risk mitigation activities as (1) the establishment and maintenance of a permanent test bed(s) to perform conformance, compliance and compatibility testing, OCDs, prototyping and beta-testing; (2) the rigorous application of configuration management procedures to document and manage frequently-changing system baselines; (3) the continuous systems engineering activities including market research, analysis of obsolescence projections, and determination of alternatives to avoid obsolescence situations and integrate the resulting information with new requirements and field data; and (4) the support of more frequent engineering changes to the system. Once identified, budgets must provide funding in a timely manner in order to avoid any impacts on system operations (refer to section  HYPERLINK  \l "AppendixD" D.5). 

     After a system is fielded and market investigation information is analyzed, COTS product obsolescence support options such as end-of-life buys, extended warranties, license extensions, technology refreshment, third party maintenance or data rights purchase must be decided on and planned for as part of each yearly budget cycle. 

     If this strategy is ignored, the program management will be unable to make informed decisions at any level thereby impacting program cost, schedule and performance. 

**1.6.9  COTS Risk Mitigation Strategy No. 9: Integrate COTS-based technology evolution planning data within the Implementation Strategy and Planning Document (ISPD)**

     **WHAT/WHY -** The ISPD is a document that addresses overall strategic planning, program decisions/changes and to project how the program is expected to evolve. It is the tool by which the acquiring activity ensures that it has instituted the necessary planning/processes to most effectively manage the expected and unexpected changes associated with dynamic market-driven COTS-based systems. The inclusion of COTS-specific technology evolution planning information with the results of engineering analyses, management decisions, budget impacts, organizational constraints, policy changes, new user requirements, external interface changes, EOL analyses, integrated change planning, etc. are documented against the existing baseline to form the basis for revising/updating program planning documents, briefs and budget calls and to serve as a central repository of project information. This mitigation strategy addresses COTS risk factors 1-10. 

  

     **WHEN –** The ISPD is developed and baselined during Investment Analysis. As the program is implemented during development and deployment and changes (budget-driven, requirements changes, engineering changes, programmatic, etc.) to the program or system occur, the ISPD is updated to serve as the corporate knowledge base and provides continuity among system participants.

     **HOW -** The ISPD is structured to incorporate technology evolution planning data with the other program information. (Refer to  HYPERLINK  \l "AppendixB" Appendix B, Understanding COTS Obsolescence And Technology Evolution Planning.) The ISPD template can be found in the AMS FAST under *Required Planning Documents* at  HYPERLINK "http://fast.faa.gov/" http://fast.faa.gov.

     If this strategy is ignored the program will not have a baseline strategy to implement its COTS risk mitigation activities and will lose the ability to proactively integrate and prioritize obsolescence-induced situations into the overall program planning. This can affect system performance, cost and schedule.

    

**1.6.10 COTS Risk Mitigation Strategy No. 10: Emphasize strong and COTS-relevant configuration management practices.**

     **WHAT/WHY -** The rapid evolution and proprietary nature of COTS products/systems require a robust and diligent configuration management (CM) program. Although CM practices remain the same for COTS-based systems as for custom systems (CM planning, configuration item selection, change management, auditing and status accounting), there are two very significant differences. First, unlike custom developed systems, the government has no control over the speed and content of product configuration changes since the COTS product manufacturers control them. Second, COTS products are proprietary to the manufacturer and get documented at a higher level (e.g., source control drawings, specification sheets, inputs/outputs, etc.) resulting in limited information on manufacturing processes, internal design, components, etc. Included with this higher level of documentation are different numbering conventions by the manufacturers. These differences shift CM focus from controlling configurations (as with custom development programs) to managing COTS product and system configurations (at the manufacturer-controlled product level). This mitigation strategy allows the acquiring activity to:

Improve the likelihood that the rapid and asynchronous changes associated with COTS products will not affect system performance; 

Better characterize system configuration differences for testing purposes; and                                                                                                                         

Plan for the use of higher-level manufacturer documentation for testing, training and technical manual support.

     This mitigation strategy addresses COTS risk factors 1, 2, 4 and 5.

     

**WHEN –** Configuration management begins during Investment Analysis as program documents such as the ISPD, Acquisition Program Baseline, contract, and specification are developed and finalized. During system development, CM activities expand beyond the documentation level to include system hardware and software baselines to support test and integration activities as well as system acceptance. After deployment CM continues to document delivered system configurations and any engineering changes that occur throughout the lifecycle of the system.  

**HOW -** In rapidly evolving COTS-based systems, engineering changes can become more frequent. Planning for COTS-based systems should include the possibility that functionally equivalent products will be at different revision levels due to non-FAA controlled manufacturer change activity and typically lengthy deployment schedules. Contract requirements to have the integrator ask for and assess product differences can help to minimize impacts of unknown COTS product changes. 

     Proper documentation of the system configurations becomes more critical to the test community to ensure that continuously changing COTS products do not introduce unknown characteristics that affect system performance. Contractual requirements must recognize the higher level of documentation and should be managed at the lowest possible level consistent with the maintenance philosophy. CM considerations for COTS products must also include a cost-benefit trade off between using a product serial number control system against a system that requires the re-identification (i.e., different numbering scheme) of those products.  Serial number control allows for a direct link back to the manufacturer and production lot differences. This strategy is closely linked to maintaining an on-going COTS products test capability. Because manufacturers control their product configurations and capabilities, it is especially important to ensure that new COTS products do not get introduced into a system without the appropriate level of compatibility testing in a properly configured test bed.   

     If this mitigation strategy is ignored the program will be subject to the introduction of “unknown” COTS product characteristics and the inability to effectively manage multiple configurations. This can impact system performance. 

**1.6.11  COTS Risk Mitigation Strategy No. 11: Use a COTS-experienced systems**

**integration agent.**

     **WHAT/WHY -** During a COTS-based system development, initial engineering emphasis is placed on test and integration activities because the COTS products are bought and used in an “as is” state. To ensure that the complexities of integrating COTS products are understood and effectively engineered, it is best to select a COTS-experienced systems integration agent. Although COTS products are developed to commercial standards, there are manufacturer-driven, technology-driven and market-driven differences that preclude a simple “plug and play” integration approach. Additional complexity is added due to external system interfaces that may not be compatible. Program risk is reduced with this strategy because experienced integrator management and engineering personnel use proven COTS-oriented processes to select and integrate COTS products and provide obsolescence management support. This mitigation strategy addresses COTS risk factors 1-10.

**WHEN –** Contract requirements for a systems integrator are developed in the later stages of Investment Analysis. It is at this point where source selection criteria and risk analyses are needed to compare the approaches offered by candidate system integration agents and determine which has the greater chance of mitigating COTS risks. The contract is awarded early during the Solution Implementation phase and should contain COTS-specific contract statement of work (SOW), contract deliverable requirements list (CDRL) and data item description (DID) requirements. After deployment, the system integrator is typically involved in system support activities including market research, spares support and engineering change development.  

     **HOW -** When considering a candidate systems integrator, certain COTS management risk factors need to be formally evaluated. Examples include:

Overall experience and success in the integration, deployment and lifecycle                  support of COTS-based systems;

Expertise in market research (surveillance and investigation);

Technology evolution planning capabilities;

No vested interest in any one particular manufacturer or COTS product set; 

A wide manufacturer network base with good working relations; 

A demonstrated ability to negotiate best value product purchases, warranty, licensing and support agreements and provide credible estimates;                     

COTS-knowledgeable systems engineering, test, integration, deployment and                  lifecycle support personnel;                                  

An aversion to modifying COTS products;                                                                     

The ability to incorporate non-technical COTS selection criteria into the trade                  off and design process; and

The use of lifecycle modeling tools to make design trade off decisions, which consider long-term system supportability consequences. 

     Using the above evaluation elements will provide an indication of the candidate systems integrator’s ability to understand and execute COTS-oriented contract requirements for both products and services. These contract requirements reflect the application of many of the COTS mitigation strategies and include:

Establishing an ongoing market research effort that includes market surveillance (technologies, trends, available manufacturers and products, etc.) and market investigation (product testing and obsolescence projections);

Developing/delivering periodic (e.g., every four months) system product             obsolescence projections, impacts and solutions;

Developing/delivering integrated technology evolution planning data, conducting working group meetings and providing status at program reviews;

Establishing a test facility capable of continuously testing COTS products for compatibility, compliance and conformance;

Ensuring provisions for early user involvement within the systems engineering and development process;

Requiring that notification of proposed COTS modifications be made only with trade-off considered and Government consent;

Refining COTS non-technical selection factors and COTS technical performance factors and incorporating them into the design analysis process;

Using COTS-adapted lifecycle modeling tools to identify long-term impacts of product selection decisions on total ownership costs;

Incorporating cost-saving sharing incentives into the contract to optimize design and supportability decisions based on total ownership costs; and

Making provisions for ongoing contractor maintenance and logistics support. 

**1.6.12 COTS Risk Mitigation Strategy No. 12: Leverage the commercial infrastructure wherever feasible.**

     **WHAT/WHY -** One aspect of using COTS products is that there typically exists a manufacturer-supplied support infrastructure for those products that includes internal       (technical, repair and parts support) and external commercial processes (transportation, communications, etc.) to facilitate that support. When elements of this infrastructure are adopted by the procuring agency and end-users, cost benefits and risk reductions may be realized by not having to replicate a separate support system. For instance, an experienced COTS-based system integrator can provide a centralized repair, replace and technical support function that takes advantage of the individual manufacturer relationships it has established. Cost-benefit-risk analyses are needed to determine the comparative overall values of support alternatives and how well they can meet support requirements. This mitigation strategy addresses COTS risk factors 4 and 9.     

    

     **WHEN –** Leveraging the commercial infrastructure can begin as early as Mission Analysis and Investment Analysis with prototyping and beta-testing activities as well as early operational concept demonstrations (OCDs). This strategy can carry into the maintenance concept and contract requirements development activities for implementation during Solution Implementation and after deployment when the system is in-service. Trade studies must be conducted in accordance with OMB Circular A-76 to determine the benefits of outsourcing work that is inherently non-governmental.

**HOW -** The methods by which existing commercial infrastructure activities can be leveraged include:

Having manufacturers demonstrate their products prior to a purchase commitment                  ( i.e., being a “smart consumer”);

Negotiating quantity discounts and warranty/support/licensing provisions up                  front;

Leasing the equipment;

Requiring deliverables in contractor format;

Performing market research activities;

Using manufacturer and/or third party repair and technical support capabilities;          

Using the internet and overnight shipping as transaction mediums; 

Using manufacturer-developed training and documentation packages; and

Promoting close manufacturer working relations to gain insight into product changes and technology trends.

     If this strategy is ignored, the program can incur additional costs for duplicating services already available in the commercial market.

**1.6.13  COTS Risk Mitigation Strategy No. 13: Avoid the modification of COTS**

**products when possible.**

     **WHAT/WHY -** Modification of COTS products can involve the addition or deletion of code, changes to the hardware design, or changes to any of the product support (i.e., documentation, spares, etc.). Modification of COTS products should only be considered as a last resort since it can involve lifecycle costs that often exceed those of using unmodified COTS products. Savings in development costs and schedules can be offset by the modification of COTS products and can result in a unique version of the product that the manufacturer will not support under warranty and which must be supported separately from other versions, often with increased support costs. A cost-benefit analysis should be undertaken to determine what the consequences of COTS product modification are and to determine the lifecycle costs associated with supporting a unique product. This mitigation strategy addresses COTS risk factors 3 and 7.

     **WHEN -** Decisions to avoid the modification of COTS products are made throughout the system lifecycle starting with the requirements definition process when initial market research is conducted to identify COTS-based technological opportunities. Such a decision can be an influence on the development and prioritization of initial requirements, which can be developed with a level of flexibility that allows for the consideration of available COTS products, thereby precluding the possibility of having to consider the need for modifications. There will be situations where a unique interface requirement or peculiar need will force a modification to a COTS product or a custom development solution.

     This effort is continued during the alternatives analysis process with the evaluation of technological opportunities and the finalization of requirements to allow consideration of available COTS products. Trade off analyses can then be performed to identify, evaluate and select COTS-based alternative/candidate solutions that use available COTS products or those that require modifications due to unique or high priority requirements. After fielding a system, projected changes to existing COTS products and the introduction of new products are continually evaluated to determine if the modification of a COTS product is a viable option.

     **HOW –** Available methods to avoid unnecessarily modifying COTS products include: 

Establishing prioritized requirements for more flexible product selection;

Persuading the manufacturer to incorporate the acquiring activities unique requirements as part of the commercial product’s functionality;

Documenting this strategy in acquisition documentation;

Incorporate into the source selection criteria and procurement documentation;

Instituting a lifecycle model that can support the cost/benefit analysis of modifying COTS products;

Ruggedizing the COTS product within an external shell or casing; and

Establishing a contract requirement to notify the acquiring activity prior to modifying any COTS product.

     If this strategy is ignored the program runs the risk of incurring additional support costs and supportability issues.

**1.7 COTS Risk Mitigation for Fielded Systems**

     For systems that are already fielded, it is still possible to retroactively apply and gain the benefits from many of the risk mitigation strategies discussed in the previous section. The activities that can be applied to fielded systems are identified in Table 1-3.

**Table 1-3. COTS Risk Mitigation Strategies for Fielded Systems**

     Retroactively applying COTS risk mitigation strategies to fielded systems can still yield major obsolescence management benefits. The rationale for being able to apply these strategies is as follows:

Strategy #1 - It is never too late to find or hire “COTS-smart” people to support your

                      program and help apply the risk mitigation strategies.

Strategy #2 - Although it is too late to get the full benefit from early user

                      involvement, in the case of ongoing COTS upgrades to the system,

                      some benefits from soliciting user perspectives can still be realized.

Strategy #3 - It is never too late to institute market research activities to understand

                      which phases of obsolescence COTS products are in.

Strategy #4 - It is never too late to integrate market research information with field

                      data and new requirements.

Strategy #5 - Although it is too late to change the baseline specification for a fielded

                      system, in the case of ongoing COTS upgrades to the system, some benefits

                      from flexible performance requirements can still be realized.

Strategy #6 - It is never too late to establish a COTS product test capability.

Strategy #7 - Although it is too late to apply COTS selection factors to a fielded

                      system, in the case of ongoing COTS upgrades to the system, some benefits

                      from establishing COTS selection factors can still be realized.

Strategy #8 - It is never too late to use COTS-sensitive analytical and budget processes.

Strategy #9 - It is never too late to integrate technology evolution planning

                      information with the overall integrated program planning.

Strategy #10 - It is never too late to emphasize strong and COTS-relevant

                        configuration management practices.

Strategy #11 – If a program undergoes a re-competition, some benefits can be realized by      

                        selecting a COTS-experienced system integration agent.

Strategy #12 – If  a cost/benefit analysis shows an economic advantage to shifting the     

                        existing support concept to one that leverages the commercial  

                        infrastructure, some benefit can be realized.

Strategy #13 - Although it is probably too late to avoid the modification of COTS, in

                        the case of ongoing COTS upgrades to the system, some benefits from not

                        modifying COTS can still be realized.

     All of the risk mitigation strategies can be implemented on already fielded COTS-based systems to achieve benefits for the remainder of the system lifecycle. If all of the strategies cannot be implemented due to cost constraints or other programmatic limitations, it is very highly recommended that at a minimum, risk mitigation strategy number 3, Perform Continuous COTS Product Market Research, be implemented. This risk mitigation activity will yield immediate cost benefits to the program due to the establishment of an obsolescence planning horizon to project and provide budget defense rationale for product obsolescence situations. 

**1.8  Summary**

     The information contained in this COTS risk mitigation guide is to be incorporated as part of the overall risk management program for both existing and new start COTS-based system acquisitions. Since COTS-based solutions are a relatively new AMS policy preference, this guide has been developed for the acquisition, system engineering and support communities to address the need to:

Acknowledge the infusion of COTS products into the NAS;

Understand the unique risks of COTS product use and their impact to existing business practices;

Identify flexible risk mitigation strategies and practical obsolescence management techniques; and

Ensure the inclusion of COTS-specific technology evolution planning information within the integrated program planning process.

     Such a risk mitigation approach allows the acquiring activity to benefit from commonly experienced government and industry lessons-learned in order to move towards market-oriented business practices which are better suited to the acquisition and lifecycle support of COTS-based systems.

                                            **Appendix A**

**References**

**A.1  Introduction**

The references used in the development of this document are as follows:  

Program Manager’s Guide to COTS/NDI: A Software Engineering Perspective, 

(SEPG), 5 Jun 1996

Acquisition Management Guide for COTS/NDI: A Software Engineering Perspective (AIT-5), 25 Mar 1997

Buying Commercial & Non-Developmental Items: A Handbook (OSD) SD-2, Apr 1996

Open Systems Acquisition & Supportability Guide (SPAWAR PMW 133-4), 31 Dec 1996

AUA Technology Refresh Planning Guide, 5 Jan 1998

COTS/NDI Workshop Presentation (ACT/AIT/SEI SERC), 19 Jan 1998

Team Submarine COTS Acquisition Primer, 6 Aug 1997

Lockheed Martin Task Order 40, DSR Technology Refresh Study, 30 Apr 1998

Lockheed Martin Contractor Depot Logistics Support Technical Proposal, 20 Jul 2000

Engineering Off-The-Shelf Solutions, A Lifecycle View (LMDS), Sep 1995

Technology Refresh of NAS Equipment Rev. 9 (AMS FAST), 20 Nov 1998

Air Force Handbook 60-113 (Draft) “Buying Commercial Off-The-Shelf”, 21 Oct 1998

Standard Terminal Automation Replacement System (STARS) Commercial Item/CAS Management Plan, 8 May 1998 

Constructive COTS (COCOTS) software cost model information  HYPERLINK "HTTP://sunset.usc.edu/research/COCOTS/index.html" HTTP://sunset.usc.edu/research/COCOTS/index.html 

A Management Guide to Software Maintenance in COTS-Based Systems (Judith A. Clapp, Audrey E. Taub – MITRE Corp.), Nov 1998  HYPERLINK HTTP://www.mitre.org/resources/centers/sepo/sustainment/manage\_guide\_cots\_base.html HTTP://www.mitre.org/resources/centers/sepo/sustainment/manage\_guide\_cots\_base.html

NAVSEA PMS450 Virginia Class Technology Refreshment Management Plan, 31 Mar 1999

Commercial Advocates Forum, Office of the Under Secretary of Defense 

(Acquisition Reform)  HYPERLINK HTTP://www.cadv.org/CAF\_News.htm HTTP://www.cadv.org/CAF\_News.htm

Eunomia Market Survey Question Responses from industry (bus. sens.), 1 Feb 1999

Effectiveness of COTS Solutions, Study Prepared for Office of Acquisition  

Management, 1 Feb 1999

ACQWeb, Office of the Under Secretary of Defense for Acquisition, Technology and Logistics  HYPERLINK HTTP://www.acq.osd.mil HTTP://www.acq.osd.mil

COTS Lessons Learned, Logistics Information SPO (undated)

Concepts For Economically Supporting Electronic Systems with Dynamic Baselines,  A Study in Supporting Systems Based On Commercial-Off-The-Shelf (COTS) Electronics

The COTS Journal, published bi-monthly by the RTC Group   HYPERLINK "http://www.cotsjournalonline.com/" http://www.cotsjournalonline.com/

CROSSTALK, The Journal of Defense Engineering, by Software Technology 

Support Center  HYPERLINK HTTP://stsc.hill.af.mil/Crosstalk/crostalk.html HTTP://stsc.hill.af.mil/Crosstalk/crostalk.html

Assessing the Risks of Commercial-Off-The-Shelf Applications: Lessons Learned 

from the Information Technology Resources Board, Dec 1999 

       HYPERLINK HTTP://www.itrb.gov HTTP://www.itrb.gov

Off-The-Shelf Software: Practical Evaluation (Lee Fischmnann/Karen McRitchie – Galorath Inc.)  HYPERLINK "http://www.galorath.com/presentations\_sem./html" http://www.galorath.com/presentations\_sem./html 

Architectural Issues, other Lessons Learned in Component-Based Software 

Development (Will Tracz, Ph.D., Lockheed Martin Federal Systems)

 HYPERLINK HTTP://www.owego.com/~tracz HTTP://www.owego.com/~tracz

Ensuring Successful Implementation of Commercial Items in Air Force Systems 

(U.S. Scientific Adv. Brd.), Apr 2000

An Activity Framework for COTS-Based Systems (SEI Obendorf, Brownsword, 

Sledge), Oct 2000  HYPERLINK "http://www.sei.cmu.edu/publications" http://www.sei.cmu.edu/publications

A Study of the Federal Government’s Experiences With Commercial Procurement Practices (Michael Anderson), Jun 1997

COTS and Open Systems: SEI Monographs on the Use of Commercial Software in Government Systems (SEI Oberndorf), Feb 1998  HYPERLINK "http://www.sei.cmu.edu/cbs/papers/monographs/cots-open-systems/cots.open.systems.htm" http://www.sei.cmu.edu/cbs/papers/monographs/cots-open-systems/cots.open.systems.htm 

Commercial Item Acquisition: Considerations and Lessons Learned, Office of the 

Secretary of Defense (OSD), 14 Jul 2000

Common Risks and Risk mitigation Actions for Management of a COTS-Based 

System (Pamela Engert, Judith Clapp – MITRE Corp.)  

       HYPERLINK HTTP://www.mitre.org/pubs/edge\_perspectives/march\_01/risks.html/ HTTP://www.mitre.org/pubs/edge\_perspectives/march\_01/risks.html/

Selecting COTS Products – or Services (John Wilson – MITRE Corp.) 

       HYPERLINK HTTP://www.mitre.org/pubs/edge\_perspectives/march\_01/wilson.html/ HTTP://www.mitre.org/pubs/edge\_perspectives/march\_01/wilson.html/

Electronic Part Obsolescence Driven Product Redesign Optimization (P. Singh and P. 

Sandborn, T. Geiser and D. Lorenson, May 2002

**Appendix B**

**Understanding COTS Obsolescence And Technology Evolution Planning**

**B.1  COTS Hardware Obsolescence**

     One of the more difficult aspects of managing COTS-based systems is rooted in the rapid evolution of COTS products. The fundamental problem is product obsolescence because new versions or releases of COTS products are brought to the market frequently. The level of maintenance support and availability of spare parts for a given version or release of such a product diminishes over time and can become more costly in a correspondingly rapid manner. 

     The first step in the mitigating the risks associated with using COTS products is to use COTS-knowledgeable individuals in all of the analytical processes. This knowledge includes an understanding of the risks and mitigation strategies unique to COTS products and an understanding of COTS product obsolescence stages and how to limit their potential effects on system performance. For example, Figure B-1 (COTS Product Obsolescence Progression) illustrates the stages of obsolescence that COTS hardware products pass through as evolution of the commercial market makes them obsolete. These stages are risk trigger points that should elicit a question such as “What impact if any, does this change of product status have on my system/program?” The definitions of these trigger points are:

                                **Figure B-1.  COTS Product Obsolescence Progression**

*End of life (EOL).* This stage occurs when a product is no longer manufactured by its original equipment manufacturer (OEM). Between this stage change and the end of service (EOS) stage, the OEM is typically willing and able to provide repair/replacement support services until unprofitable or unable to continue doing so.

*End of service (EOS).* This stage occurs when a product is no longer serviced by the OEM. Between this stage change and the end of repair (EOR) stage, third-party sources may be available to provide repair/replacement support services until no longer profitable or unable to do so. If no third-party support is available then the product is at the EOR stage.

*End of repair (EOR).* This stage occurs when hardware product support is no longer available by any means or is cost-prohibitive. This stage change is characterized by system usage/demand depleting the remaining depot spares over time. This begins to create support uncertainty (or risk) for the program related to such factors as remaining spares quantities, item failure rate, etc.

*End of maintenance (EOM).* This stage occurs when a site requisition cannot be replenished. This stage change begins with the depletion of limited depot and site spares quantities, followed by service degradation (i.e., loss of redundancy) and ultimately loss of system operations.

**B.2  COTS Software Obsolescence**

     COTS software supportability characteristics and obsolescence management options differ somewhat from those of COTS hardware. The projected EOS date (i.e., the vendor no longer provides product support) is the primary point in the progression at which to assess impacts and determine options. Although there is some variation, COTS software vendors will typically provide technical support for the previous two generations of software before declaring EOS. The support that is provided by a vendor can take the form of technical support to help integrate the product during development, updates to that product to incorporate fixes and, even after EOS, technical support on a hourly basis might be available.

     Although COTS hardware and software products differ in their obsolescence characteristics, the progressive obsolescence of both product types can affect system sustainment. A fundamental characteristic of COTS software worth noting is that after sufficient test, integration and debugging, it is inherently reliable and can perform its function almost indefinitely as long as the hardware platform remains stable. 

     However, despite the inherent reliability of software over time and a stable hardware platform, the prolonged use of COTS software products beyond EOS must be continuously assessed for there are conditions that occur in a system’s evolution where COTS software obsolescence can drive change as well. Some of the many factors that need to be taken into consideration when continuously analyzing the COTS software products within a system include:

Diminishing software support skills (integrator, third party or in-house) over time;

New COTS software product compatibility with the underlying hardware platform;

The complexity of the COTS software interfaces (e.g. operating system software) with other system COTS software products/applications, middleware, glue code, custom/legacy interfaces;

The ability to modify a system function without unknowingly exceeding a COTS software product tolerance;

Introducing system “unknown unknowns” with untested products (e.g. unused code, timing differences, firmware changes etc.); 

Sole source dependency for critical software components and data rights availability;

Information security;

Licensing options and costs; and

Data rights availability, etc.

 

**B.3  COTS Obsolescence Planning**

     Management of COTS product obsolescence entails the initial use of a system-level strategy and the subsequent use of product level support options. A system-level strategy for obsolescence management must be formulated early in a COTS-based system’s acquisition cycle. It provides a lifecycle system evolution path that integrates such activities as pre-planned product improvements (P3Is) and new requirements changes with projected obsolescence-induced system upgrades. The strategy also provides the basis for system budget projections and risk management. Because of the extent of variability encountered when using COTS products, the system-level strategy must be reviewed periodically and adjusted as needed.

     During early program planning, a notional architecture is used to begin a high level cost estimating process. The architecture needs to be decomposed into product segments such as custom development, COTS and modified COTS. The COTS category can be further decomposed into related product groups such as applications, processors, personal computers, graphics user interface (GUI), mainframes, displays, operating system etc. to begin to characterize the lifecycles of these groups mover time and to estimate technology refresh cycles and costs. Using COTS-experienced cost estimators and system engineers, early cost estimates can be derived from the selected obsolescence management strategy and the economic service life values contained in *Toolsets/Investment Analysis/Special Topics/Economic Service Life* at  HYPERLINK "http://fast.faa.gov/" http://fast.faa.gov.

     As the system architecture is defined and the COTS product composition becomes known, the system-level assumptions and resultant planning can be refined to reflect end-of-life/end-of-service (EOL/EOS) data gathered through market research activities. When EOL/EOS dates are projected by a product’s manufacturer, a determination can then be made on which of several product support options they wish to implement in support of the overall system evolution/obsolescence management strategy using a mixture of such options. Implementing a mix of options over time provides management cost, schedule and risk flexibility to address market-driven COTS variances. The system-level management strategies and product level obsolescence support options are described in the following paragraphs.

**B.4  COTS Obsolescence Management Strategies**

     At the system level, there exists a broad range of strategies for managing COTS obsolescence in order to mitigate the risks. Possible management strategies include:

The continuous refresh of all COTS products to maintain currency of manufacturer support;

Freezing the hardware/software baseline during development and then using product obsolescence support options to sustain the system for a defined period; or

Freezing the hardware/software baseline for a defined period and then refreshing as required. 

     Each obsolescence management strategy exercises a different level of control over market-driven product obsolescence and consequently invokes a different level of program risk as illustrated in Figure B-2 (COTS Obsolescence Management Strategies). 

**Figure B-2.  COTS Obsolescence Management Strategies**

     For example, adopting a continuous refresh strategy is beneficial from a product support standpoint, but it is high risk due to the loss of programmatic control over the impact and cost of frequent successive vendor-driven product refreshes to system evolution. This approach is best suited to systems that can take immediate advantage of emergent technology improvements (e.g., leased systems). 

     Conversely, a strategy of freezing the hardware and software baselines for a defined period (including the spares to support that period) and then refreshing as required affords the advantages of greater programmatic control and less risk from product change impacts. The disadvantage is that this strategy can be overly rigid when dealing with a dynamic marketplace and could result in more expensive upgrades due to new product incompatibilities with the older products. This approach is best suited to systems that will not undergo significant performance enhancements over time.

     While a particular strategy can be applied at the system level to anticipate and avoid COTS obsolescence, there will be unforeseen obsolescence situations that require near term action. Commercial market volatility due to vendors dropping product lines or going out of business, or mergers and sellouts coupled with short EOL/EOS notification periods are typical of what can be encountered in today's marketplace. Therefore, in looking for useful system sustainment and risk management strategies in a COTS environment, program managers must consider flexibility in applying the strategies. That is, the managers must not use strategies that "lock" them into specific directions and prevent them from modifying their plans as the COTS products or the requirements change.

     A third dimension that must be considered is the timing of changes to a system. If a program is proactive in anticipating obsolescence issues, it will have more support options available to deal with the issue. The later in time that an obsolescence issue is addressed, fewer options exist and they can also cost more (e.g., redesign).  

     

     A strategy of freezing the hardware and software baseline during development and then using product obsolescence support options to sustain the system for a defined period is a compromise between the two previous strategies.  It affords the ability for the program to have an overall system evolution plan that: (a) is flexible enough to be responsive to market-driven changes, and (b) limits the extent of “chasing the market” behavior. Although there is little control over product and market changes, the gathering of projected product EOL/EOS data coupled with the application of various product obsolescence support options allows the program to respond to emergent obsolescence situations before they become problems. These options are discussed in greater detail in the following paragraph.

**B.5  COTS Product Obsolescence Support Options**

     Product obsolescence support options can range from single-event activities such as lifetime buys to periodic event activities such as technology refreshment. Figure B-3 (COTS Product Obsolescence Support Options) illustrates the product obsolescence support options relative to the previously described stages of product obsolescence. The figure shows the options that exist for countering the effects of COTS product obsolescence. 

**Figure B-3.  COTS Product Obsolescence****Support Options**

     The impact to a system or program as a result of a COTS product reaching an EOS/EOL stage can range from none to major redesign depending on such factors as vendor notification lead time, failure rate, spares availability, alternate product compatibility, interface interdependencies, new requirements, technology trends, costs, risks, etc. (see COTS  HYPERLINK  \l "Risk2" risk factor #2). 

     These factors, which are all inputs to a systems engineering trade study process, will determine which product obsolescence support options the acquiring activity chooses to support its system evolution strategy. The figure also shows how the passage of time closes the “window of opportunity” for dealing with product obsolescence. Addressing these problems early in the obsolescence cycle provides the greatest degree of flexibility in finding effective solutions, and helps to avoid situations that can potentially impact system operations.

     The gathering and analyzing of product obsolescence data and selecting support options identifies those planning and budgeting requirements essential for sustaining system operations. This data is then used to define potential obsolescence-driven operational impacts to technically justify the funding requirements that sustain existing system operations. Refer to Table B-1 (COTS Product Obsolescence Support Options) for a description of available COTS product obsolescence support options. The analysis of these obsolescence support options is a key input to COTS risk mitigation and specifically to technology evolution planning which is focused on the gathering and analysis of market-driven product (or COTS) data to address COTS product obsolescence. 

**Table B-1.  COTS Product Obsolescence Support Options**

|  |  |
| --- | --- |
| **Option** | **Definition** |
| No action required | When a product’s reliability and/or the availability of replacement assets (i.e., depot spares, OEM, third party) allows for continued product support regardless of obsolescence phase. |
| Lifetime Buy | The acquisition of (e.g., purchase, cannibalization, trade) sufficient replacement products, components or items to meet a projected failure/demand rate until a defined point in time. |
| Extended Maintenance/Warranty | The purchase of technical and/or repair support from the original equipment manufacturer (OEM) that extends the support of a product beyond the original timeframe. |
| Third Party Maintenance | The establishment of technical and/or repair support by a vendor other than the OEM that is qualified to provide that support. |
| Technology Refreshment | “The periodic replacement of COTS products using the same kind of products (e.g., processors, displays, computer O/S, commercially available software) within the larger system to assure continued supportability of the system through an indefinite service life.” (AMS 11/98) Periodicity is based on when the product can no longer be supported. Technology refresh does not change the system performance baseline. |
| Redesign/Integrated Change | When product obsolescence is addressed by a system redesign (e.g., new products, new architecture) or when replacement of obsolete products is integrated into a larger system upgrade or a pre-planned product improvement (i.e., P3I). |
| Purchase Data Rights | An arrangement made by a product user with the OEM to secure the proprietary data rights (i.e., drawings, software, documentation etc.) for a product to assume organic (internal) or third party support for that product. |
| Reclamation/salvage | Also referred to as cannibalization, this is typically a last resort support option whereby pieces of a discarded product are reclaimed and re-assembled to create a functional product. |

**B.6  COTS Risk Mitigation And Technology Evolution Planning Process**

     As illustrated in Figure B-4 (COTS Risk Mitigation/Technology Evolution Planning Process Flow), the process begins with the development of an Implementation Strategy and Planning Document (ISPD) that captures the COTS-based acquisition strategy. The ISPD also captures the program’s system engineering activities and programmatic risk mitigation planning that is then tailored to incorporate the COTS risk mitigation strategies that establish the technology evolution planning foundation. The primary objective of technology evolution planning is to provide budget and decision-making personnel with support alternatives that address product obsolescence issues before they happen. 

**Figure B-4. COTS Risk Mitigation/Technology Evolution Planning Process Flow**

     The technology evolution planning part of this process flow starts with the collection of market research data which can include either high-level market surveillance information on what technologies and products can meet the requirements, or more product-oriented market investigation activities later in the program to determine compliance, conformance and compatibility and to establish product obsolescence profiles. This obsolescence information is then analyzed to determine system impacts and identify viable mitigation actions. At this point in technology evolution planning, the viable mitigation actions are examined for both the engineering and budget lead time requirements to implement the solution prior to the realization of the risk situation. Based on this information, the desired options are chosen, resource requirements are identified for budgeting purposes and then documented in an update to the ISPD. 

     For example, the notional product in the green block in Figure B-4 is anticipated to go into the end of repair (EOR) phase around Year 6, which begins the depletion of any remaining spares stock. If funds are not made available in time to resolve the problem, the product will progress into the end of maintenance (EOM) phase (or imminent system degradation due to lack of spares) late in the Year 7 timeframe. 

     In this example, Year 6 is assumed to be the latest possible target for completing the deployment of the solution to avoid spares depletion. If the engineering/test/deployment lead-time for the chosen solution is about 1.5 years, the needed funds must be placed on contract during Year 4. Allowing for a 2 year budget cycle, the requirements must be identified and budgeted in Year 2. This scenario provides a reasonable margin of time to account for delays or EOM estimation error. If the funding is not made available until the following year, this results in a “just in time” deployment of the solution but with a greater risk of operational impact to the system. If  any further funding delays occur, then the only way to avoid an operational impact is an immediate reprogramming of funds.**Appendix C**

**COTS Risk Mitigation Strategies and the Work Breakdown Structure**

**C.1  Introduction**

When acquiring a new system or upgrading an existing one, inter-related COTS risk mitigation activities begin during mission analysis and continue throughout the system’s lifecycle until such time that the system is replaced or the capability is no longer required. The mitigation strategies applied during one phase provide a foundation for the next set of strategies. The resources needed to implement the COTS risk mitigation strategies are consistent with the FAA Standard Work Breakdown Structure (WBS) (Rev 1.0). Refer to Table C-1 (COTS Risk Mitigation Strategies, AMS and Standard WBS) for a table showing the relationship of the COTS risk mitigation strategies with the AMS phases and applicable WBS tasks.

**Table C-1. COTS Risk Mitigation Strategies, AMS and Standard WBS**

|  |  |  |  |
| --- | --- | --- | --- |
| **Number** | **Risk Mitigation**  **Strategy** | **AMS**  **Phase** | **WBS**  **Para No.** |
| 1      2        3          4      5        6      7        8      9        10      11      12      13 | Involve COTS-knowledgeable individuals in all analytical processes    Involve users early and throughout the program lifecycle to identify and resolve COTS-related issues    Perform continuous COTS product market research (i.e., technology trends, product applicability and obsolescence status)      Integrate market research results with field data and new requirements    Develop and maintain  flexible performance requirements suited to the use of COTS products    Institute and maintain ongoing COTS product testing capability    Develop and maintain non-technical COTS selection factors      Use COTS-sensitive analytical and budget processes     Integrate COTS-based technology evolution planning with overall ISPD     Emphasize strong and COTS-relevant configuration management practices    Use a COTS-experienced systems integration agent    Leverage the commercial infrastructure wherever feasible    Avoid the modification of COTS products when possible | All      All        All          All      All        All      IA, SI, ISM         IA, SI,            ISM    IA, SI, ISM      SI, ISM      SI, ISM      SI,  ISM      IA, SI, ISM | 1.1, 2.1, 3.1, 4.1      1.1, 2.1, 3.1, 4.1        1.2, 2.1, 2.2, 3.2, 3.7        1.1, 1.2, 1.3, 2.1, 2.2, 3.2, 3.7    1.3, 2.1.1, 2.1.2        1.2, 2.1, 2.2      2.2, 3.2, 3.5, 3.7        2.2, 3.1.2, 3.2, 3.5, 3.7, 4.1.2, 5.7.2    2.2, 3.1.1, 4.1.1, 5.7.2      3.2.6, 4.1.3, 5.7      4.1.3, 5.7.1      3.4, 5.11      2.2, 3.2 |

**Appendix D**

**Obsolescence Risk Analysis**

**D.1 Objectives**

     This appendix applies standard programmatic risk management techniques to facilitate COTS product obsolescence risk analysis and to determine appropriate risk mitigation actions to minimize the impact of product obsolescence on system operations.  It incorporates COTS Risk Mitigation courseware material and is structured to illustrate a variety of “real-world” COTS product obsolescence scenarios and the variety of mitigation activities to address them. The objectives of this appendix will allow the reader to:

Learn what market research information is needed and the definition of the      

information elements;

Project end of repair (EOR) and end of maintenance (EOM) dates for COTS products;

Integrate COTS product information into a system obsolescence risk profile;

Analyze and select viable risk mitigation/product obsolescence support options and determine their impact to the system;

Identify product obsolescence risk issues and mitigation actions using programmatic risk management templates; and

Develop and communicate credible budget defense rationale; and

Integrate COTS product information into a system obsolescence risk profile.

     In essence the reader will know what information to ask for, how to identify and analyze product obsolescence risks and how to select and implement risk mitigation options. This process is illustrated in Figure D-1 and is derived from the FAA Programmatic Risk Management section of the FAA System Engineering Manual.

**Figure D-1. Risk Management Process Flow**

     Contained within the FAA Programmatic Risk Management course is an exercise that illustrates that ***risk is in the eye of the beholder***. One person may be willing to bet on rolling a seven with a pair of dice and another will bet against it even though it is the most likely number that will be rolled (odds = 6:36). The same statement applies to the obsolescence risk analysis exercises contained in this appendix; levels of risk will be subject to the interpretation of the available information.

**D.2 Identifying COTS Product Risks**

     When an acquisition program implements COTS risk mitigation strategies, technology evolution planning information is collected, primarily from the market research process. Market research consists of a high-level market surveillance process (technology trends, market conditions, etc.) and a more product focused market investigation process (compatibility testing, obsolescence status etc.). It is the market investigation process that provides the information necessary to establish the forward-look planning horizon needed to effectively manage COTS product obsolescence (see  HYPERLINK  \l "AppendixB" Appendix B – Understanding COTS Obsolescence).

     Once a COTS-based system architecture has been established and the constituent COTS products identified, market investigation activities must be conducted to identify product end of life (EOL) and end of service (EOS) dates from the product suppliers or manufacturers as well as demand and spares information as illustrated in Figure D-2. 

**Figure D-2. Market Research / Product Supportability Information Template**

     Although not the only source, the system integration agent typically provides this information as a contract deliverable (report, study, etc.) due to the already established vendor relationships. This information is collected on a periodic basis (e.g., every four to six months) from each product manufacturer or supplier throughout the lifecycle of the system to determine the impacts of projected COTS product obsolescence status changes and to select the appropriate risk mitigation/product obsolescence support option.

                       **Table D-1. Market Research Information Element Definitions**

     This spreadsheet format can be easily tailored to specific program information requirements and can be updated to reflect new product obsolescence information. A definition of the information elements in the report is provided in Table D-1.

**D.3 Analyzing COTS Product Risks**

     Once market research information is received, risk assessment activities can begin using the obsolescence analysis worksheet shown below in Figure D-3. This worksheet is designed to help develop additional information about the particular COTS product obsolescence situation so it can then be recorded onto the programmatic risk templates.

**Figure D-3. Obsolescence Analysis Worksheet Template**

     After identifying the particular product being analyzed, the analyst is prompted by the sheet to project EOR and EOM dates. Using the product’s demand history and reliability trend as a basis for projecting usage, it is possible to estimate an approximate date for EOR (when repair/replace support is no longer available or too costly and spares stock is depleting) and EOM (when site spares can no longer be replenished).

**D.4 Selecting the Risk Mitigation Options**

     The next step in filling in the obsolescence analysis worksheet is to identify the possible support options for dealing with each COTS product obsolescence case. The options are listed on the worksheet and the analyst(s) must determine whether or not an option is viable based on the information provided. If it is questionable whether an obsolescence support option is viable, a “don’t know” status should be indicated. This status will in turn create an action to determine the answer to the question. The task to answer the question is then given to the system integration agent (or other support resources) and the answer(s) recorded on the worksheet to determine option viability with respect to cost, schedule and technical impacts.

     When all the information has been collected, the most viable support option or combinations of options are selected and written up as a risk mitigation recommendation.      Using the five levels of risk likelihood and risk consequence (provided later as part of the exercise), the FAA programmatic risk sheet (see Figure D-4) is then filled in to determine 

 

**Figure D-4. FAA Risk Worksheet Template**

determine the severity of each risk and to document the recommended actions. This allows the risks to be communicated to others in a standard and easy to understand format.

     Once the worksheet is filled in for a particular risk situation, and the recommended mitigation option (or combination of options) is identified, it is now possible to graphically illustrate the timeliness and effectiveness of the mitigation actions on the risk mitigation waterfall schedule (see Figure D-5). This scheduling activity allows the analyst to phase the funding requirements and also provides a standard format to communicate the risk mitigation recommendations. The chart is also used to support changes to the program plan and the budget to include the risk mitigation efforts.

**Figure D-5. Risk Mitigation Waterfall Schedule Template**

     

     Prior to changing the program plan to reflect these recommendations, the obsolescence-related risk mitigation recommendations must be prioritized against other proposed system changes and analyzed for technical and schedule relationships that could be leveraged (refer to paragraph 1.5.4). One method to accomplish this analysis is illustrated in Figure D-6.

     

**Figure D-6. Risk Mitigation Action Prioritization**

     

     Actions that mitigate obsolescence/supportability risks are typically prioritized as the highest since they are critical to sustaining system operations. The next category of system change is that which makes existing system capabilities more efficient or effective. These improvements are considered sensible to adopt and are typically justified with a return on investment rationale (e.g., converting from an analog to digital switching system to reduce dedicated phone line usage). The last category of system change activities includes P3I and new requirements. These possible enhancements to system capability are categorized as lowest presuming a limited budget situation. In other words it makes more sense to fix a leaky pipe or broken window in your home before you add on a new deck.

     Once the projected system change activities are plotted out in a manner similar to that illustrated in Figure D-6 it is now possible to examine the technical and schedule relationships that might exist. For example, if the system is expected to undergo a pre-planned product improvement (P3I) in the near future the risk analyst would examine the affected components of the system P3I to determine if the upgrade will resolve an existing or projected product supportability issue.

     A technical and schedule relationship might exist between a proposed improvement and a separately projected supportability issue that could be assembled as an integrated change package. Another example of a technical and schedule relationship is if one risk mitigation action is accelerated by a year to be packaged with another risk mitigation action in order to minimize the disruption to system operations with only a single installation activity.

     The last piece of information that is derived from the risk mitigation waterfall chart is the funding profile needed to execute or implement the mitigation actions. This includes the lead-time needed for budgeting, engineering, testing and deploying the solution.

**D.5 Implementing the Risk Mitigation Plan**

     Once a decision to accept the recommended risk mitigation action(s) is made, the next step is to apply funding. If funding must be reprogrammed or if new funds are needed, a technical rationale to justify the risk mitigation action(s) against other system/program priorities is essential to answer the commonly asked question:

***“What will happen if we delay funding this activity?”***

     The rationale to defend the risk mitigation activity is based on market research information and a structured system engineering and risk analysis process. The business case for funding a risk mitigation activity must be expressed in terms of operational 

**Figure D-7. Budget Defense Rationale Template**

impacts. Using a format similar to Figure D-7, the technical rationale and risk description can help to provide a clear picture for the decision-maker of what the consequence of inaction (i.e., assuming the risk) actually means. Examples of operational impacts include:

loss of ground to air /ground to ground communications

loss of back-up capability

degraded operational availability

loss of radar or sector coverage

security

passenger/airline impacts (delays, costs, flight safety etc.)

lack of certification

     Another tool that can be used to communicate the obsolescence status of the COTS products within a system (before mitigation) is illustrated below in Figure D-8. By laying out COTS product EOL, EOS, EOR and EOM information on a timeline, a snapshot view of a system’s health can be had (refer also to Figure D-15).     

**Figure D-8. System Obsolescence Risk Profile Template**

     The above risk templates can be adapted to any particular program by downloading them from the “Tool Kit” link at the FAA COTS Lifecycle Management web site at  HYPERLINK "http://www.faa.gov/aua/resources/cots" http://www.faa.gov/aua/resources/cots.  The COTS risk mitigation methodology described above can now be applied in a practical manner using a sample program scenario.

**D.6 Sample Obsolescence Risk Analysis Scenario**

     The following is a situation summary for a fielded program called the Automated 

Information System (AIS). It will be used as the basis for the following sample scenario 

and the associated product obsolescence risk analysis examples.

You are supporting the Automated Information System (AIS) project. It

is a hybrid system comprised of ***both custom and COTS products*****.** It has

been fielded at 20 sites for about three years and does ***not have any COTS***

***risk mitigation*** strategies in place.

The contractor has recently indicated that one of its COTS product suppliers

just went out of business. Concerned about the other COTS products,

your system engineering group has ***tasked the contractor*** to deliver a

***market research report*** for all the COTS products in the AIS and you have

just received it. The contractor has summarized the ***top six COTS product***

***risks*** that appear to need attention due to near term end of service dates they

have obtained from the product manufacturers and suppliers.

The program’s Integrated Program Plan and budget do not have any

provisions for technology refresh or obsolescence-induced supportability

problems. It indicates that an external system interface change requires an

***upgrade of the Central Computer Complex hardware and operating system***

***software***. It is scheduled for initial key site deployment ***four years from***

***now*** with one year planned for development, test and integration.

     The AIS architecture is illustrated below in Figure D-9 to help visualize the system and its COTS product inter-dependencies. It is a relatively simple information processing and display system that consists of:

**Figure D-9. Automated Information System (AIS) Architecture Diagram**

A dual redundant central computer complex that interfaces with all other AIS sub-systems and an external input/output device;

A display sub-system consisting of six operator display workstations;

Dual redundant high speed printers that print the data stored in the data storage devices;

Dual redundant data storage devices to capture and retrieve historical system; and

Dual redundant remote maintenance workstations and local printers to support system maintenance and certification activities.

**D.6.1 Identifying the Risks**

     We begin the obsolescence risk analysis exercise by assuming that the system integrator has just delivered a supportability analysis based on market research information we tasked under contract. The contractor was provided the obsolescence report element definitions ( HYPERLINK  \l "D2" Table D-1) to ensure a common understanding of the information. The information for one of the six products that were identified as obsolescence risks is provided below in Figure D-10 and will be used for this sample exercise.   

**Figure D-10. AIS Operator Display Monitor (ODM) Market Research Information**

    

     This first look at the raw market research information provides an overall understanding of the nature of the risks associated when a COTS product goes end of life/end of service. 

     

The information reads as follows:

     - This ODM is a COTS product made by Suny Inc. This “item type” block could also 

        indicate a modified or custom part if included in the tasking.

     - There is one ODM per workstation or six in each system.

     - Unknown to the system integrator, Suny stopped producing this monitor two years 

        ago thereby establishing the end of life date.

     - Suny will only be supporting the ODM (in this case warranty and technical support 

        only since the notes indicate it is a non-repairable unit) for another six months which 

        establishes the end of service date.

     - The ODM fails at an average rate of six per year but over the past year that rate has 

        increased to 10 failures indicating an upward or accelerating failure trend by 66%.

     - There are 20 ODM depot spares and two spares located at each  of the 20 sites.

     - The manufacturer’s next generation monitor is not form, fit and function (F3) 

        compatible.

     - There are no other manufacturers or suppliers capable of providing a full F3 

        compatible substitute product but there are somewhat compatible or F2 sources 

        available.

     - The system integrator has estimated that the time to test the substitute product(s) will     

        be 4 months. 

     - Production lead time or the time needed to procure, develop, test and initially deploy 

       a replacement ODM will be one year.

     - The impact of an ODM failure takes the entire workstation down but the workstation 

        functions can be off-loaded to other workstations with the system only able to 

        handle one workstation failure at a time before losing sector coverage.

     - The notes tell us that this is a sealed unit and therefore non-repairable and that the 

        manufacturer’s next generation product is 21” rather than the current 20” thereby 

        affecting the system’s rack fit factor of form, fit and function.

     - The notes also tell us that the ODM manufacturer is a sole source supplier which can 

        often limit the solutions that are available to a program when choosing a product.

**D.6.2 Analyzing the Risks**

     Understanding this raw information and developing solutions to mitigate the risk begins with filling in the obsolescence analysis worksheet as illustrated below in Figure D-11. 

     The first action is to calculate the end of repair date (when support is no longer available). Since the manufacturer is the only supplier of the ODM we assume for now that when they stop supporting the technical and warranty replacement support for their product that EOR is the same date as end of service.

      

**Figure D-11. Sample Obsolescence Analysis Answers for the ODM**

     The end of maintenance date is calculated next by simply dividing the number of depot spare assets on hand by the most recent yearly usage rate and then adding the number of months to EOS. Close examination of the reliability information is important to ensure failures have not been induced by other than “normal” usage factors. This avoids skewing the analysis results. If the most recent yearly usage rate is suspect then the average failure rate should be used. In the case of the ODM, 20 spares are divided by a demand of 10 per year equals 24 months. Adding the six months until EOS makes for a total of 30 months from the present.

     As we examine the support options that are available to us, we know that we’re going to run out of the ODMs soon so the “no action required” option isn’t viable. Although we suspect that Suny Inc. is the only source for this product the information obtained from the integrator doesn’t tell us whether or not there might be other sources for a “lifetime buy” of the ODM so a “don’t know” status is indicated on the worksheet. The “extended maintenance/warranty” and “third party maintenance” options are not viable either since the ODM is not a repairable item and the manufacturer has declared EOS.

     The “tech refresh” option is a possibility but since there are no fully compatible substitute products a “don’t know” status exists about what other 20” display products might be available and how different their form, fit or function might be.

     The redesign/integrated change” is also a possibility for the same reason as tech refresh. Since the AIS situation summary has given no information about any planned changes to the workstation, it is assumed that integrating the ODM replacement as part of a larger engineering change isn’t possible.

     The last option of “purchase data rights” doesn’t work in this case unless the program is willing to assume the start-up costs to establish and maintain a production line for a unique product. The cost is considered in this case to be prohibitive.

     As a result of the “don’t know” status to some of the solution options, there now exists a basis for going back and tasking the system integrator to answer more specific questions. The first task to the integrator then is to determine if the manufacturer or any other supplier have extra ODMs for sale to be able to push back the EOM date to either meet the projected service life of the system or to “buy time” to engineer another solution.

     The next “don’t know” status results in a task to the integrator to go and find out what available F2 compatible products on the market most closely meet the requirements. In some cases this could require buying and testing the product to verify contractor claims or to determine the extent of the impact to the system should a redesign be needed.

     The integrator comes back with some answers to these two tasks. There are only 10 more ODMs available for purchase from any source…five from Suny Inc. and five more from ABC Monitors Inc. at a 50% higher cost.

     The integrator responses also indicate that there are other 20” monitors on the market, however because of fit and form factor differences, they would all require extensive cabinet and wiring redesign.

     Additionally the tasking results show that a 20” flat panel was recently demonstrated at a trade show the integrator attended and looks like a good tech refresh candidate for ODM replacement within the existing cabinet space. Further information is provided about when a prototype might be available for testing (one year), when the OEM will go into production (two years) and how long it will take the integrator to test it out within the system (seven months).

     As a result of this additional information, it is now easier to determine the risk mitigation solutions. The “course solution” for the recommended risk mitigation strategy is to purchase the 10 available ODMs to extend the EOM until the flat panel solution can be tested and deployed to the sites. The flat panel will be available for test the following year. If successful, the integrator has indicated that the production lead-time or the time needed to gear up to produce these flat panel replacement units is 12 months. The necessary information is now in place to assess the risk and to develop the risk mitigation plan. This is done by using the risk worksheet and the risk mitigation waterfall template.

**D.6.3 Selecting the Risk Mitigation Option**

     The risk worksheet illustrated below in Figure D-12 takes the information from the obsolescence analysis worksheet and provides a means to assess the risk likelihood, the risk consequence and how the mitigation activities reduce the risk.

     

       

**Figure D.12. FAA Risk Worksheet for AIS ODM**

     The ODM risk worksheet reads as follows:

- After identifying the **program title** a brief **description** **of the risk** is provided. In this case it is the risk of not being able to support (i.e., not being able to replace) the ODMs when the manufacturer moves on to its next generation product.

     - The **source and root cause** of the risk is identified as the declaration of EOS by Suny and the fact that their next generation display is 21” vice the 20” model currently being used in the workstations and would also require a major redesign to accommodate.

     - Although there are three general **categories of risk** (cost, technical, schedule), COTS product obsolescence and the impact to product support is almost always a technical risk due to the effect an unrepairable failure would have on system performance. This is explained in the rationale block of the worksheet.

     - The **likelihood of this risk** (without mitigation action) is rated as **significant (level 4)** using the definitions contained in Table D-2. This **rationale** is based on the facts that EOS has been declared by Suny and spare resources are limited, thereby justifying the rating because the current approach will not work. Write a short hand description to the right of the likelihood rating definition e.g., “Cannot mitigate risk but different approach might”.

     - The **consequence of realizing the risk** is rated as being **significant (level 4)** using the definitions contained below in Table D-3.  The **rationale** is based on the facts that despite the workstation redundancy and site spares serving as buffers, the actual loss of workstation capability directly affects the system’s mission effectiveness. Write a short hand description to the right of the consequence rating definition e.g., “Unacceptable system performance but alternatives available”. Place an **X** where the risk likelihood and consequence intersect on the green, yellow, red grid.

     - Fill in the **consequence definition**. Even though the course answer is a significant risk likelihood and significant risk consequence, remember that risk is in the eye of the beholder. There will always be some subjectivity associated with applying the definitions and assigning these ratings to a particular situation. However, whether a risk falls into the red zone or yellow zone, it is a risk that most likely deserves analysis and mitigation action.

     - The next task on this worksheet is to identify the **risk resolution date**. In the case of COTS product obsolescence, this will be the date at which point an unacceptable risk to critical system operations may or can occur. The point in time when a failed spare from an operational site cannot be replenished (i.e., EOM) is the threshold we use as the beginning of system degradation. In other words this is the point in time when the system performance baseline, which includes the supportability characteristics, is compromised. Approaching this point of  system operational impact is unacceptable to the field. In this case the EOM “drop dead” date is the 30 months that was calculated before applying any mitigation measures.

     - The last part of the worksheet is a **description** of the sequence of proposed mitigation actions (derived from the obsolescence analysis worksheet) that address the risk and how each action mitigates the **risk level when implemented**. 

**Table D-2. FAA Programmatic Risk Likelihood Definitions**

**Table D-3. FAA Technical Consequence Definitions**

**D.6.4 Scheduling The Risk Mitigation Activities**

 At this point we are ready to fill in the ODM risk mitigation waterfall chart (Figure D-13). This chart provides a standardized method to graphically communicate the effectiveness of the risk mitigation activities to management.

     The first event this chart will capture is when the risk was first determined. Since the integrator’s market research on the ODM was recently received, a high-risk condition is indicated at the current date.

     The first mitigation action to procure the 10 display monitors needs to occur prior to the six month EOS date. The effect of extending the EOM date is identified and the risk level is changed to a high yellow because the obsolescence risk is only somewhat deferred.

**Figure D-13. Risk Mitigation Waterfall Chart for AIS ODM**

     The next action is to acquire and test the prototype (approximately one year to acquire and seven months to test) and indicate its effect of lowering but not resolving the risk condition.

     The last mitigation action that is illustrated is the 12 month production lead time needed to get into the initial solution deployment which returns the risk back to a green condition.

     The completion of this schedule allows the last part of the obsolescence analysis worksheet to be completed. This is when funding needs to be applied to accomplish the mitigation actions.

      This chart provides a very succinct snapshot of this particular risk and the path needed to address it before EOM occurs. It also indicates when funding is needed for these activities. In this case it includes the reprogramming of current funds for the ODM purchase, re-allocation of funds to acquire and test the prototype next year and the programming of funds to produce and deploy the solution in the third year.

**D.6.5 Implementing the Risk Mitigation Plan**

     Implementing risk mitigation planning requires that the appropriate funding be applied when needed. Despite the fact that a clear case has been made for risk mitigation action, budget personnel constantly have to make tradeoffs among many different risk situations to prioritize the limited available funding. This is the reason to be prepared to provide accurate technical rationale and the operational consequences of not addressing the risk.

     In this case the question is what the impact would be if funding were deferred for the prototype development until the following year. Based on the market research information and the waterfall schedule an answer can be provided that allows the budget and decision-making personal to more fully understand the consequences of inaction (or of assuming the risk) as shown in Figure D-14.

 

                                    **Figure D-14. ODM Budget Defense Rationale**

     The increasing ODM failures (as display monitors are prone to do over time) can be pointed out and as a result the linear failure acceleration rate that was used for the EOM projections is understated. A year slip in funding will take the system beyond the EOM date and begin an unacceptable system degradation through the lack of spares, loss of workstations and loss of system mission capability affecting flight sector management and possibly flight safety.

     There is no guarantee that the requested funding will be received, but at a minimum the situation has been illustrated in a consistent, realistic and data-driven manner.

   

     It is now possible to develop a system level obsolescence risk profile by simply plotting out the EOL, EOS, EOR and EOM dates for the top product obsolescence issues onto a schedule as shown in Figure D-15). This chart illustrates the overall system obsolescence risk potential prior to the determination of possible solutions and is meant to convey a snapshot system health status.

**Figure D-15. AIS System Obsolescence Risk Profile**

**D.7 AIS Obsolescence Risk Scenarios**

     The following material identifies five more items for which market research information has been provided by the system integrator for the AIS. The information is in the same format as the ODM sample exercise and the same process for analyzing the information can be used. 

     The risks described below represent a cross-section of possible obsolescence situations and the variety of methods with which to address them. They are derived from actual program experience within the FAA. Should readers wish to try and analyze this information on their own they should use the blank templates provided at the link entitled “Tool Kit” at  HYPERLINK "http://www.faa.gov/aua/resources/cots" http://www.faa.gov/aua/resources/cots. For comparative purposes the course answers are provided in the following pages for each obsolescence situation.

**AIS Line Item #1 – PC Model 2001 Maintenance Workstation**

**AIS Line Item #2 – Data Storage Device Disk Drive**

**AIS Line Item #3 – ODW Graphics Engine**

**AIS Line Item #4 – High Speed Printer Print Head**

**AIS Line Item #5 – Central Computer Complex Operating System**

**Appendix E**

**COTS Technical Performance Factors**

**E.1  Introduction**

     This appendix addresses technical performance characteristics or factors that are unique to COTS-based products and systems that must be considered as part of the standard requirements and functional/performance specification development process.

     Since COTS products are developed to commercial standards to meet a market-based demand, their technical characteristics are pre-determined by the vendors trying to meet that demand. Therefore, performance requirements have to be specified in functional terms that are quantifiable and measurable and need to include certain COTS-unique technical performance factors that will distinguish among the choices of candidate products capable of meeting the requirements. 

     The technical performance factors are listed in Table E-1 (COTS Technical Performance Factors) and are intended to work in conjunction with the COTS Non-Technical Selection Factors identified in Appendix F. The characteristics are organized by major categories.  For each such category, some representative characteristics (some general and some relating more detail) are provided.\*

**\*The major categories and many of the general performance factors are from the Software Engineering Institute (SEI) presentation “Picking the Right COTS Product,” by Tricia Oberndorf (SEI), Santiago Comelia-Dorda (SEI), John Dean (NRC), and Ed Morris (SEI), copyright 2000 by Carnegie-Mellon University, given at the September 2000 SEI Symposium.**

**Table E-1. COTS Technical Performance Factors**

**MAJOR CATEGORY:** ***Hardware Configuration***

|  |  |
| --- | --- |
| **GENERAL  PERFORMANCE FACTORS** | **RELATED  FACTORS** |
| Type |  |
| Memory requirements | Ability of COTS product to perform its function within the memory available in the system. |
| Disk requirements |  |
| Other storage media |  |
| Communications |  |

**MAJOR CATEGORY:** **S*****oftware Configuration***

|  |  |
| --- | --- |
| **GENERAL  PERFORMANCE FACTORS** | **RELATED  FACTORS** |
| Unused features/dead code |  |
| Operating system |  |
| Communications |  |
| Database |  |
| Related applications |  |
| Known compatibility problems | Compatibility with other software products, and with gluecode solutions to compatibility (existing gluecode within systems, gluecode approaches). |

**MAJOR CATEGORY:** ***Standards***

|  |  |
| --- | --- |
| **GENERAL  PERFORMANCE FACTORS** | **RELATED  FACTORS** |
| Standards used (DoD, Industry, Organizational) | Ability to interface (“openness”) |
| Confidence in adherence to standards |  |

**MAJOR CATEGORY:** ***Functionality***

|  |  |
| --- | --- |
| **GENERAL  PERFORMANCE FACTORS** | **RELATED  FACTORS** |
| Suitability |  |
| Accuracy | Precision = "degree of exactness or discrimination with which quantities are stated - e.g., number of decimal places of accuracy". |
| Security | Degree of security in design for system/COTS products |
| Non-Specified Features | Additional capabilities provided by OEM as part of COTS product/system |

**MAJOR CATEGORY:** ***Usability***

|  |  |
| --- | --- |
| **GENERAL  PERFORMANCE FACTORS** | **RELATED  FACTORS** |
| Intended use & users | User awareness of/familiarity with/reaction to system/its use of COTS products/vendors. |
| General operability |  |
| Skill level required |  |
| Responsiveness | Maturity/obsolescence/availability of spare parts etc for product  (??) |
| Robustness | COTS product robustness = “degree to which component can function correctly in presence of stressful environmental condition”. |
| Help capabilities |  |
| Error assist/recovery |  |
| Understandability |  |
| Learnability |  |

**MAJOR CATEGORY:** ***Supportability***

|  |  |
| --- | --- |
| **GENERAL  PERFORMANCE FACTORS** | **RELATED  FACTORS** |
| Self diagnostics |  |
| Disclosure of subcontractors (or other support organizations) | Availability/quality/cost of third party vendors to provide support for products no longer supported by OEM or vendor. |
| Effort of upgrade |  |
| History of upward compatibility | Upward/downward compatibility of product (within system – across system boundary). |
| Site installation support |  |
| Site operation support |  |
| Tool support required |  |
| Analyzability |  |
| Installability | Installation ease: how easily COTS product can be installed in its environment [applies to integration when system being first acquired, and to integration as part of tech refresh/update]. |
| Replacability |  |
| Preventive maintenance |  |

**MAJOR CATEGORY:** ***Interoperability***

|  |  |
| --- | --- |
| **GENERAL  PERFORMANCE FACTORS** | **RELATED  FACTORS** |
| Data model/format |  |
| Support for data access |  |
| Support for control by/of other applications |  |
| Infrastructure utilized |  |
| Infrastructure commonality |  |

**MAJOR CATEGORY:** ***Reliability***

|  |  |
| --- | --- |
| **GENERAL  PERFORMANCE FACTORS** | **RELATED  FACTORS** |
| Test regimen |  |
| Test coverage | "Testability" = ease of establishing test criteria for a COTS product and then performance of corresponding tests. |
| Types/frequency of faults |  |
| Recovery from faults | COTS product safety/risk factors: Fail safe, fail soft, fault tolerant, input error tolerant? |
| MTBF | Availability, failure rate, failure distribution. |

**MAJOR CATEGORY:** ***Performance***

|  |  |
| --- | --- |
| **GENERAL  PERFORMANCE FACTORS** | **RELATED  FACTORS** |
| Benchmarking results | Product performance compared to requirement. |
| Time-related behavior | Execution performance” = degree to which a COTS component performs its functions within given execution timing constraints.    Throughput = the amount of work the COTS component can perform in a specified amount of time. |
| Resource behavior |  |
| Surge capacity |  |

**MAJOR CATEGORY:** **A*****daptability/Flexibility***

|  |  |
| --- | --- |
| **GENERAL  PERFORMANCE FACTORS** | **RELATED  FACTORS** |
| Customization approach | Flexibility = “ease with which COTS component can be tailored for use in applications/environments other than those for which it was specifically designed”.    Range of tuning or adjusting of COTS product performance or  behavior (akin to “tailoring”). |
| Customization effort |  |
| Portability |  |
| Scalability |  |

**Appendix F**

**COTS Non-Technical Selection Factors**

**F.1 Introduction**

     This appendix addresses non-technical characteristics or factors that are unique to COTS-based products and their vendors that must be considered as part of the standard requirements and functional/performance specification development process.

     In screening a group of COTS products for use in a specific system, there will be situations when more than one product meets the functional performance requirements equally well. In such situations COTS products also have important non-technical factors that need to be evaluated to optimize product selection along such qualitative parameters as:

 

Characteristics of the firms in the COTS market (vendors making products, suppliers selling products, firms providing maintenance services for installed COTS products, and integrators building systems out of products), 

Non-technical aspects of the capabilities represented by the products, and

Business-related aspects of the product in question. 

     The selection factor approach should be understood as a form of risk management, within the overall risk management context of using COTS products.   The goal of identifying and then using selection factor is to find the best solution within available resources that minimizes risks and satisfies minimum acceptable levels of value received.  That’s why these factors are important – they help identify and screen out high-risk COTS products.

     As in many other aspects of decision-making involving COTS products, the “85%” rule, itself a risk management approach, needs to be applied when identifying and then using selection factors and finding the data to support their use.  Spending too much time or other resources in an attempt to drive towards a “complete” solution can often result in a diminishing return for the effort expended. 

     In order to apply these characteristics in identifying the factors to be used for a specific product and system, the analyst/user and the decision-maker must:

Determine which product characteristics are meaningful for a given COTS product selection task (some may not apply for specific products, systems, or decisions);

Set the “measurement” level (qualitative or quantitative) for each product characteristic that will be considered to be acceptable; and

Set the relative priorities to be assigned to each of the relevant factors and decide how to use these factors during product evaluation.

     The COTS non-technical selection factors are listed in Table F-1 (COTS Non-Technical Selection Factors) and are intended to work in conjunction with the COTS Technical Performance Factors identified in Appendix E. The characteristics are organized by major categories.  For each such category, some representative characteristics (some general and some relating more details) are provided.\*  

**\*** **The major categories and many of the general factors are from the Software Engineering Institute (SEI)**

**presentation “Picking the Right COTS Product,” by Tricia Oberndorf (SEI), Santiago Comelia-Dorda (SEI), John Dean**

**(NRC), and Ed Morris (SEI), copyright 2000 by Carnegie-Mellon University, given at the September 2000 SEI Symposium.**

**Table F-1.  COTS Non-Technical Selection Factors**

**MAJOR CATEGORY:** ***Vendor Characteristics***

|  |  |
| --- | --- |
| **GENERAL  SELECTION FACTORS** | **RELATED  FACTORS** |
| Organizational stability | Breadth of customer base for firms potentially supplying product: chances they will continue to be active, offer the product, won't depend on FAA for large portion of their sales. |
| Financial stability | Staffing stability |
| Nationality |  |
| Ease of access |  |
| Independence | Partnerships/acquisitions |
| Reputation | Government experience with vendor's products & support:  FAA   Other government organizations |
| Sole Source Vendor |  |
| Support infrastructure |  |
| Engineering approach |  |
| Maintenance approach | Vendor responsiveness:  Response time when critical problems appear  Response to questions, requests for help installing, testing, using products |
| History | Availability/value of warranties.  Vendor level of related experience:  Vendor knowledge of FAA needs and systems  Vendor experience with systems similar to FAA ATC systems  Vendor track record:  Longevity in the market  Success rate as developer  Success of vendor's systems that use COTS products  Use of Lessons Learned re: use of COTS products  Experience in:   Managing end-of-life issues  CM for system w/ multiple baselines   Using Open System Standards for systems   Selecting COTS products for use in systems   Creating/delivering training on COTS-based systems  Market research/watch for COTS products  Analytic tools/metrics for analysis of COTS-related issues  Risk management (identification, analysis, mitigation) in a COTS environment  Testing of COTS candidates    Buy vs. lease decisions for COTS products used in your systems |

**MAJOR CATEGORY:** ***Product Characteristics***

|  |  |
| --- | --- |
| **GENERAL  SELECTION FACTORS** | **RELATED  FACTORS** |
| First shipment date | Maturity of technology in the product |
| Install base | Extent to which product and/or its components are already in inventory vs. adding new configuration items to inventory.    Current/projected use of similar technology or products in same FAA system (have variations in technology/products entered the inventory during the system's installation or operational life?).    Current/projected use of same/similar technology/products in other FAA systems.    Fraction of system in question represented by the COTS product in question |
| Market share |  |
| Market trend | Product configuration stability – new release rate  - typical time span between new releases.    Market/demand demographics:   Product market size (current, projected, trend)  Number of vendors  Longevity of this technology |
| Customer references |  |
| End of life plans |  |
| Availability of training | Availability of training for maintainers, users. |
| Access to hotline |  |
| Availability of consultants |  |
| Delivery method | Availability of product/support via leasing. |
|  | Other detailed characteristics:  Possible effects on product of switch to different technology  Modularity of product design  Special maintenance/support needs characteristic of product.  Availability/cost of spares  Current/projected $ for product, support, spares, licenses, leases.  Price stability/response to market changes  Quantity discounts  Resources needed to manage configuration for product/systems using it.  Price history as function of volume  Availability/cost of data rights (if needed). |

**MAJOR CATEGORY:** ***Documentation***

|  |  |
| --- | --- |
| **GENERAL  SELECTION FACTORS** | **RELATED  FACTORS** |
| Availability of design and maintenance documents |  |
| Customization |  |
| Quality | "Documentation Quality" = "measure/indicator of value of provided documentation for use in using, testing, tailoring, etc the COTS product. |

**MAJOR CATEGORY:** ***Training***

|  |  |
| --- | --- |
| **GENERAL  SELECTION FACTORS** | **RELATED  FACTORS** |
| Materials | Training resources needed (people, time, $, facilities, etc) |
| Courses |  |
| Customization |  |
| Policy on reproduction |  |

**MAJOR CATEGORY:** ***Licenses***

|  |  |
| --- | --- |
| **GENERAL  SELECTION FACTORS** | **RELATED  FACTORS** |
| Standard use & maintenance licenses |  |
| Site licensing |  |
| Quantity discounts |  |
| Transferability of license |  |
| Development/runtime licenses |  |
| Licensing bases (per seat, CPU, etc.) |  |
| Data rights |  |
| Escrow | Vendor willingness to put source code in "escrow," in hands of   3rd party. |

**Appendix G**

**Glossary of Terms**

**Compatibility testing** – the determination of a product’s ability to substitute for another similar product without a major difference in form, fit or function (F3) parameters.

**Compliance testing** – the determination of a product’s ability to comply with specified performance characteristics.

**COTS-based acquisition** – the planning, procuring, integration, testing, fielding and support of a system or change to fielded system that contains COTS products.

**End of life (EOL)** – the stage of COTS product obsolescence that occurs when a product is no longer manufactured by its original equipment manufacturer (OEM) but the OEM is willing and able to provide repair/replacement support services until unprofitable or unable to continue doing so.

**End of maintenance (EOM)** – the stage of COTS product obsolescence that occurs when a site requisition cannot be replenished. The stage change begins with the depletion of limited site and depot spares quantities, followed by service degradation (i.e., loss of redundancy) and ultimately loss of system operations.

**End of repair (EOR)** – the stage of COTS product obsolescence that occurs when hardware product support is no longer available by any means (including third party) or is cost-prohibitive. The stage change is characterized by system usage/demand depleting the remaining depot spares over time which begins to create support uncertainty (or risk) for the program related to such factors as remaining spares quantities, item failure rate, etc.

**End of service (EOS)** – the stage of COTS product obsolescence that occurs when a product is no longer serviced by the OEM but third-party sources are available to provide repair/replacement support services until no longer profitable or unable to do so.

**F****3** – the form (i.e., physical layout), fit (i.e., size) and function (i.e., capability) parameters of a product.

**F****2** – when only two of the three F3 characteristics are the same between products.

**Integrated change planning/integrated change package** – the logical and optimal combination of product obsolescence support options, efficiency improvements and functional enhancements.

**Inter-operability** – a product’s ability to operate with other products without modification.

**Lifecycle** – “a generic term relating to the entire period of conception, definition, build, distribution, operation and disposal of a product.” (AMS Appendix C).

**Market investigation** – a more focused process (subset of market research) of identifying and determining if specific COTS products can meet particular functional requirements. Also includes system obsolescence profiling to proactively plan for the continued support or replacement of soon-to-be obsolete products.

**Market research** – a process of collecting information about existing and emerging technologies, products, manufacturers, suppliers and their trends. It consists of market surveillance and market investigation, the former being a continuous canvassing of the commercial market for all the technologies, vendors’ products and trends that can potentially meet existing and emergent requirements from a strategic perspective.

**Mitigation** – “to make less severe” (Webster’s Collegiate Dictionary).

**Non-developmental Item (NDI)** – an item that has been previously developed for use by federal, state, local or a foreign government and for which no further development is required (AMS Appendix C).

**Programmatic risk** – areas of uncertainty for achieving projected cost, schedule and technical program planning elements.

**Supportability** – “the degree to which product design and planned logistics resources meet product use requirements.” (AMS Appendix C).

**Sustainment** – “those activities associated with keeping fielded products operational and maintained.” (AMS Appendix C).

**Technology evolution planning** – the collection and analysis of COTS product market research information to identify the risks and mitigation measures for projected product obsolescence issues.**Appendix H**

**Acronym List**

AIS  Automated information system

AMS  Acquisition Management System

ANSI  American National Standards Institute

Ao  Operational availability

APB  Acquisition Program Baseline

ARA  Associate Administrator for Research and Acquisitions

BCP  Best commercial practices

CBSs  COTS-based systems

CAST  COTS assessment and selection tool

CCC  Central computer complex

CDRL  Contract data requirements list

CM  Configuration management

COCOTS Constructive COTS 

COTS  Commercial off-the-shelf

CPU  Central processor unit

CWBS  Contract Work Breakdown Structure

DIDs  Data item descriptions

DBMS  Data base management system

DSD  Data storage device

DSR  Display system replacement

ECPs  Engineering change proposals

EOL  End-of-life

EOM  End-of-maintenance

EOR  End-of-repair

EOS  End-of-service

ERAM  En route automation modernization

F2  Any two combinations of form, fit or function

F3  Form, fit, and function

FAA  Federal Aviation Administration

FAST  FAA Acquisition System Toolset

F&E  Facilities and equipment

FY  Fiscal year

GA  Government acceptance

GUI  Graphical user interface

HOCSR Host/Oceanic computer system replacement

HW  Hardware

I&T  Integration and test

IA  Investment analysis

IEEE  Institution of Electrical and Electronic Engineers

INCOSE International Council on Systems Engineering

ISM  In-service management

ISO  International Organization for Standardization 

ISPD   Implementation Strategy and Planning Document

JIT  Just-in-time

LAN  Local area network

LCC  Lifecycle cost

LRU  Lowest replaceable unit

MA                  Mission analysis

MOU  Memorandum of Understanding

NAS  National Airspace System

NDI  Non-developmental items

OCDs  Operational capability demonstrations

ODM  Operator display monitor

ODW  Operator display workstation

OEM  Original equipment manufacturer

OPS  Operations

ORB  Object relation broker

OS  Operating system

P3I  Pre-planned product improvement

PC  Personal computer

R&D   Research and development

RFIs  Requests for information

RMA  Reliability/Maintainability/Availability

SEC  System engineering council

SEM  System Engineering Manual

SEMP  System Engineering Management Plan

SCSI   Small Computer Serial Interface

SI  Solution implementation

SIR  Screening information request

SLOC  Source line of code

SNMP       Simple Network Management Protocol

SQL  Software Query Language

SOW  Statement of work

SW  Software

T&E  Test and evaluation

TCP/IP Transmission control protocol / Internet protocol

URET CCLD User request evaluation tool core capability limited deployment 

WJHTC William J. Hughes Technical Center

WYSIWYG What you see is what you get

PAGE  

**PAGE  vi**

**FAA COTS Risk Mitigation Guide**

**March 2012**

**FAA COTS Risk Mitigation Guide**

**March 2012**

FAA COTS Risk Mitigation Guide   PAGE v

Revision 3.2, Date 01/2010                                                                                                                                                                     

FAA COTS Risk Mitigation Guide

Revision 3.2, Date 01/2010  A- PAGE 2

**FAA COTS Risk Mitigation Guide**

**March 2012**  **B- PAGE 7**

**FAA COTS Risk Mitigation Guide**

**March 2012**  **C- PAGE 2**

**FAA COTS Risk Mitigation Guide**

**March 2012**  **D- PAGE 4**

**FAA COTS Risk Mitigation Guide**

**March 2012**  **E- PAGE 5**

**FAA COTS Risk Mitigation Guide**

**March 2012**  **F- PAGE 4**

**FAA COTS Risk Mitigation Guide**

**March 2012**  **G- PAGE 1**

**FAA COTS Risk Mitigation Guide**

**March 2012**  **H- PAGE 2**

***Acquisition Management System Guidance***

 EMBED Word.Picture.8  

Additional related information  

Notes/Additional Information

Identifies temporary methods of addressing continued failures of this item

Workaround

Describes the operational consequence(s) of continued failures of this item

System Availability Impact

The length of time it will take to acquire and initially deploy production quantities of the change kit

Procurement/Production Lead Time

The amount of time the integrator estimates it will take to acquire the product (or develop a change kit) and the time to test and evaluate the product (or fix) in a system context

T&E Time

Whether or not there are other products from the OEM or from other manufacturers that come close to meeting full form, fit and function  (F3) requirements

Alternate F2 Products Available?

Whether or not there are other products on the market from different manufacturers that are form, fit and function (F3) compatible

Alternate F3 Products Available?

Whether or not the next generation product by the OEM is form, fit and function (F3) compatible with the currently used product

OEM Next Generation Product F3 Compatibility

The number of total spares available at all operational sites

Site Spares

The number of immediately usable spares that are available for replenishment of site spares

Ready For Issue Spares

The total number of spare assets for this item including those in the repair pipeline but not including site spares

Total Depot Spares

Identifies whether or not a failure trend exists (upward, downward or none) by measuring failure data against an agreed upon threshold and includes module repairability success % 

Failure Trend

The actual number of failures that have occurred over the past 12 months

Failure Rate (Last 12 months)

The average number of actual failures per year of this item. If the system is newly fielded, mean time between failure projections may be used until actual failure data is collected

Average Failure Rate (Per Year)

Identifies the software components that interface with this item

S/W Interface

Identifies the hardware components that interface with this item

H/W Interface

When the manufacturer no longer provides repair, replacement or technical support

End of Service Date

When the manufacturer no longer produces this item

End of Life Date

Total quantity of items contained in each system

Quantity Per System

Type of product I.e., COTS, modified COTS or custom made

Item Type

Original equipment manufacturer that produced the item

OEM

Commonly used nomenclature for the item

Item Description

System integration agent’s unique part number assignment

Integrator Part #

Item identification sequence number assigned by the report originator

Line Item #

**Description**

**Information Block Title**
