import json
import pandas as pd
import os

class FewShotPosts:
    def __init__(self):
        base_path = "data"

        self.creator_data = {
            "Muskan Handa": self._load_creator(
                os.path.join(base_path, "processed_posts_muskan_handa.json")
            ),
            "Ankur Warikoo": self._load_creator(
                os.path.join(base_path, "processed_posts_ankur_warikoo.json")
            )
        }

    def _load_creator(self, file_path):
        with open(file_path, encoding="utf-8") as f:
            posts = json.load(f)

        df = pd.json_normalize(posts)
        df["length"] = df["line_count"].apply(self.categorize_length)

        median_engagement = df["engagement"].median()

        return {
            "df": df,
            "median_engagement": median_engagement
        }

    def categorize_length(self, line_count):
        if line_count < 5:
            return "Short"
        elif 5 <= line_count <= 10:
            return "Medium"
        else:
            return "Long"

    def get_tags(self, creator):
        df = self.creator_data[creator]["df"]
        return sorted(set(sum(df["tags"], [])))

    def get_filtered_posts(self, length, language, tag, creator):
        data = self.creator_data[creator]
        df = data["df"]
        median_engagement = data["median_engagement"]

        # basic filters
        if language:
            df = df[df["language"] == language]

        if length:
            df = df[df["length"] == length]

        # quality + relevance filter
        if tag:
            df = df[
                (df["engagement"] >= median_engagement) |
                (df["tags"].apply(lambda tags: tag in tags))
            ]
        else:
            df = df[df["engagement"] >= median_engagement]

        return df.to_dict(orient="records")
