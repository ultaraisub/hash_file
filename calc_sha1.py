import hashlib
import sys

def calculate_sha1(file_path):
    """指定されたファイルのSHA-1ハッシュ値を計算する関数"""
    # SHA-1ハッシュオブジェクトの作成
    sha1_hash = hashlib.sha1()

    try:
        # ファイルをバイナリ読み込みモードで開く
        with open(file_path, "rb") as f:
            # 4096バイトずつ読み込み、ハッシュを更新する（メモリ枯渇対策）
            for chunk in iter(lambda: f.read(4096), b""):
                sha1_hash.update(chunk)
                
        # 16進数の文字列としてハッシュ値を返す
        return sha1_hash.hexdigest()
        
    except FileNotFoundError:
        return "エラー: 指定されたファイルが見つかりません。"
    except Exception as e:
        return f"予期せぬエラーが発生しました: {e}"

if __name__ == "__main__":
    # ハッシュを計算したいファイルのパスをここに指定します
    # （例としてコマンドライン引数から取得する形にしています）
    if len(sys.argv) > 1:
        target_file = sys.argv[1]
    else:
        target_file = "sample.txt" # デフォルトのファイル名 (SHA-1: fd0d40481601165e5a5a5d4c1202481dac2cbd86)
        
    print(f"対象ファイル: {target_file}")
    
    result = calculate_sha1(target_file)
    print(f"SHA-1ハッシュ値: {result}")
