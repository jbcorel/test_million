
#Имитация базы данных
db = {}

def get_full_link(short_link: str) -> str:
    return db.get(short_link, None)


def get_short_link(link: str):
    return db.get(link, None)



def create(link: str, short_link: str, created_at: str) -> dict :
    db.update({
        short_link: {
            'full': link,
            'created_at': created_at
        },
        link: {
            'short': short_link,
            'created_at': created_at
        }
    })
    print(db)
    return get_short_link(link=link)
    

def delete(short_link: str):
    value = db.pop(short_link, None)
    if value:
        db.pop(value['full'])
            
