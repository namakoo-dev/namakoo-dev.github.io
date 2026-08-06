Option VBASupport 1
Option Explicit

' 見積: 単価 x 数量 と合計
Sub FillQuote(oDoc As Object)
    Dim oSheet As Object, i As Long, total As Double
    oSheet = oDoc.Sheets.getByIndex(0)
    For i = 5 To 9
        Dim u As Double, q As Double
        u = oSheet.getCellByPosition(2, i).getValue()
        q = oSheet.getCellByPosition(3, i).getValue()
        oSheet.getCellByPosition(4, i).setValue(u * q)
        total = total + u * q
    Next i
    oSheet.getCellByPosition(4, 10).setValue(total)
End Sub

' 受注: 粗利率 = (受注額 - 原価) / 受注額。書式もここで付ける
Sub FillMargin(oDoc As Object)
    Dim oSheet As Object, i As Long
    Dim oFmts As Object, nFmt As Long
    Dim aLoc As New com.sun.star.lang.Locale
    oSheet = oDoc.Sheets.getByIndex(0)
    oFmts = oDoc.getNumberFormats()
    nFmt = oFmts.queryKey("0.0%", aLoc, False)
    If nFmt = -1 Then nFmt = oFmts.addNew("0.0%", aLoc)
    For i = 4 To 8
        Dim s As Double, c As Double
        s = oSheet.getCellByPosition(2, i).getValue()
        c = oSheet.getCellByPosition(3, i).getValue()
        If s > 0 Then oSheet.getCellByPosition(4, i).setValue((s - c) / s)
    Next i
    oSheet.getCellRangeByPosition(4, 4, 4, 8).NumberFormat = nFmt
End Sub
