# Tables & Statistics

This page contains statistical tables from our survey.


## Survey Comparison

*Comparison between this work and existing surveys.*


| **Paper** | **Language** | **What** | **Why** | **How** | **Pipeline** | **Highlights** |
| --- | --- | --- | --- | --- | --- | --- |
| Recommender Systems Meet Large Language Model Agents: A Survey | ❌ | ✅ | ❌ | ✅ | (1) Agents for RS (2) RS for Agents (3) Trustworthy Agents and RS | analyzes how the LLM agent module supports recommendation systems and how recommendation systems,in turn, optimize the operation of these agents. |
| A Survey on LLM-powered Agents for Recommender Systems | ❌ | ✅ | ❌ | ✅ | (1) Recommender-oriented approaches (2) Interaction-oriented approaches (3) Simulation-oriented approaches | identifies three key paradigms in current research and explores their architectural components and evaluation frameworks. |
| A Survey of Large Language Model Empowered Agents for Recommendation and Search: Towards Next-Generation Information Retrieval | ❌ | ✅ | ❌ | ✅ | (1) User Interaction (2) Item Representation (3) System Integration (4) Environment Simulation | emphasizes how LLM-powered agents improve recommender systems by enabling deep semantic understanding, dynamic task decomposition, and interactive user engagement |
| **Ours** | ✅ | ✅ | ✅ | ✅ | (1) Where agents are applied (2) What agents are used (3) Why agents are used (4) How agents are designed | proposes four key questions��"Where," "What," "Why," and "How" to conduct a comprehensive analysis of the existing academic research. |


## Agent as Rec (WHERE)

*Papers where agents serve as the primary recommendation entity.*


| **Model Name** | **Paper** | **Single/Multi** | **Application Scenarios** | **Venue** |
| --- | --- | --- | --- | --- |
| InteRecAgent | [Recommender AI Agent: Integrating Large Language Models for Interactive Recommendations](https://dl.acm.org/doi/full/10.1145/3731446) | Single | Interactive Improvement | ACM TRANS'25 |
| STARec | [STARec: An Efficient Agent Framework for Recommender Systems via Autonomous Deliberate Reasoning](https://dl.acm.org/doi/10.1145/3746252.3760995) | Single | General Recommendation | CIKM'25 |
| MARC | [MARC: Multimodal and Multi-Task Agentic Retrieval-Augmented Generation for Cold-Start Recommender System](https://arxiv.org/abs/2511.08181) | Multi | Domain-Specific | CIKM'25 |
| REMI | [REMI: A Novel Causal Schema Memory Architecture for Personalized Lifestyle Recommendation Agents](https://oars-workshop.github.io/papers/Raman2025.pdf) | Single | Domain-Specific | KDD'25 |
| ChatCRS | [Incorporating External Knowledge and Goal Guidance for LLM-based Conversational Recommender Systems](https://aclanthology.org/2025.findings-naacl.17/) | Multi | Interactive Improvement | NAACL'25 |
| MMAgentRec | [MMAgentRec | Multi | Domain-Specific | Scientific Reports'25 |
| PUMA | [Large Language Models Empowered Personalized Web Agents](https://dl.acm.org/doi/10.1145/3696410.3714842) | Single | Domain-Specific | WWW'25 |
| AgentDR | [AgentDR: Dynamic Recommendation with Implicit Item-Item Relations via LLM-based Agents](https://arxiv.org/pdf/2510.05598) | Single | General Recommendation | arXiv'25 |
| TAIRA | [Thought-Augmented Planning for LLM-Powered Interactive Recommender Agent](https://arxiv.org/abs/2506.23485) | Multi | Interactive Improvement | arXiv'25 |
| MATCHA | [MATCHA:CanMulti-Agent Collaboration Build a Trustworthy  Conversational Recommender?](https://arxiv.org/pdf/2504.20094) | Multi | Interactive Improvement | arXiv'25 |
| RouteLLM | [Constraint-Aware Route Recommendation from Natural Language via Hierarchical LLM Agents](https://arxiv.org/pdf/2510.06078) | Multi | Domain-Specific | arXiv'25 |
| CDA4Rec | [Cloud-Device Collaborative Agents for Sequential Recommendation](https://arxiv.org/pdf/2509.01551) | Multi | Domain-Specific | arXiv'25 |
| MADREC | [MADREC:AMulti-Aspect Driven LLM Agent for Explainable and Adaptive Recommendation](https://arxiv.org/pdf/2510.13371) | Single | General Recommendation | arXiv'25 |
| Shuang et al. | [An Extremely Data-efficient and Generative LLM-based Reinforcement Learning Agent for Recommenders](https://arxiv.org/pdf/2408.16032) | Single | Domain-Specific | KDD'24 |
| RecMind | [RecMind: Large Language Model Powered Agent For Recommendation](https://aclanthology.org/2024.findings-naacl.271/) | Single | General Recommendation | NAACL'24 |
| AutoConcierge | [Automated Interactive Domain-Specific Conversational Agents that Understand Human Dialogs](https://link.springer.com/chapter/10.1007/978-3-031-52038-9_13) | Single | Domain-Specific | PADL'24 |
| MAS4POI | [MAS4POI: a Multi-Agents Collaboration System  for Next POI Recommendation](https://link.springer.com/chapter/10.1007/978-981-96-8180-8_28) | Multi | Domain-Specific | PAKDD'24 |
| MACRec | [MACRec: a Multi-Agent Collaboration Framework for Recommendation](https://dl.acm.org/doi/abs/10.1145/3626772.3657669) | Multi | General Recommendation | SIGIR'24 |
| RecAI | [RecAI: Leveraging Large Language Models for Next-Generation Recommender Systems](https://dl.acm.org/doi/abs/10.1145/3589335.3651242) | Single | General Recommendation | WWW'24 |
| MACRS | [A Multi-Agent Conversational Recommender System](https://arxiv.org/pdf/2402.01135) | Multi | Interactive Improvement | arXiv'24 |
| PMS | [Personalized Recommendation Systems using Multimodal, Autonomous, Multi Agent Systems](https://arxiv.org/pdf/2410.19855) | Multi | Interactive Improvement | arXiv'24 |
| Rec4Agentverse | [Prospect Personalized Recommendation on Large Language Model-based Agent Platform](https://arxiv.org/pdf/2402.18240) | Multi | Interactive Improvement | arXiv'24 |


## Agent for Rec (WHERE)

*Papers where agents interact with the system to enhance performance.*


| **Model Name** | **Paper** | **Single/Multi** | **Application Scenarios** | **Venue** |
| --- | --- | --- | --- | --- |
| Zhang et al. | [LLM-Powered User Simulator for Recommender System](https://ojs.aaai.org/index.php/AAAI/article/view/33456) | Single | General Recommendation | AAAI'25 |
| iAgent | [iAgent: LLM Agent as a Shield between User and Recommender Systems](https://arxiv.org/pdf/2502.14662) | Single | Interactive Improvement | ACL'25 |
| RecAgent | [User Behavior Simulation with Large Language Model based Agents](https://dl.acm.org/doi/full/10.1145/3708985) | Single | Evaluation & Security | ACM TRANS'25 |
| Lusifer | [Lusifer: LLM-based User Simulated Feedback  Environment For online Recommender systems](https://ieeexplore.ieee.org/abstract/document/11141085/) | Single | Domain-Specific | IEEE'25 |
| TextSimu | [ID-Free Not Risk-Free: LLM-Powered Agents Unveil Risks in  ID-Free Recommender Systems](https://dl.acm.org/doi/abs/10.1145/3726302.3730003) | Multi | Evaluation & Security | SIGIR'25 |
| iALP | [Large Language Model driven Policy Exploration for  Recommender Systems](https://dl.acm.org/doi/abs/10.1145/3701551.3703496) | Single | Interactive Improvement | WSDM'25 |
| RecUserSim | [RecUserSim: A Realistic and Diverse User Simulator for  Evaluating Conversational Recommender Systems](https://dl.acm.org/doi/pdf/10.1145/3701716.3715258) | Single | Evaluation & Security | WWW'25 |
| DiscomfortFilter | [Filtering discomforting recommendations with large language models](https://dl.acm.org/doi/abs/10.1145/3696410.3714850) | Multi | Domain-Specific | WWW'25 |
| CSHI | [A LLM-based Controllable, Scalable, Human-Involved User Simulator Framework for Conversational Recommender Systems](https://dl.acm.org/doi/abs/10.1145/3696410.3714858) | Single | Interactive Improvement | WWW'25 |
| DrunkAgent | [Get the Agents Drunk: Memory Perturbations in Autonomous  Agent-based Recommender Systems](https://arxiv.org/pdf/2503.23804) | Single | Evaluation & Security | arXiv'25 |
| RuleAgent | [RuleAgent: Discovering Rules for Recommendation Denoising  with Autonomous Language Agents](https://arxiv.org/pdf/2503.23374) | Single | Domain-Specific | arXiv'25 |
| CARTS | [CARTS: Collaborative agents for recommendation textual summarization](http://arxiv.org/pdf/2506.17765) | Multi | Domain-Specific | arXiv'25 |
| Chirag Shah et al. | [Dynamic Evaluation Framework for Personalized and Trustworthy Agents: A Multi-Session Approach to Preference Adaptability](https://www.arxiv.org/pdf/2504.06277) | Multi | Evaluation & Security | arXiv'25 |
| CreAgent | [CreAgent: Towards Long-Term Evaluation of Recommender System under Platform-Creator Information Asymmetry](https://arxiv.org/pdf/2502.07307) | Single | Evaluation & Security | arXiv'25 |
| Yoon et al. | [Evaluating Large Language Models as Generative User Simulators for  Conversational Recommendation](https://aclanthology.org/2024.naacl-long.83/) | Single | Evaluation & Security | ACL'24 |
| PEARL | [PEARL: Preference Extraction with Exemplar Augmentation and Retrieval with LLM Agents](https://aclanthology.org/2024.emnlp-industry.112.pdf) | Multi | Domain-Specific | EMNLP'24 |
| CheatAgent | [CheatAgent: Attacking LLM-Empowered Recommender Systems via LLM Agent](https://dl.acm.org/doi/10.1145/3637528.3671837) | Single | Evaluation & Security | KDD'24 |
| Agent4Rec | [On Generative Agents in Recommendation](https://dl.acm.org/doi/abs/10.1145/3626772.3657844) | Multi | Evaluation & Security | SIGIR'24 |
| ToolRec | [Let Me Do It For You: Towards LLM Empowered Recommendation via Tool Learning](https://dl.acm.org/doi/abs/10.1145/3626772.3657828) | Single | Domain-Specific | SIGIR'24 |
| USimAgent | [USimAgent: Large Language Models for Simulating Search Users](https://dl.acm.org/doi/abs/10.1145/3626772.3657963) | Single | Evaluation & Security | SIGIR'24 |
| RAH | [RAH! RecSys-Assistant-Human: A Human-Centered Recommendation Framework with LLM Agents](https://ieeexplore.ieee.org/abstract/document/10572486) | Multi | General Recommendation | TCSS'24 |
| SimpleUserSim | [How Reliable is Your Simulator? Analysis on the Limitations of  Current LLM-based User Simulators for Conversational  Recommendation](https://dl.acm.org/doi/abs/10.1145/3589335.3651955) | Single | Evaluation & Security | WWW'24 |
| SUBER | [SUBER: An RL Environment with Simulated  Human Behavior for Recommender Systems](https://arxiv.org/pdf/2406.01631) | Single | Evaluation & Security | arXiv'24 |
| PEPPER | [Stop Playing the Guessing Game ! Target-free User Simulation for Evaluating Conversational Recommender Systems](https://www.arxiv.org/pdf/2411.16160) | Single | Evaluation & Security | arXiv'24 |
| iEvaLM | [Rethinking the Evaluation for Conversational Recommendation  in the Era of Large Language Models](https://arxiv.org/pdf/2305.13112) | Single | Evaluation & Security | EMNLP'23 |
| CORE | [Lending Interaction Wings to Recommender Systems with Conversational Agents](https://proceedings.neurips.cc/paper_files/paper/2023/hash/58cd3b02902d79aea4b3b603fb0d0941-Abstract-Conference.html) | Single | Interactive Improvement | NeurlPS'23 |


## Agent in Rec (WHERE)

*Papers where agents are embedded in specific process stages.*


| **Model Name** | **Paper** | **Single/Multi** | **Application Scenarios** | **Venue** |
| --- | --- | --- | --- | --- |
| RPP | [Reinforced prompt personalization for recommendation with large language models](https://dl.acm.org/doi/full/10.1145/3716320) | Multi | General Recommendation | ACM TRANS'25 |
| AgentCF++ | [AgentCF++: Memory-enhanced LLM-based Agents for  Popularity-aware Cross-domain Recommendations](https://dl.acm.org/doi/abs/10.1145/3726302.3730161) | Multi | General Recommendation | SIGIR'25 |
| ARAG | [ARAG: Agentic Retrieval Augmented Generation for  Personalized Recommendation](https://arxiv.org/pdf/2506.21931) | Multi | General Recommendation | SIGIR'25 |
| AFL | [Agentic Feedback Loop Modeling Improves Recommendation  and User Simulation](https://dl.acm.org/doi/abs/10.1145/3726302.3729893) | Multi | Domain-Specific | SIGIR'25 |
| VRAgent-R1 | [VRAgent-R1: Boosting Video Recommendation with MLLM-based Agents via Reinforcement Learning](https://arxiv.org/pdf/2507.02626) | Multi | Domain-Specific | arXiv'25 |
| Jie Wang et al. | [Reinforcement Learning-based Recommender Systems with  Large Language Models for State Reward and Action Modeling](https://dl.acm.org/doi/abs/10.1145/3626772.3657767) | Single | General Recommendation | SIGIR'24 |
| BiLLP | [Large Language Models are Learnable Planners for Long-Term  Recommendation](https://dl.acm.org/doi/abs/10.1145/3626772.3657683) | Multi | Evaluation & Security | SIGIR'24 |
| AgentCF | [AgentCF: Collaborative Learning with Autonomous Language  Agents for Recommender Systems](https://dl.acm.org/doi/abs/10.1145/3589334.3645537) | Multi | Interactive Improvement | WWW'24 |
| KGLA | [KGLA: Knowledge Graph Enhanced Language Agents for Recommendation](https://arxiv.org/pdf/2410.19627) | Multi | General Recommendation | arXiv'24 |
| CSA | [Contrastive State Augmentations for Reinforcement  Learning-Based Recommender Systems](https://dl.acm.org/doi/abs/10.1145/3539618.3591656) | Single | General Recommendation | SIGIR'23 |


## HOW Dimension - Module Usage

*Analysis of optimization modules: Profile, Memory, Planning, and Action.*


| **Methods** | **Profile Module** | **Memory Module** | **Planning Module** | **Action Module** | **Code** | **Model(Framework)** | **Dataset** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| AFL | ❌ | ✅ | ✅ | ✅ | ✅ | GPT-4o-mini | Lastfm, Steam, MovieLens |
| Agent4Rec | ✅ | ✅ | ❌ | ✅ | ✅ | LangChain | MovieLens-1M, Steam, Book |
| AgentCF | ❌ | ✅ | ❌ | ✅ | ❌ | RecBole | CDs and Vinyl, Office Products |
| AgentCF++ | ❌ | ✅ | ❌ | ❌ | ✅ | GPT-4o-mini | Books, CDs, Movies, Games |
| AgentDR | ❌ | ✅ | ❌ | ✅ | ❌ | Phi-4 | Instacart, Electronics, Sports |
| ARAG | ❌ | ✅ | ✅ | ✅ | ❌ | GPT-3.5-turbo | Review |
| AutoConcierge | ✅ | ✅ | ✅ | ✅ | ❌ | GPT-3 | No available datasets |
| BiLLP | ❌ | ❌ | ✅ | ❌ | ✅ | GPT-3.5-turbo-16k | Steam, Book |
| CARTS | ❌ | ✅ | ❌ | ✅ | ❌ | GPT-4o | Beauty, Electronics, Fashion |
| CDA4Rec | ✅ | ❌ | ✅ | ✅ | ❌ | LLaMA-3.1-8B | ReDial, Music4All, Sports |
| ChatCRS | ✅ | ❌ | ✅ | ❌ | ✅ | GPT-3.5-turbo-1106, LLaMA-7b | DuRecDial, TG-Redial |
| CheatAgent | ❌ | ❌ | ✅ | ❌ | ❌ | T5 | MovieLens-1M, LastFM, Taobao |
| Chirag Shah et al. | ✅ | ✅ | ✅ | ✅ | ❌ | Not Specified | Not Specified |
| CORE | ❌ | ❌ | ✅ | ❌ | ❌ | GPT-3.5-turbo | Amazon, Last.fm, Yelp, Taobao |
| CreAgent | ✅ | ✅ | ❌ | ✅ | ✅ | Llama3-8B | YouTube |
| CSA | ❌ | ✅ | ❌ | ✅ | ✅ | Tensorflow | RC15, RetailRocket and Meituan |
| CSHI | ✅ | ✅ | ❌ | ✅ | ✅ | GPT-3.5-turbo | ReDial, OpenDialKG, MovieLens |
| DiscomfortFilter | ✅ | ❌ | ❌ | ❌ | ❌ | Multiple LLMs | MIND |
| DrunkAgent | ❌ | ✅ | ❌ | ❌ | ❌ | LLaMA3-8B-Instruct | CDs & Vinyl, Office Products, Musical |
| iAgent | ✅ | ✅ | ❌ | ❌ | ✅ | GPT-4o-mini | Book, Movie, Goodreads |
| iALP | ❌ | ❌ | ✅ | ✅ | ❌ | Mistral 7B | LFM, Industry, Coat |
| iEvaLM | ❌ | ❌ | ❌ | ✅ | ✅ | GPT-3.5-turbo | ReDial, OpenDialKG |
| InteRecAgent | ✅ | ✅ | ✅ | ❌ | ✅ | LangChain | Steam, MovieLens, Beauty |
| Jie Wang et al. | ❌ | ✅ | ✅ | ✅ | ❌ | Mistral 7B | LFM, Industry |
| KGLA | ❌ | ✅ | ❌ | ❌ | ❌ | Claude3-Haiku-20240307 | CDs, Clothing, Beauty |
| Lusifer | ❌ | ✅ | ❌ | ✅ | ✅ | GPT-4o-mini | MovieLens |
| MACRec | ✅ | ✅ | ✅ | ✅ | ✅ | GPT-3.5-turbo-1106 | Generate data |
| MACRS | ✅ | ✅ | ✅ | ✅ | ❌ | GPT-3.5-turbo-0613, Llama-2-70b-chat-hf | MovieLens |
| MADREC | ✅ | ✅ | ❌ | ❌ | ❌ | GPT-4.1-nano | Beauty, Sports, Toys |
| MARC | ❌ | ❌ | ✅ | ✅ | ✅ | GPT-4o | cocktails, ingredients and instructions |
| MAS4POI | ✅ | ✅ | ✅ | ✅ | ✅ | Six Distinct LLMs | NYC, TKY |
| MATCHA | ❌ | ❌ | ✅ | ✅ | ❌ | Multiple LLMs | OMuleT, WildJailbreak |
| MMAgentRec | ✅ | ✅ | ❌ | ✅ | ❌ | BERT | Guangdong Tourism Dataset, QK-Video |
| PEARL | ❌ | ✅ | ❌ | ✅ | ❌ | Claude-instant-v1 | Internal Dataset, MultiWOZ-H |
| PEPPER | ❌ | ✅ | ❌ | ✅ | ❌ | GPT-3.5-turbo | IMDb, ReDial, OpenDialKG |
| PMS | ✅ | ✅ | ✅ | ✅ | ❌ | LangChain | Created dataset |
| PUMA | ❌ | ✅ | ❌ | ✅ | ✅ | LLaMA-2-7B | Review |
| RAH | ✅ | ✅ | ✅ | ✅ | ❌ | GPT-4-0613 | Movies, Books, Video Games |
| Rec4Agentverse | ✅ | ✅ | ✅ | ✅ | ❌ | GPT-4 | Generate data |
| RecAgent | ✅ | ✅ | ❌ | ✅ | ❌ | ChatGPT | MovieLens-1M, Beauty, Book-Crossing |
| RecAI | ✅ | ✅ | ✅ | ❌ | ✅ | GPT-4 | Beauty, Video Games, MovieLens 1M |
| RecMind | ❌ | ✅ | ✅ | ✅ | ❌ | GPT-3.5-turbo-16k | Reviews, Yelp |
| RecUserSim | ✅ | ✅ | ❌ | ✅ | ❌ | Multiple LLMs | Generate data |
| REMI | ❌ | ✅ | ✅ | ✅ | ❌ | Gemini-2.0-Flash | Generate data |
| RouteLLM | ❌ | ❌ | ✅ | ✅ | ✅ | GPT-4o | Generate data |
| RPP | ❌ | ❌ | ❌ | ✅ | ✅ | LLaMa2-7B-chat | ML-1M, Games, Lastfm |
| RuleAgent | ✅ | ✅ | ✅ | ✅ | ❌ | GPT-4o mini | Beauty, Yelp2018, Gowalla |
| Shuang et al. | ❌ | ❌ | ❌ | ✅ | ❌ | BERT | WebShop |
| SimpleUserSim | ✅ | ❌ | ❌ | ✅ | ❌ | iEvaLM | ReDial, OpenDialKG |
| STARec | ❌ | ❌ | ✅ | ✅ | ❌ | Multiple LLMs | MovieLens 1M, CDs and Vinyl |
| SUBER | ❌ | ✅ | ❌ | ❌ | ✅ | Sentence-T5 | ML-latest small, Book |
| TAIRA | ❌ | ❌ | ✅ | ❌ | ✅ | GPT-4o | Clothing & Shoes, Beauty, Music |
| TextSimu | ✅ | ✅ | ✅ | ✅ | ❌ | GPT-4o mini | Beauty, Instrument, Office |
| ToolRec | ❌ | ❌ | ✅ | ✅ | ✅ | GPT-3.5-turbo-16k | ML-1M, Book, Yelp2018 |
| USimAgent | ❌ | ❌ | ✅ | ✅ | ❌ | GPT-4 | UserStudy |
| VRAgent-R1 | ❌ | ✅ | ✅ | ✅ | ❌ | Qwen2.5-7B | MicroLens-100K, MovieLens-1M |
| Yoon et al. | ❌ | ✅ | ❌ | ✅ | ✅ | PyABSA | ReDial, Reddit, MovieLens |
| Zhang et al. | ✅ | ❌ | ✅ | ❌ | ✅ | ChatGLM-6B | Yelp, Music, Games |


---


**Total Tables**: 5
