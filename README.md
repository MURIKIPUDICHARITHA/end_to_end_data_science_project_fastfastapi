
# FastAPI Model Deployment

This project demonstrates how to use FastAPI to serve a machine learning model.

## How to Run

1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Run the app:
   ```
   uvicorn app_fastapi:app --reload
   ```

3. Access API at:
   - Home: `http://127.0.0.1:8000/`
   - Swagger UI: `http://127.0.0.1:8000/docs`
   - JSON endpoint: `http://127.0.0.1:8000/predict`

## Input Format

```json
{
  "feature1": 1.0,
  "feature2": 2.0
}
```
