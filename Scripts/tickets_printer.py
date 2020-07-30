""" Module for Printing the Tambola Ticket to PDF """

# pylint: disable = C0301

import os
import sys
from datetime import datetime as dt
import pdfkit

import tambola_tickets as t
import colors as c

def styles():
    """
    Function returns the styles for the HTML to be exported.
    """

    color_codes = c.colors()

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

def markup(number=6):
    """
    Function returns the markup code for the output file.
    """

    html = f"<html>{styles()}<body>"
    side = ('left', 'right')
    flag = False
    ticket_count = 0

    for ticket in t.ticket_agent(number):
        if ticket_count%12 == 0:
            html += '<div class="page">'

        if ticket_count%6 == 0:
            html += f'<div class="split {side[int(flag)]}">'

        html += '<table id = "ticket">\n'
        for line, _ in enumerate(ticket):
            html += '<tr>\n'
            for cell, _ in enumerate(ticket[line]):
                html += f'<td id="{chr(65+line)}{cell+1}">'
                if ticket[line][cell]:
                    html += str(ticket[line][cell])
                else:
                    html = html[:-1]
                    html += ' class="blank">  \n'
                html += '</td>\n'
            html += '</tr>\n'
        html += '</table>\n'

        ticket_count += 1
        if ticket_count%6 == 0:
            flag = not flag
            html += '</div>\n'
        if ticket_count%12 == 0:
            html += '</div>'

    html += "</body></html>\n"

    return html

def convert_to_html(html, filename='Tambola_Tickets_' + dt.now().strftime('%d%b%Y%H%M%S')):
    """
    Writes the markup to an HTML file.
    """
    fullpath = os.path.join(os.path.split(os.getcwd())[0], 'Printouts', filename + '.html')
    with open(fullpath, "w") as file:
        file.write(html)

    return fullpath

def html_to_pdf(filename='Tambola_Tickets_' + dt.now().strftime('%d%b%Y%H%M%S')):
    """
    Renders HTML to PDF.
    """
    fullpath = os.path.join(os.path.split(os.getcwd())[0], 'Printouts')
    pdf_file = os.path.join(fullpath, filename + '.pdf')
    path_wkhtmltopdf = os.path.join(os.path.split(os.getcwd())[0], 'Extras', 'wkhtmltopdf.exe')
    config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
    _ = pdfkit.from_file(os.path.join(fullpath, filename + '.html'), pdf_file, configuration=config)

    os.remove(os.path.join(fullpath, filename + '.html'))
    print(f'\n-- Deleted {filename+".html"} --')

    return os.path.join(os.getcwd(), pdf_file)

def main():
    """
    Creates PDF of the Tambola Tickets
    """
    try:
        number_of_tickets = int(sys.argv[1]) if len(sys.argv) > 1 else 1
        html = markup(number_of_tickets)
        if len(sys.argv) > 2:
            print(f'\nHTML File: {convert_to_html(html, str(sys.argv[2]))}\n')
            print(f'\nPDF File: {html_to_pdf(str(sys.argv[2]))}\n')
        else:
            print(f'\nHTML File: {convert_to_html(html)}\n')
            print(f'\nPDF File: {html_to_pdf()}')
    except:
        print('Invalid Arguments. Please retry.')
        sys.exit(0)

if __name__ == "__main__":
    main()
