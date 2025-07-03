
## API Endpoints

### 1. Generate Content Brief and Article Title
- **Endpoint**: `/generate_brief_title`
- **Method**: `POST`
- **Request Body**:
  ```json
  {
    "keyword": "string"
  }
  ```
- **Response Body**:
  ```json
  {
    "content_brief": "string",
    "article_title": "string"
  }
  ```

### 2. Generate Full Article
- **Endpoint**: `/generate_article`
- **Method**: `POST`
- **Request Body**:
  ```json
  {
    "keyword": "string",
    "article_title": "string",
    "content_brief": "string"
  }
  ```
- **Response Body**:
  ```json
  {
    "full_article": "string"
  }
  ```

