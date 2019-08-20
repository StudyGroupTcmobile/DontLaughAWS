# Amazon Rekognition

本READMEは、以下のAmmazon Rekoginition公式リファレンスの、API仕様について概略化したものです。
詳しくは、公式リファレンスより参照願います。

* https://docs.aws.amazon.com/ja_jp/rekognition/latest/dg/what-is.html

## Amazon Rekognitionとは

　画像分析と動画分析をアプリケーションに組み込むことができる。RekognitionAPIに画像や動画を指定するだけで、コンテンツ中のモノ、人物、テキスト、シーン、行動を識別することができる。また、高精度な顔認識をはじめとした、多様なユースケースに向けた顔の検出、比較、分析ができる。

※ 予算の都合で利用するAPIがAmazon Rekoginition Imageのみであることを確認

## 一般的なユースケース

* 画像や動画における物体やシーンの検出
* 顔ベースのユーザー比較検証によるアイデンティティの確認
* 顔の画像からによる嬉しい、悲しい、驚きなどの感情、および性別などの人口統計情報を検出
* 保存済みの顔データ(画像、動画)と比較して、検索したいデータ中に一致する顔がないかといった顔認識
* 不適切なコンテンツの検出
* 有名人認識
* テキスト検出

## Amazon Rekognition Imageで画像に対する実行できる検出と認識のタイプについて

* ラベル検出
* 顔の検出と比較
* 有名人の認識
* イメージモデレーション
* イメージ検出内のテキスト

## Amazon Rekognition ImageAPI一覧

### 非ストレージ型オペレーション(リクエストするコンテンツが保存されない)

[詳細](https://docs.aws.amazon.com/ja_jp/rekognition/latest/dg/how-it-works-storage-non-storage.html)

#### DetectLabels

S3バケット内の画像(jpgまたはpng)内のラベルを検出できます。

* [リファレンス(英語)](https://docs.aws.amazon.com/ja_jp/rekognition/latest/dg/API_DetectLabels.html)
* [開発者ガイド(日本語)](https://docs.aws.amazon.com/ja_jp/rekognition/latest/dg/labels-detect-labels-image.html)

#### DetectFaces

リクエストに含まれる顔に関するコンテンツかS3バケット内のオブジェクトについて、
目、鼻、口などの主な顔の特徴を探して入力イメージ内の顔を検出できます。

* [リファレンス(英語)](https://docs.aws.amazon.com/ja_jp/rekognition/latest/dg/API_DetectFaces.html)
* [開発者ガイド(日本語)](https://docs.aws.amazon.com/ja_jp/rekognition/latest/dg/faces-detect-images.html)

#### CompareFaces

ソースイメージ内の顔とターゲットイメージ内の各顔を比較できます。

* [リファレンス(英語)](https://docs.aws.amazon.com/ja_jp/rekognition/latest/dg/API_CompareFaces.html)
* [開発者ガイド(日本語)](https://docs.aws.amazon.com/ja_jp/rekognition/latest/dg/faces-comparefaces.html)

#### DetectModerationLabels

* [リファレンス(英語)](https://docs.aws.amazon.com/ja_jp/rekognition/latest/dg/API_DetectModerationLabels.html)
* [開発者ガイド(日本語)](https://docs.aws.amazon.com/ja_jp/rekognition/latest/dg/moderation.html)

イメージまたはビデオに明示的または暗示的なアダルトコンテンツが含まれているかどうかを判定できます()

#### RecognizeCelebrities

イメージ内の有名人を認識し、認識した有名人に関する追加情報を取得できます。

* [リファレンス(英語)](https://docs.aws.amazon.com/ja_jp/rekognition/latest/dg/API_RecognizeCelebrities.html)
* [開発者ガイド(日本語)](https://docs.aws.amazon.com/ja_jp/rekognition/latest/dg/celebrities-procedure-image.html)

#### DetectText

イメージのバイト配列 (base64 エンコードされたイメージのバイト) を指定するか、S3 オブジェクトを指定して、単語と行の関係 (Id と ParentId)、イメージ上のテキストの位置 (Geometry)、検出されたテキストと境界ボックスの精度を示す Amazon Rekognition の信頼度 (Confidence)、検出されたテキストのタイプ (Type)等の情報を取得できます。

* [リファレンス(英語)](https://docs.aws.amazon.com/ja_jp/rekognition/latest/dg/API_DetectText.html)
* [開発者ガイド(日本語)](https://docs.aws.amazon.com/ja_jp/rekognition/latest/dg/text-detecting-text-procedure.html)

### ストレージ型オペレーション

* [IndexFaces](https://docs.aws.amazon.com/ja_jp/rekognition/latest/dg/API_IndexFaces.html)
* [ListFaces](https://docs.aws.amazon.com/ja_jp/rekognition/latest/dg/API_ListFaces.html)
* [SearchFacesByImage](https://docs.aws.amazon.com/ja_jp/rekognition/latest/dg/API_SearchFacesByImage.html)
* [SearchFaces](https://docs.aws.amazon.com/ja_jp/rekognition/latest/dg/API_SearchFaces.html)
* [DeleteFaces](https://docs.aws.amazon.com/ja_jp/rekognition/latest/dg/API_DeleteFaces.html)
* [DescribeCollection](https://docs.aws.amazon.com/ja_jp/rekognition/latest/dg/API_DescribeCollection.html)