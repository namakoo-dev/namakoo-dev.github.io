Option VBASupport 1
Option Explicit

' 版数の行を差し替え、末尾にロット件数を追記する。
' ★ この .bas は文書に埋め込まれない。実行時に流し込まれる。
Sub Revise(oDoc As Object)
    Dim oEnum As Object, oPar As Object, n As Integer
    oEnum = oDoc.Text.createEnumeration()
    Do While oEnum.hasMoreElements()
        oPar = oEnum.nextElement()
        If oPar.supportsService("com.sun.star.text.Paragraph") Then
            If InStr(oPar.getString(), "版数：初版") > 0 Then
                oPar.setString("製造管理課　版数：第 2 版（basrun 改訂 2026-08-06）")
                n = n + 1
            End If
        End If
    Loop
    Dim oText As Object, oCur As Object
    oText = oDoc.Text
    oCur = oText.createTextCursorByRange(oText.getEnd())
    oText.insertString(oCur, Chr(13) & "対象ロット " & _
        (oDoc.TextTables.getByIndex(0).Rows.Count - 1) & " 件 / 版数差し替え " & n & " 箇所", False)
End Sub
