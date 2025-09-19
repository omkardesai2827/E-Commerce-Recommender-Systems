# E-Commerce Recommender System

<img width="1465" height="878" alt="image" src="https://github.com/user-attachments/assets/92521c5e-1acf-4d45-a09b-4a2b66d576b2" />


This repository contains the implementation of a comprehensive e-commerce recommender system developed as a final project for a Machine Learning course. The system includes three distinct recommendation approaches: **Transactional (Market Basket) Recommender**, **Item-Item Recommender**, and **User-Item Recommender**. These systems are designed to enhance user experience in online shopping by providing personalized product suggestions based on transaction patterns, item similarities, and user behavior.

The project was built using Python, leveraging libraries such as Pandas, Scikit-learn, PyTorch, and Streamlit for the UI. It demonstrates practical applications of machine learning algorithms in real-world e-commerce scenarios.

## Table of Contents
- [Project Overview](#project-overview)
- [Recommender Systems Explained](#recommender-systems-explained)
  - [Transactional (Market Basket) Recommender](#transactional-market-basket-recommender)
  - [Item-Item Recommender](#item-item-recommender)
  - [User-Item Recommender](#user-item-recommender)
- [Algorithms and Logic](#algorithms-and-logic)
- [Real-Life Use Cases](#real-life-use-cases)
- [Contributors](#contributors)

## Project Overview
In e-commerce, recommender systems play a crucial role in driving sales, improving customer satisfaction, and increasing engagement. This project addresses three common challenges:
- **Cross-selling opportunities** from transaction data (e.g., "Customers who bought X also bought Y").
- **Similarity-based recommendations** for new or cold-start users (e.g., similar products to a viewed item).
- **Personalized suggestions** based on user history (e.g., tailored to past purchases and interactions).

We processed a dataset of over 1.3 million transaction records, including product details, user profiles, and purchase histories. The systems were evaluated for efficiency, accuracy, and relevance, with a focus on scalable algorithms suitable for large datasets.

## Recommender Systems Explained
### Transactional (Market Basket) Recommender
This system analyzes transaction data to identify frequent itemsets and association rules. It suggests products that are commonly purchased together.

- **Logic**: 
  - Group transactions by order ID to form "baskets."
  - Mine frequent patterns and generate rules like "If antecedent (X), then consequent (Y)."
  - Filter and rank rules based on metrics such as support, confidence, and lift.

- **Example**: If a user adds "Olive Crew Neck T-shirt" to their cart, recommend "Purple Crew Neck T-shirt" based on high lift.

### Item-Item Recommender
This collaborative filtering approach recommends products similar to a given item, ideal for new users without purchase history.

- **Logic**:
  - Combine product features (e.g., name, description, category, price) into a text vector.
  - Compute similarity using vector embeddings.
  - Recommend top-N similar items, excluding the query item itself.

- **Example**: For "Black Drawstring Trackpants," suggest similar athletic wear like "Dark Grey Drawstring Trackpants."

### User-Item Recommender
This system provides personalized recommendations based on a user's past interactions and purchases.

- **Logic**:
  - Create a user-item interaction matrix (e.g., based on purchases and add-to-cart counts).
  - Decompose the matrix to learn latent factors.
  - Predict and rank unseen items for each user, excluding previously interacted items.

- **Example**: For a user who bought sneakers and T-shirts, recommend complementary items like socks or jackets.

## Algorithms and Logic
- **FP-Growth (Frequency Pattern Growth) for Market Basket**:
  - Builds a compact FP-tree from transactions in two database scans, avoiding multiple passes over large data (unlike Apriori).
  - Shares branches for common patterns, reducing memory usage.
  - Mines frequent itemsets directly from the tree, focusing on lift (>1) to identify meaningful associations (e.g., "buy X makes Y 1.4x more likely").
  - Why FP-Growth? Efficient for 1.3M+ records; avoids combinatorial explosion.

- **Cosine Similarity for Item-Item**:
  - Measures angle between item feature vectors (e.g., TF-IDF or combined text features).
  - Formula: <img width="616" height="90" alt="image" src="https://github.com/user-attachments/assets/5784c981-c04a-4d12-8c62-9ef95af28de4" />

  - Incorporates Term Frequency (TF) for word importance in descriptions and Inverse Document Frequency (IDF) to downweight common terms.
  - Logic: High cosine score indicates similar products; used for top-10 recommendations.

- **NMF (Non-Negative Matrix Factorization) + NCF (Neural Collaborative Filtering) for User-Item**:
  - **NMF**: Decomposes interaction matrix into non-negative factors, capturing broad patterns while ignoring noise.
    
    <img width="480" height="283" alt="image" src="https://github.com/user-attachments/assets/38f10fcb-a435-4a13-b720-fe059af1bbd7" />
    
  - **NCF**: Uses neural networks to learn embeddings and non-linear interactions via multi-layer perceptrons.
  - Combined Logic: Predict scores from both models, average them for hybrid ranking. Exclude seen items and select top-N.
  - Why Hybrid? NMF for reliable trends; NCF for nuanced, non-linear preferences.

## Real-Life Use Cases
- **Market Basket**: Upsell during checkout (e.g., Amazon's "Frequently bought together"). Increases average order value by surfacing cross-sell opportunities.
- **Item-Item**: Product detail pages for cold-start users (e.g., "Similar products" on eBay). Helps with discovery when user data is limited.
- **User-Item**: Personalized homepages or emails (e.g., Netflix-style "Recommended for you" on Shopify). Boosts retention by tailoring to individual journeys.
- Overall: These systems can increase conversion rates by 10-30% in e-commerce, as seen in platforms like Alibaba or Walmart.

## Contributors
- **Omkar Desai** - Logic and model building
- **Panagiotis Valsamis** - logic and interface building

**We did this project as a group for our 2nd semester Machine learning course.**
