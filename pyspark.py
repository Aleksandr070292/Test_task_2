from pyspark.sql import SparkSession
from pyspark.sql.functions import col

def get_product_category_pairs_with_no_category(products_df, categories_df):
    # Объединяем датафреймы продуктов и категорий по общему полю (например, id продукта)
    joined_df = products_df.join(categories_df, products_df["product_id"] == categories_df["product_id"], "left_outer")

    # Выбираем только необходимые столбцы (Имя продукта и Имя категории)
    result_df = joined_df.select(products_df["product_name"], categories_df["category_name"])

    # Фильтруем строки, чтобы получить только продукты, у которых нет категорий
    products_with_no_category = result_df.filter(col("category_name").isNull())

    return products_with_no_category


if __name__ == "__main__":
    spark = SparkSession.builder.appName("ProductCategoryPairs").getOrCreate()

    # Создаем примеры датафреймов с продуктами и категориями
    products_data = [("p1", "product1"), ("p2", "product2"), ("p3", "product3")]
    products_df = spark.createDataFrame(products_data, ["product_id", "product_name"])

    categories_data = [("p1", "category1"), ("p2", "category2")]
    categories_df = spark.createDataFrame(categories_data, ["product_id", "category_name"])

    # Получаем результат по заданной задаче
    result = get_product_category_pairs_with_no_category(products_df, categories_df)
    result.show()

    spark.stop()