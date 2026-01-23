# Templates for Batch Import - Agent4Rec Survey

This folder contains CSV templates for batch importing papers.

## 📄 Paper Template (`papers_template.csv`)

### Column Definitions

| Column | Description | Required | Example |
|--------|-------------|----------|---------|
| `category_id` | Paper category | ✅ | `general` |
| `short_name` | Short name/identifier | ✅ | `RecMind` |
| `title` | Full paper title | ✅ | `RecMind: Large Language Model Powered Agent For Recommendation` |
| `authors` | Author list | ❌ | `Authors et al.` |
| `venue` | Publication venue | ❌ | `NAACL'24` |
| `year` | Publication year | ✅ | `2024` |
| `arxiv` | arXiv URL | ❌ | `https://arxiv.org/abs/...` |
| `github` | GitHub URL | ❌ | `https://github.com/...` |
| `huggingface` | HuggingFace URL | ❌ | `-` |
| `doi` | DOI URL | ❌ | `-` |
| `website` | Other website URL | ❌ | `-` |

### Valid Category IDs

- `general` - 📈 General Recommendations
- `domain_specific` - 🔍 Domain-Specific Recommendations
- `interactive` - 📚 Interactive Recommendations
- `evaluation` - 🎮 System Evaluation
- `single_agent` - 🤖 Single-Agent Systems
- `multi_agent` - 👥 Multi-Agent Systems

### Usage

1. Open `papers_template.csv` in Excel/LibreOffice/Text Editor
2. Fill in your papers (one row per paper)
3. Save the file
4. Import: `run.bat` → `[3] Batch Import`
5. Or: `python scripts/batch_import.py templates/papers_template.csv`

### Example Data

```csv
category_id,short_name,title,authors,venue,year,arxiv,github,huggingface,doi,website
general,RecMind,RecMind: Large Language Model Powered Agent For Recommendation,Authors et al.,NAACL'24,2024,https://arxiv.org/...,-,-,-,-
single_agent,PUMA,Large Language Models Empowered Personalized Web Agents,Authors et al.,WWW'25,2025,-,https://github.com/...,-,-,-
```

## 💡 Tips

1. **Empty Fields**: Use `-` or leave blank for optional fields
2. **Excel Editing**: Open CSV files in Excel for easier editing
3. **UTF-8 Encoding**: Save files as UTF-8 to support special characters
4. **Validation**: Script automatically checks for duplicates
5. **Testing**: Import a few papers first to verify the format

## 📝 Notes

- Lines starting with `#` are treated as comments and ignored
- Duplicate papers are automatically detected and skipped
- All imports can be previewed before confirmation
- Run sync scripts automatically after import
