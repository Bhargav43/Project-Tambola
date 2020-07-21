import pdfkit
import os
import sys

import TambolaTickets as t
import Colors as c

def StyleSheet():
    """
    Function returns the styles for the HTML to be exported.
    """

    color_codes = c.Colors()

    style = '\n'.join((
        '*{text-align: center;color: ' + color_codes[0] + ' !important; -webkit-print-color-adjust: exact; font-size: 25px;font-family:calibri;}',
        'body{width: 794px; margin: auto;}',
        '.split {width:390px; height: 1063;  overflow-x:hidden; margin: auto; margin-top: 40px; margin-bottom: 40px; }',
        '.left {float: left; position:relative;}',
        '.right {position:relative; page-break-after:always;}',
        '.page {margin: auto; border:1px solid; border-color: #FFFFFF; height: 1223px; width: 794px;}',
        'table{margin: auto; margin-top: 35px; margin-bottom: 35px; width: 380px; height: 130px; border-radius: 10px 10px 10px 10px;border: 1px solid; background-color: ' + color_codes[1] + ' !important;}',
        'td{border-radius: 10px 10px 10px 10px;background-color: #FFFFFF !important;}',
        'td.blank{background-color: ' + color_codes[2] + ' !important;}'
    ))

    return f'<style>{style}</style>'

def Markup(number = 6):
    """
    Function returns the markup code for the output file.
    """

    html = f"<html>{StyleSheet()}<body>"
    side = ('left', 'right')
    flag = False
    ticket_count = 0

    for ticket in t.ticketAgent(number):
        if ticket_count%12==0:
            html+= '<div class="page">'

        if ticket_count%6 == 0:
            html+=f'<div class="split {side[int(flag)]}">'

        html+= f'<table id = "ticket">\n'
        for line in range(len(ticket)):
            html+='<tr>\n'
            for cell in range(len(ticket[line])):
                html+= f'<td id="{chr(65+line)}{cell+1}">'
                if ticket[line][cell]:
                    html+=str(ticket[line][cell])
                else:
                    html = html[:-1]
                    html+=' class="blank">  \n'
                html+='</td>\n'
            html+='</tr>\n'
        html+='</table>\n'

        ticket_count+=1
        if ticket_count%6 == 0:
            flag = not flag
            html+='</div>\n'
        if ticket_count%12==0:
            html+= '</div>'

    html+= "</body></html>\n"

    return html

def convert_to_html(html, filename = 'Tambola Tickets'):
    """
    Writes the markup to an HTML file.
    """

    with open(filename+'.html', "w") as f:
        f.write(html)

    return os.path.join(os.getcwd(), filename+'.html')

def html_to_pdf(filename = 'Tambola Tickets'):
    """
    Renders HTML to PDF.
    """

    pdf_file = filename+'.pdf'
    path_wkhtmltopdf = r'E:\Installation Directory\wkhtmltopdf\bin\wkhtmltopdf.exe'
    config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
    a = pdfkit.from_file(filename+'.html', pdf_file, configuration=config)

    return os.path.join(os.getcwd(), pdf_file)

def main():
    try:
        number_of_tickets = int(sys.argv[1]) if len(sys.argv)>1 else 1
        filename = str(sys.argv[2]) if len(sys.argv)>2 else 'Tambola Tickets'
    except:
        print('Invalid Arguments. Please retry.')
        sys.exit(0)

    html = Markup(number_of_tickets)
    print(f'\nHTML File: {convert_to_html(html, filename)}\n')
    print(f'\nPDF File: {html_to_pdf(filename)}\n')

if __name__=="__main__":
    main()