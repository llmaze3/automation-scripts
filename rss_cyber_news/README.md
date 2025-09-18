## Overview
This automation retrieves cyber security news from multiple RSS feeds using **Make.com** and updates the **Norton database** each morning. The goal is to centralize cyber threat and security news from different outlets into a single source for daily review.

## Workflow
1. **Trigger** – Scheduled run every morning (07:15).
2. **Data Retrieval** – Pulls latest articles from configured RSS feeds (e.g., https://www.bleepingcomputer.com/feed/]).
3. **Database Update** – Inserts new articles into the Norton database for centralized access.
4. **Completion** – Confirms successful update and logs results.


## Benefits
- Provides a single dashboard for cyber news.
- Saves time compared to manually checking multiple news sites.
- Ensures analysts always start the day with updated security headlines.

## Next Steps
- Add new RSS feeds as needed.
– **Processing**: Filter duplicate or already-stored articles.
- Extend the workflow to include threat tagging or enrichment (future).
