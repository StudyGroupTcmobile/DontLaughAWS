# 資料

## Python基本文法
【参考】[Python チュートリアル](https://docs.python.org/ja/3/tutorial/index.html)
### 分岐
```python
if 条件:
    処理
elif 条件:
    処理
else:
    処理
```

### for文
```python
# for 変数 in データの集合（iterableなオブジェクト）
# 処理
# C系の for (int i = 0; i < 10; i++) {}みたいなことをやりたい
for i in range(0, 10):
    処理
```

### 関数
```python
def 関数名():
    処理
```
## Pythonのデータ操作

### for文

```python

for value in values:
    
```
### 辞書型
- keyとvalueが組み合わせになったデータの形
- 一意のkeyを使ってvalueを呼び出すような使い方をする
- JavaだとMapやRubyだとHash, PHPだと連想配列(array)が該当する
- 辞書型のkeyとして使える型（int, str, tuple, frozenset）
- 同じ辞書内に異なる型のkeyやvalueが存在してもよい

#### 宣言
```python
dic = {key1: value1, key2: value2}
```

#### 要素を取得する
```python
dic = {"name": "Taro", "age": "18", "address": "Tokyo"}
print(dic["name"])
# => "Taro"
```


### ネストした辞書型から要素を取得する
- 欲しい`value`を`key`で絞り込む

```python
dic = {
    "family_name": "Yamada",
    "structure" : {
        "father": {
            "first_name": "Jiro",
            "age": "47",
            "address": "Kanagawa"
        },
        "mother": {
            "first_name": "Hanako",
            "age": "44",
            "address": "Kanagawa"
        },
        "eldest_son": {
            "first_name": "Taro",
            "age": "18",
            "address": "Tokyo"
        }
    }
}

print(dic["family_name"])
# => "Yamada"

print(dic["structure"]["eldest_son"])
# => {"first_name": "Taro", "age": "18", "address": "Tokyo"}

print(dic["structure"]["eldest_son"]["first_name"])
# => "Taro
```
#### 全てのkeyの取得
```python
dic = {"name": "Taro", "age": "18", "address": "Tokyo"}
print(dic.keys)
# => ["name", "age", "address"]
```

### 全てのvalueの取得
- リストで取れる
```python
dic = {"name": "Taro", "age": "18", "address": "Tokyo"}
print(dic.values)
# => ["Taro", "18", "Tokyo"]
```

### valueの追加、書き換え
- keyを指定して再代入する
```python
dic = {"name": "Taro", "age": "18", "address": "Tokyo"}
dic["address"] = "Osaka"
print(dic)
# => {"name": "Taro", "age": "18", "address": "Osaka"}
```

## デバッグいろいろ
### オブジェクトの型情報を取得する

- type関数に変数を代入する
```python
x = 'テキスト'
print(type(x))
# => <class 'str'>


x = 10
print(type(x))
# => <class 'int'>


x = True
print(type(x))
# => <class 'bool'>


x = [10, 20, 30, 'テキスト']
print(type(x))
# => <class 'list'>


x = {'a':10, 'b':20, 'c':30, 'd':'テキスト'}
print(type(x))
# => <class 'dict'>
```

### JSONを整形して出力する

【参考】[[python] JSONファイルのフォーマットを整えてDumpする](https://qiita.com/Hyperion13fleet/items/7129623ab32bdcc6e203)
```python
print(json.dumps(faces, indent=4, sort_keys=True))
```

※ 配布したコードの49行目に記載しています。

※ APIの実行を1度だけにするためにwhile文の直前でカウンタを作成し、while文の条件にカウンタの制限をつけている。

## boto3
全ての情報は以下（英語）

【参考】[Boto3 Docs 1.11.5 rekognition](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition.html)

## 目次
- `detect_faces()`
- `detect_labels()`
- `detect_text()`
- ``

### detect_labels()
- イメージ内のラベルの検出


- https://docs.aws.amazon.com/ja_jp/rekognition/latest/dg/labels-detect-labels-image.html

