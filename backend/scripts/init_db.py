import sys
import os
# 将 backend 目录加入系统路径，以便导入 app 模块
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.models.database import engine, Base, SessionLocal
from app.models.tables import Product, Obstacle, Recipe
import json

def init_database():
    # 创建所有表
    Base.metadata.create_all(bind=engine)
    print("数据库表创建完成。")

    db = SessionLocal()
    try:
        # ----- 插入示例商品（坐标请根据实际货架位置调整）-----
        products = [
            Product(name="红富士苹果", price=5.8, cost=3.0, supplier="本地农场",
                    discount=0.9, image_url="apple.png", shelf_id=1, pos_x=2.5, pos_y=2.3),
            Product(name="鲜香菇", price=12.0, cost=7.0, supplier="菌菇基地",
                    image_url="mushroom.png", shelf_id=2, pos_x=2.5, pos_y=3.8),
            Product(name="洗衣粉", price=19.9, cost=12.0, supplier="日化厂",
                    image_url="detergent.png", shelf_id=3, pos_x=6.0, pos_y=6.0),
        ]
        db.add_all(products)

        # ----- 插入示例货架障碍物（与 map_data.json 对应）-----
        obstacles = [
            Obstacle(name="水果区货架", type="rect", x1=1.0, y1=2.0, x2=4.0, y2=2.6),
            Obstacle(name="蔬菜区货架", type="rect", x1=1.0, y1=3.5, x2=4.0, y2=4.1),
        ]
        db.add_all(obstacles)

        # ----- 插入示例菜谱 -----
        recipes = [
            Recipe(name="红烧肉", ingredients=json.dumps(["五花肉","酱油","冰糖","葱","姜","料酒"])),
            Recipe(name="芹菜炒肉", ingredients=json.dumps(["芹菜","猪肉","蒜","生抽"])),
        ]
        db.add_all(recipes)

        db.commit()
        print(f"已插入 {len(products)} 个商品, {len(obstacles)} 个货架, {len(recipes)} 个菜谱。")
    except Exception as e:
        db.rollback()
        print("数据插入失败：", e)
    finally:
        db.close()

if __name__ == "__main__":
    init_database()