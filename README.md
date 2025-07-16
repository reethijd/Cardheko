# Cardheko
This project focuses on building a predictive model to estimate used car prices based on various features such as body type, kilometers driven, model year, transmission, ownership, and brand.

The raw dataset was provided in Excel format, containing nested JSON-like feature information inside single cells. Extensive preprocessing was performed to normalize and clean the data, including JSON parsing, missing value imputation, outlier treatment, encoding of categorical features, and scaling of numerical columns.

Multiple regression algorithms were tested (Linear Regression, Decision Tree, Random Forest, XGBoost) and compared to select the best-performing model. Hyperparameter tuning was performed using RandomizedSearchCV to further optimize performance.

Finally, the selected Random Forest model was deployed using Streamlit to create an interactive web application. Users can input car details through a simple interface and get instant price predictions.

All code, data samples, trained model, and the deployment app are available in this repository for easy reproducibility and demonstration
# Libraries used for the workflow
# Data Handling & Analysis

pandas — For reading CSV/Excel, cleaning, manipulating DataFrames

numpy — For numerical operations, arrays, NaN handling
# Visualization

matplotlib — For plots like histograms, scatter plots, boxplots

seaborn — For heatmaps, correlation plots, enhanced visuals
# Machine Learning

sklearn (scikit-learn):

train_test_split — For splitting data

LinearRegression, DecisionTreeRegressor, RandomForestRegressor, XGBRegressor — Models

StandardScaler, MinMaxScaler — Scaling

OneHotEncoder — Encoding categorical variables

SimpleImputer — For mean/mode imputation (if used)

RandomizedSearchCV — For hyperparameter tuning

metrics — For R², MAE, etc.
# Deployment

streamlit — To build the web app
# Saving the Model

pickle — To save and load your trained .pkl file

