def build_html(table: str, customer_name: str) -> str:
    return f"""
<!DOCTYPE html>
<html>
    <body>
    <div style="background-color: #eee; padding: 10px 20px">
      <p
        style="font-family:Georgia, 'Times New Roman', Times, serif;color:#454349;"
      >
        Dear IBM <b>{customer_name}</b>
      </p>

      </div>
      <div style="padding: 10px 20px">
      <p style="font-family:Georgia, 'Times New Roman', Times, serif">
        Hope this note finds you well. We have noticed the following invoice are
        open on our system. <br>
        If you have already paid them, please provide us the proof of payment or
        remittance details to do our internal research. <br>
        
      </p>
      <p style="font-family:Georgia, 'Times New Roman', Times, serif">
        If you have requested the cancellation at some point, please provide us the cancellation request so that we can process it. <br> 
        We will really appreciate your help in sending the payment if none of the above had occurred previously.
      </p>
      <div>
        {table}
      </div>
      <br>
      <p style="font-family:Georgia, 'Times New Roman', Times, serif">
        <b>Please see below our payment information Check to:</b> <br>
IBM Corporation<br>
PO BOX 645510<br>
PITTSBURGH PA 15264-5253<br>
Please include your invoice number on the check.
      </p>
      <p style="font-family:Georgia, 'Times New Roman', Times, serif">
        <b> Wire transfer to: </b><br>
PNC Bank, Pittsburgh PA <br>
Swift Code: PNCCUS33 <br>
ABA Routing #: 043000096<br>
Account Name: IBM Corporation - SaaS Account<br>
Account #: 1029161101
      </p>
      
      <br>
      <p style="font-family:Georgia, 'Times New Roman', Times, serif" >
        Regards,<br>
Irene Jiménez Hernández<br>
Q2C Operations US HECP AR Collector.<br>Squad Leader Cecilia Lozano Torres<br>
      </p>
      <p style="font-family:Georgia, 'Times New Roman', Times, serif">
        Finance and Operations <br>
<a href="mailto:Irene.Jimenez.Hernandez@ibm.com ">Irene.Jimenez.Hernandez@ibm.com </a><br>
+18842162156 ext. 5441
      </p>


      </div>
    </div>
  </body>
</html>
"""
