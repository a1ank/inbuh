import smtplib as root
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

login = 'alan.khalaf@mail.ru'
password = 'bTEZiieAEpyRNTrwLiSK'
url = 'smtp.mail.ru'
toaddr = 'alan.khalaf@mail.ru'
topic = '@talkwithjohn_bot'

message = """\
<!DOCTYPE html>
<link rel="stylesheet" href="style.css">
<div id="DroppableDiv" class="layout droppable customer-email mobile-mail-repl ui-droppable ui-sortable"
    current-email-width="600" style="padding-top:20px; /* border: 1px solid red; */">
    <div class="line email-struc-item card-holder" id="line_1">
        <div class="email-sized-wrapper email-columns card-holder"
            style="width: 600px; border-left-width: 0px; border-right-width: 0px;">
            <div class="droppable" id="droppable_2"
                style="width: 600px; border: 0px; background-color: rgb(238, 238, 238);">
                <div class="out_block email-text-out-block ui-draggable" data-element-type="text"
                    elemtype="mail_text_simple" id="out_block_2"
                    style="padding: 20px 30px; background-color: rgb(238, 238, 238);">
                    <div class="mob-hidden-handler-wrapper handler-wrapper constructor-menu-items js-mob-hidden-icon">
                        <div class="handler-item"><img
                                src="https://www.inbuh.kz/cms/uploads/file_1631694866_138107176.png" style="width: 144px;
                            max-width: 600px; display: inline-block; vertical-align: top; padding: 10px;"
                                alt="mobile hidden"></div>
                    </div>
                    <div class="mail_text_simple_border data_text email-text mce-content-body" id="mce_0">
                        <div>
                            <div><span style="font-size: 16px;"
                                    data-mce-style="font-size: 16px; padding-bottom: 0px 0px 20px 20px;">Здравствуйте!</span>
                            </div>
                            <div>
                                <div><br></div>
                                <div><span style="font-size: 16px;" data-mce-style="font-size: 16px;">Настоящим письмом
                                        уведомляем о том, что банковские реквизиты ТОО «Интернет
                                        Бухгалтерия»<strong>&nbsp;изменились</strong>.</span></div>
                                <div><br></div>
                                <div><span style="font-size: 16px;" data-mce-style="font-size: 16px;"><strong>Новые
                                            реквизиты для безналичных расчетов</strong>&nbsp;приведены ниже.</span>
                                </div>
                                <div><br></div>
                                <div><span style="font-size: 16px;" data-mce-style="font-size: 16px;">ТОО «Интернет
                                        Бухгалтерия»</span></div>
                                <div><span style="font-size: 16px;"
                                        data-mce-style="font-size: 16px;">Адрес:&nbsp;050000, Казахстан, г. Алматы, ул.
                                        Бродского д. 33.2</span></div>
                                <div><span style="font-size: 16px;"
                                        data-mce-style="font-size: 16px;">БИН:&nbsp;160940004650</span></div>
                                <div><span style="font-size: 16px;" data-mce-style="font-size: 16px;">Kбе: 17</span>
                                </div>
                                <div>
                                    <div><span style="font-size: 16px;" data-mce-style="font-size: 16px;"><strong>ИИК
                                                KZ72722S000008370810&nbsp;&nbsp;</strong></span></div>
                                    <div><span style="font-size: 16px;" data-mce-style="font-size: 16px;"><strong>БИК
                                                CASPKZKA АО "KASPI BANK" &nbsp;</strong></span></div>
                                </div>
                                <div><span style="font-size: 16px;" data-mce-style="font-size: 16px;">&nbsp;</span>
                                </div>
                                <div><span style="font-size: 16px;" data-mce-style="font-size: 16px;">Спасибо, что вы с
                                        нами!</span></div>
                            </div>
                        </div>
                        <div><span style="font-size: 16px;" data-mce-style="font-size: 16px;">&nbsp;</span></div>
                        <div><span style="font-size: 16px;" data-mce-style="font-size: 16px;">С уважением, Интернет
                                Бухгалтерия</span></div>
                        <div><span style="font-size: 16px;" data-mce-style="font-size: 16px;">Web:&nbsp;<a
                                    href="http://www.inbuh.kz/" rel="noopener noreferrer" target="_blank"
                                    data-link-id="2" data-mce-href="http://www.inbuh.kz/">www.inbuh.kz</a></span></div>
                        <div><span style="font-size: 16px;" data-mce-style="font-size: 16px;">Email:&nbsp;<a
                                    href="mailto:info@inbuh.kz" rel="noopener noreferrer" target="_blank"
                                    data-mce-href="mailto:info@inbuh.kz">info@inbuh.kz</a>,&nbsp;<a
                                    href="mailto:support@inbuh.kz" rel="noopener noreferrer" target="_blank"
                                    data-mce-href="mailto:support@inbuh.kz">sales@inbuh.kz</a></span></div>
                        <div><span style="font-size: 16px;" data-mce-style="font-size: 16px;">Tel:&nbsp;<a
                                    href="tel:+7(727)352-85-55" rel="noopener noreferrer" target="_blank"
                                    data-mce-href="tel:+7(727)352-85-55">+7 (727) 352-85-55</a>,&nbsp;<a
                                    href="tel:+7(777)270-46-33" rel="noopener noreferrer" target="_blank"
                                    data-mce-href="tel:+7(777)270-46-33">+7 (707) 350-02-32</a></span></div>
                        <div><span style="font-size: 16px;"
                                data-mce-style="font-size: 16px;">-------------------------------------------------------------------</span>
                        </div>
                        <div><span style="font-size: 16px;" data-mce-style="font-size: 16px;">Наши услуги:</span></div>
                        <div><span style="font-size: 16px;" data-mce-style="font-size: 16px;">- Аренда конфигураций
                                1С;</span></div>
                        <div><span style="font-size: 16px;" data-mce-style="font-size: 16px;">- Ведение бухгалтерского и
                                налогового учета;</span></div>
                        <div><span style="font-size: 16px;" data-mce-style="font-size: 16px;">- Сдача налоговой
                                отчетности;</span></div>
                        <div><span style="font-size: 16px;" data-mce-style="font-size: 16px;">- Автоматическое
                                формирование отчетов для руководителей и др.</span></div>
                    </div>
                </div>
                <div style="align-items: center;display: flex;justify-content: space-around;">
                    <div style="align-items: center;display: flex;justify-content: space-around;">
                        <div class="social_element"><a href="https://www.facebook.com/inbuh/" target="_blank"><img src="https://login.sendpulse.com/img/constructor/social/round/facebook.png" hspace="5"
                                    vspace="5" width="32px"></a></div>
                        <div class="social_element"><a href="https://www.instagram.com/inbuh/" target="_blank"><img src="https://login.sendpulse.com/img/constructor/social/round/twitter.png" hspace="5"
                                    vspace="5" width="32px"></a></div>
                        <div class="social_element"><a href="https://t.me/inbuh" target="_blank"><img src="https://login.sendpulse.com/img/constructor/social/round/telegram.png" hspace="5"
                                    vspace="5" width="32px"></a></div>
                        <div class="social_element"><a href="https://www.youtube.com/channel/UCTHT3en7CdRpNRjg3XlAu3Q" target="_blank"><img src="https://login.sendpulse.com/img/constructor/social/round/youtube.png" hspace="5"
                                    vspace="5" width="32px"></a></div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <div class="line email-struc-item card-holder" id="line_3">
        <div class="move-handler-wrapper handler-wrapper constructor-menu-items">
            <div class="move-handler-line handler-item"><span class="constr-icon icon-move"></span></div>
        </div>
        <div class="email-sized-wrapper email-columns card-holder"
            style="width: 600px; border-left-width: 0px; border-right-width: 0px;">
            <div class="droppable" id="droppable_3"
                style="border: 0px; background-color: rgb(238, 238, 238);">
                <div class="out_block ui-draggable" data-element-type="divider" elemtype="mail_delimiter"
                    id="out_block_4" style="padding:15px;">
                    <div class="mail_devider" style="padding-top: 0px; padding-bottom: 0px;">
                        <hr style="border-top: 1px solid #B2B2B2;">
                    </div>
                    <div class="move-handler-wrapper handler-wrapper constructor-menu-items">
                        <div class="move-handler-item handler-item"><span class="constr-icon icon-move"></span></div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <div class="line email-struc-item card-holder" id="line_4">
        <div class="email-sized-wrapper email-columns card-holder"
            style="width: 600px; border-left-width: 0px; border-right-width: 0px;">
            <div class="droppable" id="droppable_4"
                style="width: 600px; border: 0px; background-color: rgb(238, 238, 238);">
                <div class="out_block email-text-out-block ui-draggable" data-element-type="text"
                    elemtype="mail_text_simple" id="out_block_5" style="padding: 10px 0px;">
                    <div class="mail_text_simple_border data_text email-text mce-content-body"
                        style="font-weight: normal; line-height: 1; position: relative;" id="mce_2">
                        <p style="text-align: center;" data-mce-style="text-align: center;"><span
                                style="font-size: 12px;" data-mce-style="font-size: 12px;">© 1С Онлайн 2022 ТОО
                                «Интернет бухгалтерия»</span></p>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <div class="line email-struc-item card-holder" id="line_5">
        <div class="move-handler-wrapper handler-wrapper constructor-menu-items">
            <div class="move-handler-line handler-item"><span class="constr-icon icon-move"></span></div>
        </div>
        <div class="email-sized-wrapper email-columns card-holder"
            style="width: 600px; border-left-width: 0px; border-right-width: 0px; border-bottom-width: 0px;">
            <div class="droppable" id="droppable_5"
                style="width: 600px; border: 0px; background-color: rgb(238, 238, 238);">
                <div class="out_block email-text-out-block ui-draggable" data-element-type="text"
                    elemtype="mail_text_simple" id="out_block_6"
                    style="padding: 10px 30px 10px 0px; background-color: rgb(238, 238, 238);">
                    <div class="move-handler-wrapper handler-wrapper constructor-menu-items">
                        <div class="move-handler-item handler-item"><span class="constr-icon icon-move"></span></div>
                    </div>

                    <div class="mail_text_simple_border data_text email-text mce-content-body"
                        style="font-weight: normal; position: relative;" id="mce_3">
                        <p style="text-align: center;" data-mce-style="text-align: center;"><span
                                style="font-size: 13px;" data-mce-style="font-size: 13px;">Вы получили данную рассылку,
                                так как являетесь клиентом или подписчиком нашей компании. Вы можете <a
                                    href="{{unsubscribe_url}}" data-mce-href="{{unsubscribe_url}}">отказаться от рассылки.</a></span></p>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>
"""
msg = MIMEMultipart()

msg['Subject'] = topic
msg['From'] = login
body = message
msg.attach(MIMEText(body,'html'))

server = root.SMTP_SSL(url, 465)
server.login(login,password)
server.sendmail(login,toaddr,msg.as_string())