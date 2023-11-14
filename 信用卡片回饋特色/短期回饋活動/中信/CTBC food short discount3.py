import csv
from bs4 import BeautifulSoup

html = """
    <div class="twrbo-l-result__data">
            <div class="twrbo-l-resultList" data-list-id="creditcard" ng-show="isDealListSuccess &amp;&amp; dealList.totalDataRows > 0 ">
                
                <!-- ngRepeat: dealItem in dealList.promotionDetailList --><div ng-repeat="dealItem in dealList.promotionDetailList" class="twrbo-l-productCard twrbo-l-productCard--list ng-scope">
                    <div class="twrbo-l-productCard__thumb">
                        <span class="twrbo-c-thumb picturefill-background" style="background-image: url(&quot;/content/dam/twrbo/images/creditcard/offer/F202310.jpg&quot;); background-size: cover; background-repeat: no-repeat; background-position: 50% 50%;">
                            <span data-src="/content/dam/twrbo/images/creditcard/offer/F202310.jpg" data-src-default="/content/dam/twrbo/images/matchCard.png"></span>
                        </span>
                        <div class="twrbo-h-gutters-out-sm-v">
                            <ul class="twrbo-c-label twrbo-c-label--trim">
                                <li ng-show="dealItem.promTag != ''">
                                    <ul class="twrbo-c-label twrbo-c-label--promo twrbo-c-label--trim">
                                        <li>
                                            <i class="twrbo-c-iLabel twrbo-c-iLabel--fire"></i>
                                            <span ng-bind="dealItem.promTag" class="ng-binding">熱門</span>
                                        </li>
                                    </ul>
                                </li>
                                <!-- ngRepeat: tag in dealItem.C --><li ng-repeat="tag in dealItem.C" ng-show="dealItem.hasOwnProperty('C')" class="ng-scope">
                                    <a ng-click="onTagClick(tag.filterItemKey, tag.filterItemName)">
                                        <sapn ng-bind="tag.filterItemName" class="ng-binding">折扣優惠</sapn></a>
                                </li><!-- end ngRepeat: tag in dealItem.C -->
                            </ul>
                        </div>
                    </div>
                    <div class="twrbo-l-productCard__text">
                        <div class="twrbo-h-margin-bottom-md">
                            <span class="twrbo-c-h3 twrbo-c-link twrbo-c-link--ignoreEffect">
                                <span ng-bind="dealItem.name" class="ng-binding">勝博殿</span>
                            </span>
                        </div>
                        <div class="twrbo-l-productTextCard">
                            <div class="twrbo-l-productTextCard__detail">
                                <p><span ng-bind-html="dealItem.promDesc" class="ng-binding">最高現折100元</span></p>
                                <div class="twrbo-h-margin-top-sm">
                                    <ul class="twrbo-c-list twrbo-c-list--data twrbo-c-list--small twrbo-c-list--small">
                                        <li ng-show="dealItem.startDay != '' &amp;&amp; dealItem.endDay != ''">
                                            <div class="twrbo-c-additionalicon">
                                                <img src="/content/dam/twrbo/images/icon/icon_clock_dark.svg" alt="" width="16" height="16">
                                                <span ng-bind="dealItem.startDay" class="ng-binding">2023/01/01</span>
                                                <span>~</span>
                                                <span ng-bind="dealItem.endDay" class="ng-binding">2023/12/31</span>
                                            </div>
                                        </li>
                                        <li ng-show="dealItem.hasOwnProperty('B') &amp;&amp; dealItem.B.length > 0" class="ng-hide">
                                            <div class="twrbo-c-additionalicon">
                                                <img src="/content/dam/twrbo/images/icon/icon_card_dark.svg" alt="" width="16" height="16">
                                                <span>適用
                                                    <!-- ngRepeat: card in dealItem.B -->
                                                </span>
                                            </div>
                                        </li>
                                        <li>
                                            <ul class="twrbo-l-listHorizontal twrbo-l-listHorizontal--additional twrbo-c-fSmall">
                                                <li ng-show="dealItem.phone != ''" class="ng-hide">
                                                    <div class="twrbo-c-additionalicon">
                                                        <img src="/content/dam/twrbo/images/icon/icon_phone_dark.svg" alt="" width="16" height="16">
                                                        <a ng-href="tel:" target="_parent" class="twrbo-h-linkEffect-url--gy twrbo-c-link--tel" href="tel:">
                                                            <span ng-bind="dealItem.phone" class="ng-binding"></span>
                                                        </a>
                                                    </div>
                                                </li>
                                                <li ng-show="dealItem.address != ''" class="ng-hide">
                                                    <div class="twrbo-c-additionalicon">
                                                        <img src="/content/dam/twrbo/images/icon/icon_location_dark.svg" alt="" width="16" height="16">
                                                        <a ng-click="clickPopup(dealItem.promId, dealItem.name, dealItem.promDesc, dealItem.address, dealItem.lng, dealItem.lat, dealItem.phone)" class="twrbo-h-linkEffect-url--gy">
                                                            <span>地址</span>
                                                        </a>
                                                    </div>
                                                </li>
                                                <li ng-show="dealItem.storeUrl != ''" class="ng-hide">
                                                    <div class="twrbo-c-additionalicon">
                                                        <img src="/content/dam/twrbo/images/icon/icon_global_dark.svg" alt="" width="16" height="16">
                                                        <a ng-href="" class="twrbo-h-linkEffect-url--gy">
                                                            <span>網址</span>
                                                        </a>
                                                    </div>
                                                </li>
                                                <li ng-show="dealItem.promUrl != ''">
                                                    <div class="twrbo-c-additionalicon">
                                                        <img src="/content/dam/twrbo/images/icon/icon_link_dark.svg" alt="" width="16" height="16">
                                                        <a ng-href="https://www.ctbcbank.com/content/dam/minisite/long/creditcard/foodsedm/index.html" class="twrbo-h-linkEffect-url--gy" href="https://www.ctbcbank.com/content/dam/minisite/long/creditcard/foodsedm/index.html">
                                                            <span>活動網頁</span>
                                                        </a>
                                                    </div>
                                                </li>
                                                <li ng-show="dealItem.notice != ''">
                                                    <div class="twrbo-c-additionalicon">
                                                        <img src="/content/dam/twrbo/images/icon/icon_notice_dark.svg" alt="" width="16" height="16">
                                                        <a ng-click="noticePopup(dealItem.notice)" class="twrbo-h-linkEffect-url--gy">
                                                            <span>注意事項</span>
                                                        </a>
                                                    </div>
                                                </li>
                                            </ul>
                                        </li>
                                    </ul>
                                </div>
                            </div>
                        </div>
                    </div>
                </div><!-- end ngRepeat: dealItem in dealList.promotionDetailList --><div ng-repeat="dealItem in dealList.promotionDetailList" class="twrbo-l-productCard twrbo-l-productCard--list ng-scope">
                    <div class="twrbo-l-productCard__thumb">
                        <span class="twrbo-c-thumb picturefill-background" style="background-image: url(&quot;/content/dam/twrbo/images/creditcard/offer/F202311.jpg&quot;); background-size: cover; background-repeat: no-repeat; background-position: 50% 50%;">
                            <span data-src="/content/dam/twrbo/images/creditcard/offer/F202311.jpg" data-src-default="/content/dam/twrbo/images/matchCard.png"></span>
                        </span>
                        <div class="twrbo-h-gutters-out-sm-v">
                            <ul class="twrbo-c-label twrbo-c-label--trim">
                                <li ng-show="dealItem.promTag != ''">
                                    <ul class="twrbo-c-label twrbo-c-label--promo twrbo-c-label--trim">
                                        <li>
                                            <i class="twrbo-c-iLabel twrbo-c-iLabel--fire"></i>
                                            <span ng-bind="dealItem.promTag" class="ng-binding">熱門</span>
                                        </li>
                                    </ul>
                                </li>
                                <!-- ngRepeat: tag in dealItem.C --><li ng-repeat="tag in dealItem.C" ng-show="dealItem.hasOwnProperty('C')" class="ng-scope">
                                    <a ng-click="onTagClick(tag.filterItemKey, tag.filterItemName)">
                                        <sapn ng-bind="tag.filterItemName" class="ng-binding">滿額送菜</sapn></a>
                                </li><!-- end ngRepeat: tag in dealItem.C -->
                            </ul>
                        </div>
                    </div>
                    <div class="twrbo-l-productCard__text">
                        <div class="twrbo-h-margin-bottom-md">
                            <span class="twrbo-c-h3 twrbo-c-link twrbo-c-link--ignoreEffect">
                                <span ng-bind="dealItem.name" class="ng-binding">姜滿堂</span>
                            </span>
                        </div>
                        <div class="twrbo-l-productTextCard">
                            <div class="twrbo-l-productTextCard__detail">
                                <p><span ng-bind-html="dealItem.promDesc" class="ng-binding">贈「薄燒豬五花」</span></p>
                                <div class="twrbo-h-margin-top-sm">
                                    <ul class="twrbo-c-list twrbo-c-list--data twrbo-c-list--small twrbo-c-list--small">
                                        <li ng-show="dealItem.startDay != '' &amp;&amp; dealItem.endDay != ''">
                                            <div class="twrbo-c-additionalicon">
                                                <img src="/content/dam/twrbo/images/icon/icon_clock_dark.svg" alt="" width="16" height="16">
                                                <span ng-bind="dealItem.startDay" class="ng-binding">2023/01/01</span>
                                                <span>~</span>
                                                <span ng-bind="dealItem.endDay" class="ng-binding">2023/12/31</span>
                                            </div>
                                        </li>
                                        <li ng-show="dealItem.hasOwnProperty('B') &amp;&amp; dealItem.B.length > 0" class="ng-hide">
                                            <div class="twrbo-c-additionalicon">
                                                <img src="/content/dam/twrbo/images/icon/icon_card_dark.svg" alt="" width="16" height="16">
                                                <span>適用
                                                    <!-- ngRepeat: card in dealItem.B -->
                                                </span>
                                            </div>
                                        </li>
                                        <li>
                                            <ul class="twrbo-l-listHorizontal twrbo-l-listHorizontal--additional twrbo-c-fSmall">
                                                <li ng-show="dealItem.phone != ''" class="ng-hide">
                                                    <div class="twrbo-c-additionalicon">
                                                        <img src="/content/dam/twrbo/images/icon/icon_phone_dark.svg" alt="" width="16" height="16">
                                                        <a ng-href="tel:" target="_parent" class="twrbo-h-linkEffect-url--gy twrbo-c-link--tel" href="tel:">
                                                            <span ng-bind="dealItem.phone" class="ng-binding"></span>
                                                        </a>
                                                    </div>
                                                </li>
                                                <li ng-show="dealItem.address != ''" class="ng-hide">
                                                    <div class="twrbo-c-additionalicon">
                                                        <img src="/content/dam/twrbo/images/icon/icon_location_dark.svg" alt="" width="16" height="16">
                                                        <a ng-click="clickPopup(dealItem.promId, dealItem.name, dealItem.promDesc, dealItem.address, dealItem.lng, dealItem.lat, dealItem.phone)" class="twrbo-h-linkEffect-url--gy">
                                                            <span>地址</span>
                                                        </a>
                                                    </div>
                                                </li>
                                                <li ng-show="dealItem.storeUrl != ''" class="ng-hide">
                                                    <div class="twrbo-c-additionalicon">
                                                        <img src="/content/dam/twrbo/images/icon/icon_global_dark.svg" alt="" width="16" height="16">
                                                        <a ng-href="" class="twrbo-h-linkEffect-url--gy">
                                                            <span>網址</span>
                                                        </a>
                                                    </div>
                                                </li>
                                                <li ng-show="dealItem.promUrl != ''">
                                                    <div class="twrbo-c-additionalicon">
                                                        <img src="/content/dam/twrbo/images/icon/icon_link_dark.svg" alt="" width="16" height="16">
                                                        <a ng-href="https://www.ctbcbank.com/content/dam/minisite/long/creditcard/foodsedm/index.html" class="twrbo-h-linkEffect-url--gy" href="https://www.ctbcbank.com/content/dam/minisite/long/creditcard/foodsedm/index.html">
                                                            <span>活動網頁</span>
                                                        </a>
                                                    </div>
                                                </li>
                                                <li ng-show="dealItem.notice != ''">
                                                    <div class="twrbo-c-additionalicon">
                                                        <img src="/content/dam/twrbo/images/icon/icon_notice_dark.svg" alt="" width="16" height="16">
                                                        <a ng-click="noticePopup(dealItem.notice)" class="twrbo-h-linkEffect-url--gy">
                                                            <span>注意事項</span>
                                                        </a>
                                                    </div>
                                                </li>
                                            </ul>
                                        </li>
                                    </ul>
                                </div>
                            </div>
                        </div>
                    </div>
                </div><!-- end ngRepeat: dealItem in dealList.promotionDetailList --><div ng-repeat="dealItem in dealList.promotionDetailList" class="twrbo-l-productCard twrbo-l-productCard--list ng-scope">
                    <div class="twrbo-l-productCard__thumb">
                        <span class="twrbo-c-thumb picturefill-background" style="background-image: url(&quot;/content/dam/twrbo/images/creditcard/offer/F202312.jpg&quot;); background-size: cover; background-repeat: no-repeat; background-position: 50% 50%;">
                            <span data-src="/content/dam/twrbo/images/creditcard/offer/F202312.jpg" data-src-default="/content/dam/twrbo/images/matchCard.png"></span>
                        </span>
                        <div class="twrbo-h-gutters-out-sm-v">
                            <ul class="twrbo-c-label twrbo-c-label--trim">
                                <li ng-show="dealItem.promTag != ''">
                                    <ul class="twrbo-c-label twrbo-c-label--promo twrbo-c-label--trim">
                                        <li>
                                            <i class="twrbo-c-iLabel twrbo-c-iLabel--fire"></i>
                                            <span ng-bind="dealItem.promTag" class="ng-binding">熱門</span>
                                        </li>
                                    </ul>
                                </li>
                                <!-- ngRepeat: tag in dealItem.C --><li ng-repeat="tag in dealItem.C" ng-show="dealItem.hasOwnProperty('C')" class="ng-scope">
                                    <a ng-click="onTagClick(tag.filterItemKey, tag.filterItemName)">
                                        <sapn ng-bind="tag.filterItemName" class="ng-binding">滿額送菜</sapn></a>
                                </li><!-- end ngRepeat: tag in dealItem.C -->
                            </ul>
                        </div>
                    </div>
                    <div class="twrbo-l-productCard__text">
                        <div class="twrbo-h-margin-bottom-md">
                            <span class="twrbo-c-h3 twrbo-c-link twrbo-c-link--ignoreEffect">
                                <span ng-bind="dealItem.name" class="ng-binding">涓豆腐</span>
                            </span>
                        </div>
                        <div class="twrbo-l-productTextCard">
                            <div class="twrbo-l-productTextCard__detail">
                                <p><span ng-bind-html="dealItem.promDesc" class="ng-binding">贈「黃金酥炸嫩豆腐」</span></p>
                                <div class="twrbo-h-margin-top-sm">
                                    <ul class="twrbo-c-list twrbo-c-list--data twrbo-c-list--small twrbo-c-list--small">
                                        <li ng-show="dealItem.startDay != '' &amp;&amp; dealItem.endDay != ''">
                                            <div class="twrbo-c-additionalicon">
                                                <img src="/content/dam/twrbo/images/icon/icon_clock_dark.svg" alt="" width="16" height="16">
                                                <span ng-bind="dealItem.startDay" class="ng-binding">2023/01/01</span>
                                                <span>~</span>
                                                <span ng-bind="dealItem.endDay" class="ng-binding">2023/12/31</span>
                                            </div>
                                        </li>
                                        <li ng-show="dealItem.hasOwnProperty('B') &amp;&amp; dealItem.B.length > 0" class="ng-hide">
                                            <div class="twrbo-c-additionalicon">
                                                <img src="/content/dam/twrbo/images/icon/icon_card_dark.svg" alt="" width="16" height="16">
                                                <span>適用
                                                    <!-- ngRepeat: card in dealItem.B -->
                                                </span>
                                            </div>
                                        </li>
                                        <li>
                                            <ul class="twrbo-l-listHorizontal twrbo-l-listHorizontal--additional twrbo-c-fSmall">
                                                <li ng-show="dealItem.phone != ''" class="ng-hide">
                                                    <div class="twrbo-c-additionalicon">
                                                        <img src="/content/dam/twrbo/images/icon/icon_phone_dark.svg" alt="" width="16" height="16">
                                                        <a ng-href="tel:" target="_parent" class="twrbo-h-linkEffect-url--gy twrbo-c-link--tel" href="tel:">
                                                            <span ng-bind="dealItem.phone" class="ng-binding"></span>
                                                        </a>
                                                    </div>
                                                </li>
                                                <li ng-show="dealItem.address != ''" class="ng-hide">
                                                    <div class="twrbo-c-additionalicon">
                                                        <img src="/content/dam/twrbo/images/icon/icon_location_dark.svg" alt="" width="16" height="16">
                                                        <a ng-click="clickPopup(dealItem.promId, dealItem.name, dealItem.promDesc, dealItem.address, dealItem.lng, dealItem.lat, dealItem.phone)" class="twrbo-h-linkEffect-url--gy">
                                                            <span>地址</span>
                                                        </a>
                                                    </div>
                                                </li>
                                                <li ng-show="dealItem.storeUrl != ''" class="ng-hide">
                                                    <div class="twrbo-c-additionalicon">
                                                        <img src="/content/dam/twrbo/images/icon/icon_global_dark.svg" alt="" width="16" height="16">
                                                        <a ng-href="" class="twrbo-h-linkEffect-url--gy">
                                                            <span>網址</span>
                                                        </a>
                                                    </div>
                                                </li>
                                                <li ng-show="dealItem.promUrl != ''">
                                                    <div class="twrbo-c-additionalicon">
                                                        <img src="/content/dam/twrbo/images/icon/icon_link_dark.svg" alt="" width="16" height="16">
                                                        <a ng-href="https://www.ctbcbank.com/content/dam/minisite/long/creditcard/foodsedm/index.html" class="twrbo-h-linkEffect-url--gy" href="https://www.ctbcbank.com/content/dam/minisite/long/creditcard/foodsedm/index.html">
                                                            <span>活動網頁</span>
                                                        </a>
                                                    </div>
                                                </li>
                                                <li ng-show="dealItem.notice != ''">
                                                    <div class="twrbo-c-additionalicon">
                                                        <img src="/content/dam/twrbo/images/icon/icon_notice_dark.svg" alt="" width="16" height="16">
                                                        <a ng-click="noticePopup(dealItem.notice)" class="twrbo-h-linkEffect-url--gy">
                                                            <span>注意事項</span>
                                                        </a>
                                                    </div>
                                                </li>
                                            </ul>
                                        </li>
                                    </ul>
                                </div>
                            </div>
                        </div>
                    </div>
                </div><!-- end ngRepeat: dealItem in dealList.promotionDetailList --><div ng-repeat="dealItem in dealList.promotionDetailList" class="twrbo-l-productCard twrbo-l-productCard--list ng-scope">
                    <div class="twrbo-l-productCard__thumb">
                        <span class="twrbo-c-thumb picturefill-background" style="background-image: url(&quot;/content/dam/twrbo/images/creditcard/offer/F202313.jpg&quot;); background-size: cover; background-repeat: no-repeat; background-position: 50% 50%;">
                            <span data-src="/content/dam/twrbo/images/creditcard/offer/F202313.jpg" data-src-default="/content/dam/twrbo/images/matchCard.png"></span>
                        </span>
                        <div class="twrbo-h-gutters-out-sm-v">
                            <ul class="twrbo-c-label twrbo-c-label--trim">
                                <li ng-show="dealItem.promTag != ''">
                                    <ul class="twrbo-c-label twrbo-c-label--promo twrbo-c-label--trim">
                                        <li>
                                            <i class="twrbo-c-iLabel twrbo-c-iLabel--fire"></i>
                                            <span ng-bind="dealItem.promTag" class="ng-binding">熱門</span>
                                        </li>
                                    </ul>
                                </li>
                                <!-- ngRepeat: tag in dealItem.C --><li ng-repeat="tag in dealItem.C" ng-show="dealItem.hasOwnProperty('C')" class="ng-scope">
                                    <a ng-click="onTagClick(tag.filterItemKey, tag.filterItemName)">
                                        <sapn ng-bind="tag.filterItemName" class="ng-binding">滿額送菜</sapn></a>
                                </li><!-- end ngRepeat: tag in dealItem.C -->
                            </ul>
                        </div>
                    </div>
                    <div class="twrbo-l-productCard__text">
                        <div class="twrbo-h-margin-bottom-md">
                            <span class="twrbo-c-h3 twrbo-c-link twrbo-c-link--ignoreEffect">
                                <span ng-bind="dealItem.name" class="ng-binding">北村豆腐家</span>
                            </span>
                        </div>
                        <div class="twrbo-l-productTextCard">
                            <div class="twrbo-l-productTextCard__detail">
                                <p><span ng-bind-html="dealItem.promDesc" class="ng-binding">贈「首爾韓式炸雞年糕」</span></p>
                                <div class="twrbo-h-margin-top-sm">
                                    <ul class="twrbo-c-list twrbo-c-list--data twrbo-c-list--small twrbo-c-list--small">
                                        <li ng-show="dealItem.startDay != '' &amp;&amp; dealItem.endDay != ''">
                                            <div class="twrbo-c-additionalicon">
                                                <img src="/content/dam/twrbo/images/icon/icon_clock_dark.svg" alt="" width="16" height="16">
                                                <span ng-bind="dealItem.startDay" class="ng-binding">2023/01/01</span>
                                                <span>~</span>
                                                <span ng-bind="dealItem.endDay" class="ng-binding">2023/12/31</span>
                                            </div>
                                        </li>
                                        <li ng-show="dealItem.hasOwnProperty('B') &amp;&amp; dealItem.B.length > 0" class="ng-hide">
                                            <div class="twrbo-c-additionalicon">
                                                <img src="/content/dam/twrbo/images/icon/icon_card_dark.svg" alt="" width="16" height="16">
                                                <span>適用
                                                    <!-- ngRepeat: card in dealItem.B -->
                                                </span>
                                            </div>
                                        </li>
                                        <li>
                                            <ul class="twrbo-l-listHorizontal twrbo-l-listHorizontal--additional twrbo-c-fSmall">
                                                <li ng-show="dealItem.phone != ''" class="ng-hide">
                                                    <div class="twrbo-c-additionalicon">
                                                        <img src="/content/dam/twrbo/images/icon/icon_phone_dark.svg" alt="" width="16" height="16">
                                                        <a ng-href="tel:" target="_parent" class="twrbo-h-linkEffect-url--gy twrbo-c-link--tel" href="tel:">
                                                            <span ng-bind="dealItem.phone" class="ng-binding"></span>
                                                        </a>
                                                    </div>
                                                </li>
                                                <li ng-show="dealItem.address != ''" class="ng-hide">
                                                    <div class="twrbo-c-additionalicon">
                                                        <img src="/content/dam/twrbo/images/icon/icon_location_dark.svg" alt="" width="16" height="16">
                                                        <a ng-click="clickPopup(dealItem.promId, dealItem.name, dealItem.promDesc, dealItem.address, dealItem.lng, dealItem.lat, dealItem.phone)" class="twrbo-h-linkEffect-url--gy">
                                                            <span>地址</span>
                                                        </a>
                                                    </div>
                                                </li>
                                                <li ng-show="dealItem.storeUrl != ''" class="ng-hide">
                                                    <div class="twrbo-c-additionalicon">
                                                        <img src="/content/dam/twrbo/images/icon/icon_global_dark.svg" alt="" width="16" height="16">
                                                        <a ng-href="" class="twrbo-h-linkEffect-url--gy">
                                                            <span>網址</span>
                                                        </a>
                                                    </div>
                                                </li>
                                                <li ng-show="dealItem.promUrl != ''">
                                                    <div class="twrbo-c-additionalicon">
                                                        <img src="/content/dam/twrbo/images/icon/icon_link_dark.svg" alt="" width="16" height="16">
                                                        <a ng-href="https://www.ctbcbank.com/content/dam/minisite/long/creditcard/foodsedm/index.html" class="twrbo-h-linkEffect-url--gy" href="https://www.ctbcbank.com/content/dam/minisite/long/creditcard/foodsedm/index.html">
                                                            <span>活動網頁</span>
                                                        </a>
                                                    </div>
                                                </li>
                                                <li ng-show="dealItem.notice != ''">
                                                    <div class="twrbo-c-additionalicon">
                                                        <img src="/content/dam/twrbo/images/icon/icon_notice_dark.svg" alt="" width="16" height="16">
                                                        <a ng-click="noticePopup(dealItem.notice)" class="twrbo-h-linkEffect-url--gy">
                                                            <span>注意事項</span>
                                                        </a>
                                                    </div>
                                                </li>
                                            </ul>
                                        </li>
                                    </ul>
                                </div>
                            </div>
                        </div>
                    </div>
                </div><!-- end ngRepeat: dealItem in dealList.promotionDetailList --><div ng-repeat="dealItem in dealList.promotionDetailList" class="twrbo-l-productCard twrbo-l-productCard--list ng-scope">
                    <div class="twrbo-l-productCard__thumb">
                        <span class="twrbo-c-thumb picturefill-background" style="background-image: url(&quot;/content/dam/twrbo/images/creditcard/offer/F202314.jpg&quot;); background-size: cover; background-repeat: no-repeat; background-position: 50% 50%;">
                            <span data-src="/content/dam/twrbo/images/creditcard/offer/F202314.jpg" data-src-default="/content/dam/twrbo/images/matchCard.png"></span>
                        </span>
                        <div class="twrbo-h-gutters-out-sm-v">
                            <ul class="twrbo-c-label twrbo-c-label--trim">
                                <li ng-show="dealItem.promTag != ''">
                                    <ul class="twrbo-c-label twrbo-c-label--promo twrbo-c-label--trim">
                                        <li>
                                            <i class="twrbo-c-iLabel twrbo-c-iLabel--fire"></i>
                                            <span ng-bind="dealItem.promTag" class="ng-binding">熱門</span>
                                        </li>
                                    </ul>
                                </li>
                                <!-- ngRepeat: tag in dealItem.C --><li ng-repeat="tag in dealItem.C" ng-show="dealItem.hasOwnProperty('C')" class="ng-scope">
                                    <a ng-click="onTagClick(tag.filterItemKey, tag.filterItemName)">
                                        <sapn ng-bind="tag.filterItemName" class="ng-binding">折扣優惠</sapn></a>
                                </li><!-- end ngRepeat: tag in dealItem.C -->
                            </ul>
                        </div>
                    </div>
                    <div class="twrbo-l-productCard__text">
                        <div class="twrbo-h-margin-bottom-md">
                            <span class="twrbo-c-h3 twrbo-c-link twrbo-c-link--ignoreEffect">
                                <span ng-bind="dealItem.name" class="ng-binding">銅盤嚴選韓式烤肉</span>
                            </span>
                        </div>
                        <div class="twrbo-l-productTextCard">
                            <div class="twrbo-l-productTextCard__detail">
                                <p><span ng-bind-html="dealItem.promDesc" class="ng-binding">享95折優惠</span></p>
                                <div class="twrbo-h-margin-top-sm">
                                    <ul class="twrbo-c-list twrbo-c-list--data twrbo-c-list--small twrbo-c-list--small">
                                        <li ng-show="dealItem.startDay != '' &amp;&amp; dealItem.endDay != ''">
                                            <div class="twrbo-c-additionalicon">
                                                <img src="/content/dam/twrbo/images/icon/icon_clock_dark.svg" alt="" width="16" height="16">
                                                <span ng-bind="dealItem.startDay" class="ng-binding">2023/01/01</span>
                                                <span>~</span>
                                                <span ng-bind="dealItem.endDay" class="ng-binding">2023/12/31</span>
                                            </div>
                                        </li>
                                        <li ng-show="dealItem.hasOwnProperty('B') &amp;&amp; dealItem.B.length > 0" class="ng-hide">
                                            <div class="twrbo-c-additionalicon">
                                                <img src="/content/dam/twrbo/images/icon/icon_card_dark.svg" alt="" width="16" height="16">
                                                <span>適用
                                                    <!-- ngRepeat: card in dealItem.B -->
                                                </span>
                                            </div>
                                        </li>
                                        <li>
                                            <ul class="twrbo-l-listHorizontal twrbo-l-listHorizontal--additional twrbo-c-fSmall">
                                                <li ng-show="dealItem.phone != ''" class="ng-hide">
                                                    <div class="twrbo-c-additionalicon">
                                                        <img src="/content/dam/twrbo/images/icon/icon_phone_dark.svg" alt="" width="16" height="16">
                                                        <a ng-href="tel:" target="_parent" class="twrbo-h-linkEffect-url--gy twrbo-c-link--tel" href="tel:">
                                                            <span ng-bind="dealItem.phone" class="ng-binding"></span>
                                                        </a>
                                                    </div>
                                                </li>
                                                <li ng-show="dealItem.address != ''" class="ng-hide">
                                                    <div class="twrbo-c-additionalicon">
                                                        <img src="/content/dam/twrbo/images/icon/icon_location_dark.svg" alt="" width="16" height="16">
                                                        <a ng-click="clickPopup(dealItem.promId, dealItem.name, dealItem.promDesc, dealItem.address, dealItem.lng, dealItem.lat, dealItem.phone)" class="twrbo-h-linkEffect-url--gy">
                                                            <span>地址</span>
                                                        </a>
                                                    </div>
                                                </li>
                                                <li ng-show="dealItem.storeUrl != ''" class="ng-hide">
                                                    <div class="twrbo-c-additionalicon">
                                                        <img src="/content/dam/twrbo/images/icon/icon_global_dark.svg" alt="" width="16" height="16">
                                                        <a ng-href="" class="twrbo-h-linkEffect-url--gy">
                                                            <span>網址</span>
                                                        </a>
                                                    </div>
                                                </li>
                                                <li ng-show="dealItem.promUrl != ''">
                                                    <div class="twrbo-c-additionalicon">
                                                        <img src="/content/dam/twrbo/images/icon/icon_link_dark.svg" alt="" width="16" height="16">
                                                        <a ng-href="https://www.ctbcbank.com/content/dam/minisite/long/creditcard/foodsedm/index.html" class="twrbo-h-linkEffect-url--gy" href="https://www.ctbcbank.com/content/dam/minisite/long/creditcard/foodsedm/index.html">
                                                            <span>活動網頁</span>
                                                        </a>
                                                    </div>
                                                </li>
                                                <li ng-show="dealItem.notice != ''">
                                                    <div class="twrbo-c-additionalicon">
                                                        <img src="/content/dam/twrbo/images/icon/icon_notice_dark.svg" alt="" width="16" height="16">
                                                        <a ng-click="noticePopup(dealItem.notice)" class="twrbo-h-linkEffect-url--gy">
                                                            <span>注意事項</span>
                                                        </a>
                                                    </div>
                                                </li>
                                            </ul>
                                        </li>
                                    </ul>
                                </div>
                            </div>
                        </div>
                    </div>
                </div><!-- end ngRepeat: dealItem in dealList.promotionDetailList --><div ng-repeat="dealItem in dealList.promotionDetailList" class="twrbo-l-productCard twrbo-l-productCard--list ng-scope">
                    <div class="twrbo-l-productCard__thumb">
                        <span class="twrbo-c-thumb picturefill-background" style="background-image: url(&quot;/content/dam/twrbo/images/creditcard/offer/F202315.jpg&quot;); background-size: cover; background-repeat: no-repeat; background-position: 50% 50%;">
                            <span data-src="/content/dam/twrbo/images/creditcard/offer/F202315.jpg" data-src-default="/content/dam/twrbo/images/matchCard.png"></span>
                        </span>
                        <div class="twrbo-h-gutters-out-sm-v">
                            <ul class="twrbo-c-label twrbo-c-label--trim">
                                <li ng-show="dealItem.promTag != ''">
                                    <ul class="twrbo-c-label twrbo-c-label--promo twrbo-c-label--trim">
                                        <li>
                                            <i class="twrbo-c-iLabel twrbo-c-iLabel--fire"></i>
                                            <span ng-bind="dealItem.promTag" class="ng-binding">熱門</span>
                                        </li>
                                    </ul>
                                </li>
                                <!-- ngRepeat: tag in dealItem.C --><li ng-repeat="tag in dealItem.C" ng-show="dealItem.hasOwnProperty('C')" class="ng-scope">
                                    <a ng-click="onTagClick(tag.filterItemKey, tag.filterItemName)">
                                        <sapn ng-bind="tag.filterItemName" class="ng-binding">折扣優惠</sapn></a>
                                </li><!-- end ngRepeat: tag in dealItem.C -->
                            </ul>
                        </div>
                    </div>
                    <div class="twrbo-l-productCard__text">
                        <div class="twrbo-h-margin-bottom-md">
                            <span class="twrbo-c-h3 twrbo-c-link twrbo-c-link--ignoreEffect">
                                <span ng-bind="dealItem.name" class="ng-binding">釜山宗家</span>
                            </span>
                        </div>
                        <div class="twrbo-l-productTextCard">
                            <div class="twrbo-l-productTextCard__detail">
                                <p><span ng-bind-html="dealItem.promDesc" class="ng-binding">享95折優惠</span></p>
                                <div class="twrbo-h-margin-top-sm">
                                    <ul class="twrbo-c-list twrbo-c-list--data twrbo-c-list--small twrbo-c-list--small">
                                        <li ng-show="dealItem.startDay != '' &amp;&amp; dealItem.endDay != ''">
                                            <div class="twrbo-c-additionalicon">
                                                <img src="/content/dam/twrbo/images/icon/icon_clock_dark.svg" alt="" width="16" height="16">
                                                <span ng-bind="dealItem.startDay" class="ng-binding">2023/01/01</span>
                                                <span>~</span>
                                                <span ng-bind="dealItem.endDay" class="ng-binding">2023/12/31</span>
                                            </div>
                                        </li>
                                        <li ng-show="dealItem.hasOwnProperty('B') &amp;&amp; dealItem.B.length > 0" class="ng-hide">
                                            <div class="twrbo-c-additionalicon">
                                                <img src="/content/dam/twrbo/images/icon/icon_card_dark.svg" alt="" width="16" height="16">
                                                <span>適用
                                                    <!-- ngRepeat: card in dealItem.B -->
                                                </span>
                                            </div>
                                        </li>
                                        <li>
                                            <ul class="twrbo-l-listHorizontal twrbo-l-listHorizontal--additional twrbo-c-fSmall">
                                                <li ng-show="dealItem.phone != ''" class="ng-hide">
                                                    <div class="twrbo-c-additionalicon">
                                                        <img src="/content/dam/twrbo/images/icon/icon_phone_dark.svg" alt="" width="16" height="16">
                                                        <a ng-href="tel:" target="_parent" class="twrbo-h-linkEffect-url--gy twrbo-c-link--tel" href="tel:">
                                                            <span ng-bind="dealItem.phone" class="ng-binding"></span>
                                                        </a>
                                                    </div>
                                                </li>
                                                <li ng-show="dealItem.address != ''" class="ng-hide">
                                                    <div class="twrbo-c-additionalicon">
                                                        <img src="/content/dam/twrbo/images/icon/icon_location_dark.svg" alt="" width="16" height="16">
                                                        <a ng-click="clickPopup(dealItem.promId, dealItem.name, dealItem.promDesc, dealItem.address, dealItem.lng, dealItem.lat, dealItem.phone)" class="twrbo-h-linkEffect-url--gy">
                                                            <span>地址</span>
                                                        </a>
                                                    </div>
                                                </li>
                                                <li ng-show="dealItem.storeUrl != ''" class="ng-hide">
                                                    <div class="twrbo-c-additionalicon">
                                                        <img src="/content/dam/twrbo/images/icon/icon_global_dark.svg" alt="" width="16" height="16">
                                                        <a ng-href="" class="twrbo-h-linkEffect-url--gy">
                                                            <span>網址</span>
                                                        </a>
                                                    </div>
                                                </li>
                                                <li ng-show="dealItem.promUrl != ''">
                                                    <div class="twrbo-c-additionalicon">
                                                        <img src="/content/dam/twrbo/images/icon/icon_link_dark.svg" alt="" width="16" height="16">
                                                        <a ng-href="https://www.ctbcbank.com/content/dam/minisite/long/creditcard/foodsedm/index.html" class="twrbo-h-linkEffect-url--gy" href="https://www.ctbcbank.com/content/dam/minisite/long/creditcard/foodsedm/index.html">
                                                            <span>活動網頁</span>
                                                        </a>
                                                    </div>
                                                </li>
                                                <li ng-show="dealItem.notice != ''">
                                                    <div class="twrbo-c-additionalicon">
                                                        <img src="/content/dam/twrbo/images/icon/icon_notice_dark.svg" alt="" width="16" height="16">
                                                        <a ng-click="noticePopup(dealItem.notice)" class="twrbo-h-linkEffect-url--gy">
                                                            <span>注意事項</span>
                                                        </a>
                                                    </div>
                                                </li>
                                            </ul>
                                        </li>
                                    </ul>
                                </div>
                            </div>
                        </div>
                    </div>
                </div><!-- end ngRepeat: dealItem in dealList.promotionDetailList --><div ng-repeat="dealItem in dealList.promotionDetailList" class="twrbo-l-productCard twrbo-l-productCard--list ng-scope">
                    <div class="twrbo-l-productCard__thumb">
                        <span class="twrbo-c-thumb picturefill-background" style="background-image: url(&quot;/content/dam/twrbo/images/creditcard/offer/F202316.jpg&quot;); background-size: cover; background-repeat: no-repeat; background-position: 50% 50%;">
                            <span data-src="/content/dam/twrbo/images/creditcard/offer/F202316.jpg" data-src-default="/content/dam/twrbo/images/matchCard.png"></span>
                        </span>
                        <div class="twrbo-h-gutters-out-sm-v">
                            <ul class="twrbo-c-label twrbo-c-label--trim">
                                <li ng-show="dealItem.promTag != ''">
                                    <ul class="twrbo-c-label twrbo-c-label--promo twrbo-c-label--trim">
                                        <li>
                                            <i class="twrbo-c-iLabel twrbo-c-iLabel--fire"></i>
                                            <span ng-bind="dealItem.promTag" class="ng-binding">熱門</span>
                                        </li>
                                    </ul>
                                </li>
                                <!-- ngRepeat: tag in dealItem.C --><li ng-repeat="tag in dealItem.C" ng-show="dealItem.hasOwnProperty('C')" class="ng-scope">
                                    <a ng-click="onTagClick(tag.filterItemKey, tag.filterItemName)">
                                        <sapn ng-bind="tag.filterItemName" class="ng-binding">同行優惠</sapn></a>
                                </li><!-- end ngRepeat: tag in dealItem.C -->
                            </ul>
                        </div>
                    </div>
                    <div class="twrbo-l-productCard__text">
                        <div class="twrbo-h-margin-bottom-md">
                            <span class="twrbo-c-h3 twrbo-c-link twrbo-c-link--ignoreEffect">
                                <span ng-bind="dealItem.name" class="ng-binding">欣葉日本料理</span>
                            </span>
                        </div>
                        <div class="twrbo-l-productTextCard">
                            <div class="twrbo-l-productTextCard__detail">
                                <p><span ng-bind-html="dealItem.promDesc" class="ng-binding">四人同行贈200元</span></p>
                                <div class="twrbo-h-margin-top-sm">
                                    <ul class="twrbo-c-list twrbo-c-list--data twrbo-c-list--small twrbo-c-list--small">
                                        <li ng-show="dealItem.startDay != '' &amp;&amp; dealItem.endDay != ''">
                                            <div class="twrbo-c-additionalicon">
                                                <img src="/content/dam/twrbo/images/icon/icon_clock_dark.svg" alt="" width="16" height="16">
                                                <span ng-bind="dealItem.startDay" class="ng-binding">2023/01/01</span>
                                                <span>~</span>
                                                <span ng-bind="dealItem.endDay" class="ng-binding">2023/12/31</span>
                                            </div>
                                        </li>
                                        <li ng-show="dealItem.hasOwnProperty('B') &amp;&amp; dealItem.B.length > 0" class="ng-hide">
                                            <div class="twrbo-c-additionalicon">
                                                <img src="/content/dam/twrbo/images/icon/icon_card_dark.svg" alt="" width="16" height="16">
                                                <span>適用
                                                    <!-- ngRepeat: card in dealItem.B -->
                                                </span>
                                            </div>
                                        </li>
                                        <li>
                                            <ul class="twrbo-l-listHorizontal twrbo-l-listHorizontal--additional twrbo-c-fSmall">
                                                <li ng-show="dealItem.phone != ''" class="ng-hide">
                                                    <div class="twrbo-c-additionalicon">
                                                        <img src="/content/dam/twrbo/images/icon/icon_phone_dark.svg" alt="" width="16" height="16">
                                                        <a ng-href="tel:" target="_parent" class="twrbo-h-linkEffect-url--gy twrbo-c-link--tel" href="tel:">
                                                            <span ng-bind="dealItem.phone" class="ng-binding"></span>
                                                        </a>
                                                    </div>
                                                </li>
                                                <li ng-show="dealItem.address != ''" class="ng-hide">
                                                    <div class="twrbo-c-additionalicon">
                                                        <img src="/content/dam/twrbo/images/icon/icon_location_dark.svg" alt="" width="16" height="16">
                                                        <a ng-click="clickPopup(dealItem.promId, dealItem.name, dealItem.promDesc, dealItem.address, dealItem.lng, dealItem.lat, dealItem.phone)" class="twrbo-h-linkEffect-url--gy">
                                                            <span>地址</span>
                                                        </a>
                                                    </div>
                                                </li>
                                                <li ng-show="dealItem.storeUrl != ''" class="ng-hide">
                                                    <div class="twrbo-c-additionalicon">
                                                        <img src="/content/dam/twrbo/images/icon/icon_global_dark.svg" alt="" width="16" height="16">
                                                        <a ng-href="" class="twrbo-h-linkEffect-url--gy">
                                                            <span>網址</span>
                                                        </a>
                                                    </div>
                                                </li>
                                                <li ng-show="dealItem.promUrl != ''">
                                                    <div class="twrbo-c-additionalicon">
                                                        <img src="/content/dam/twrbo/images/icon/icon_link_dark.svg" alt="" width="16" height="16">
                                                        <a ng-href="https://www.ctbcbank.com/content/dam/minisite/long/creditcard/foodsedm/index.html" class="twrbo-h-linkEffect-url--gy" href="https://www.ctbcbank.com/content/dam/minisite/long/creditcard/foodsedm/index.html">
                                                            <span>活動網頁</span>
                                                        </a>
                                                    </div>
                                                </li>
                                                <li ng-show="dealItem.notice != ''">
                                                    <div class="twrbo-c-additionalicon">
                                                        <img src="/content/dam/twrbo/images/icon/icon_notice_dark.svg" alt="" width="16" height="16">
                                                        <a ng-click="noticePopup(dealItem.notice)" class="twrbo-h-linkEffect-url--gy">
                                                            <span>注意事項</span>
                                                        </a>
                                                    </div>
                                                </li>
                                            </ul>
                                        </li>
                                    </ul>
                                </div>
                            </div>
                        </div>
                    </div>
                </div><!-- end ngRepeat: dealItem in dealList.promotionDetailList --><div ng-repeat="dealItem in dealList.promotionDetailList" class="twrbo-l-productCard twrbo-l-productCard--list ng-scope">
                    <div class="twrbo-l-productCard__thumb">
                        <span class="twrbo-c-thumb picturefill-background" style="background-image: url(&quot;/content/dam/twrbo/images/creditcard/offer/F202317.jpg&quot;); background-size: cover; background-repeat: no-repeat; background-position: 50% 50%;">
                            <span data-src="/content/dam/twrbo/images/creditcard/offer/F202317.jpg" data-src-default="/content/dam/twrbo/images/matchCard.png"></span>
                        </span>
                        <div class="twrbo-h-gutters-out-sm-v">
                            <ul class="twrbo-c-label twrbo-c-label--trim">
                                <li ng-show="dealItem.promTag != ''">
                                    <ul class="twrbo-c-label twrbo-c-label--promo twrbo-c-label--trim">
                                        <li>
                                            <i class="twrbo-c-iLabel twrbo-c-iLabel--fire"></i>
                                            <span ng-bind="dealItem.promTag" class="ng-binding">熱門</span>
                                        </li>
                                    </ul>
                                </li>
                                <!-- ngRepeat: tag in dealItem.C --><li ng-repeat="tag in dealItem.C" ng-show="dealItem.hasOwnProperty('C')" class="ng-scope">
                                    <a ng-click="onTagClick(tag.filterItemKey, tag.filterItemName)">
                                        <sapn ng-bind="tag.filterItemName" class="ng-binding">滿額送菜</sapn></a>
                                </li><!-- end ngRepeat: tag in dealItem.C -->
                            </ul>
                        </div>
                    </div>
                    <div class="twrbo-l-productCard__text">
                        <div class="twrbo-h-margin-bottom-md">
                            <span class="twrbo-c-h3 twrbo-c-link twrbo-c-link--ignoreEffect">
                                <span ng-bind="dealItem.name" class="ng-binding">欣葉呷哺呷哺</span>
                            </span>
                        </div>
                        <div class="twrbo-l-productTextCard">
                            <div class="twrbo-l-productTextCard__detail">
                                <p><span ng-bind-html="dealItem.promDesc" class="ng-binding">贈【特選豬肉盤】</span></p>
                                <div class="twrbo-h-margin-top-sm">
                                    <ul class="twrbo-c-list twrbo-c-list--data twrbo-c-list--small twrbo-c-list--small">
                                        <li ng-show="dealItem.startDay != '' &amp;&amp; dealItem.endDay != ''">
                                            <div class="twrbo-c-additionalicon">
                                                <img src="/content/dam/twrbo/images/icon/icon_clock_dark.svg" alt="" width="16" height="16">
                                                <span ng-bind="dealItem.startDay" class="ng-binding">2023/01/01</span>
                                                <span>~</span>
                                                <span ng-bind="dealItem.endDay" class="ng-binding">2023/12/31</span>
                                            </div>
                                        </li>
                                        <li ng-show="dealItem.hasOwnProperty('B') &amp;&amp; dealItem.B.length > 0" class="ng-hide">
                                            <div class="twrbo-c-additionalicon">
                                                <img src="/content/dam/twrbo/images/icon/icon_card_dark.svg" alt="" width="16" height="16">
                                                <span>適用
                                                    <!-- ngRepeat: card in dealItem.B -->
                                                </span>
                                            </div>
                                        </li>
                                        <li>
                                            <ul class="twrbo-l-listHorizontal twrbo-l-listHorizontal--additional twrbo-c-fSmall">
                                                <li ng-show="dealItem.phone != ''" class="ng-hide">
                                                    <div class="twrbo-c-additionalicon">
                                                        <img src="/content/dam/twrbo/images/icon/icon_phone_dark.svg" alt="" width="16" height="16">
                                                        <a ng-href="tel:" target="_parent" class="twrbo-h-linkEffect-url--gy twrbo-c-link--tel" href="tel:">
                                                            <span ng-bind="dealItem.phone" class="ng-binding"></span>
                                                        </a>
                                                    </div>
                                                </li>
                                                <li ng-show="dealItem.address != ''" class="ng-hide">
                                                    <div class="twrbo-c-additionalicon">
                                                        <img src="/content/dam/twrbo/images/icon/icon_location_dark.svg" alt="" width="16" height="16">
                                                        <a ng-click="clickPopup(dealItem.promId, dealItem.name, dealItem.promDesc, dealItem.address, dealItem.lng, dealItem.lat, dealItem.phone)" class="twrbo-h-linkEffect-url--gy">
                                                            <span>地址</span>
                                                        </a>
                                                    </div>
                                                </li>
                                                <li ng-show="dealItem.storeUrl != ''" class="ng-hide">
                                                    <div class="twrbo-c-additionalicon">
                                                        <img src="/content/dam/twrbo/images/icon/icon_global_dark.svg" alt="" width="16" height="16">
                                                        <a ng-href="" class="twrbo-h-linkEffect-url--gy">
                                                            <span>網址</span>
                                                        </a>
                                                    </div>
                                                </li>
                                                <li ng-show="dealItem.promUrl != ''">
                                                    <div class="twrbo-c-additionalicon">
                                                        <img src="/content/dam/twrbo/images/icon/icon_link_dark.svg" alt="" width="16" height="16">
                                                        <a ng-href="https://www.ctbcbank.com/content/dam/minisite/long/creditcard/foodsedm/index.html" class="twrbo-h-linkEffect-url--gy" href="https://www.ctbcbank.com/content/dam/minisite/long/creditcard/foodsedm/index.html">
                                                            <span>活動網頁</span>
                                                        </a>
                                                    </div>
                                                </li>
                                                <li ng-show="dealItem.notice != ''">
                                                    <div class="twrbo-c-additionalicon">
                                                        <img src="/content/dam/twrbo/images/icon/icon_notice_dark.svg" alt="" width="16" height="16">
                                                        <a ng-click="noticePopup(dealItem.notice)" class="twrbo-h-linkEffect-url--gy">
                                                            <span>注意事項</span>
                                                        </a>
                                                    </div>
                                                </li>
                                            </ul>
                                        </li>
                                    </ul>
                                </div>
                            </div>
                        </div>
                    </div>
                </div><!-- end ngRepeat: dealItem in dealList.promotionDetailList --><div ng-repeat="dealItem in dealList.promotionDetailList" class="twrbo-l-productCard twrbo-l-productCard--list ng-scope">
                    <div class="twrbo-l-productCard__thumb">
                        <span class="twrbo-c-thumb picturefill-background" style="background-image: url(&quot;/content/dam/twrbo/images/creditcard/offer/F202318.jpg&quot;); background-size: cover; background-repeat: no-repeat; background-position: 50% 50%;">
                            <span data-src="/content/dam/twrbo/images/creditcard/offer/F202318.jpg" data-src-default="/content/dam/twrbo/images/matchCard.png"></span>
                        </span>
                        <div class="twrbo-h-gutters-out-sm-v">
                            <ul class="twrbo-c-label twrbo-c-label--trim">
                                <li ng-show="dealItem.promTag != ''">
                                    <ul class="twrbo-c-label twrbo-c-label--promo twrbo-c-label--trim">
                                        <li>
                                            <i class="twrbo-c-iLabel twrbo-c-iLabel--fire"></i>
                                            <span ng-bind="dealItem.promTag" class="ng-binding">熱門</span>
                                        </li>
                                    </ul>
                                </li>
                                <!-- ngRepeat: tag in dealItem.C --><li ng-repeat="tag in dealItem.C" ng-show="dealItem.hasOwnProperty('C')" class="ng-scope">
                                    <a ng-click="onTagClick(tag.filterItemKey, tag.filterItemName)">
                                        <sapn ng-bind="tag.filterItemName" class="ng-binding">折扣優惠</sapn></a>
                                </li><!-- end ngRepeat: tag in dealItem.C -->
                            </ul>
                        </div>
                    </div>
                    <div class="twrbo-l-productCard__text">
                        <div class="twrbo-h-margin-bottom-md">
                            <span class="twrbo-c-h3 twrbo-c-link twrbo-c-link--ignoreEffect">
                                <span ng-bind="dealItem.name" class="ng-binding">犇 鐵板燒 安和本館</span>
                            </span>
                        </div>
                        <div class="twrbo-l-productTextCard">
                            <div class="twrbo-l-productTextCard__detail">
                                <p><span ng-bind-html="dealItem.promDesc" class="ng-binding">最優享88折優惠</span></p>
                                <div class="twrbo-h-margin-top-sm">
                                    <ul class="twrbo-c-list twrbo-c-list--data twrbo-c-list--small twrbo-c-list--small">
                                        <li ng-show="dealItem.startDay != '' &amp;&amp; dealItem.endDay != ''">
                                            <div class="twrbo-c-additionalicon">
                                                <img src="/content/dam/twrbo/images/icon/icon_clock_dark.svg" alt="" width="16" height="16">
                                                <span ng-bind="dealItem.startDay" class="ng-binding">2023/01/01</span>
                                                <span>~</span>
                                                <span ng-bind="dealItem.endDay" class="ng-binding">2023/12/31</span>
                                            </div>
                                        </li>
                                        <li ng-show="dealItem.hasOwnProperty('B') &amp;&amp; dealItem.B.length > 0" class="ng-hide">
                                            <div class="twrbo-c-additionalicon">
                                                <img src="/content/dam/twrbo/images/icon/icon_card_dark.svg" alt="" width="16" height="16">
                                                <span>適用
                                                    <!-- ngRepeat: card in dealItem.B -->
                                                </span>
                                            </div>
                                        </li>
                                        <li>
                                            <ul class="twrbo-l-listHorizontal twrbo-l-listHorizontal--additional twrbo-c-fSmall">
                                                <li ng-show="dealItem.phone != ''" class="ng-hide">
                                                    <div class="twrbo-c-additionalicon">
                                                        <img src="/content/dam/twrbo/images/icon/icon_phone_dark.svg" alt="" width="16" height="16">
                                                        <a ng-href="tel:" target="_parent" class="twrbo-h-linkEffect-url--gy twrbo-c-link--tel" href="tel:">
                                                            <span ng-bind="dealItem.phone" class="ng-binding"></span>
                                                        </a>
                                                    </div>
                                                </li>
                                                <li ng-show="dealItem.address != ''" class="ng-hide">
                                                    <div class="twrbo-c-additionalicon">
                                                        <img src="/content/dam/twrbo/images/icon/icon_location_dark.svg" alt="" width="16" height="16">
                                                        <a ng-click="clickPopup(dealItem.promId, dealItem.name, dealItem.promDesc, dealItem.address, dealItem.lng, dealItem.lat, dealItem.phone)" class="twrbo-h-linkEffect-url--gy">
                                                            <span>地址</span>
                                                        </a>
                                                    </div>
                                                </li>
                                                <li ng-show="dealItem.storeUrl != ''" class="ng-hide">
                                                    <div class="twrbo-c-additionalicon">
                                                        <img src="/content/dam/twrbo/images/icon/icon_global_dark.svg" alt="" width="16" height="16">
                                                        <a ng-href="" class="twrbo-h-linkEffect-url--gy">
                                                            <span>網址</span>
                                                        </a>
                                                    </div>
                                                </li>
                                                <li ng-show="dealItem.promUrl != ''">
                                                    <div class="twrbo-c-additionalicon">
                                                        <img src="/content/dam/twrbo/images/icon/icon_link_dark.svg" alt="" width="16" height="16">
                                                        <a ng-href="https://www.ctbcbank.com/content/dam/minisite/long/creditcard/foodsedm/index.html" class="twrbo-h-linkEffect-url--gy" href="https://www.ctbcbank.com/content/dam/minisite/long/creditcard/foodsedm/index.html">
                                                            <span>活動網頁</span>
                                                        </a>
                                                    </div>
                                                </li>
                                                <li ng-show="dealItem.notice != ''">
                                                    <div class="twrbo-c-additionalicon">
                                                        <img src="/content/dam/twrbo/images/icon/icon_notice_dark.svg" alt="" width="16" height="16">
                                                        <a ng-click="noticePopup(dealItem.notice)" class="twrbo-h-linkEffect-url--gy">
                                                            <span>注意事項</span>
                                                        </a>
                                                    </div>
                                                </li>
                                            </ul>
                                        </li>
                                    </ul>
                                </div>
                            </div>
                        </div>
                    </div>
                </div><!-- end ngRepeat: dealItem in dealList.promotionDetailList --><div ng-repeat="dealItem in dealList.promotionDetailList" class="twrbo-l-productCard twrbo-l-productCard--list ng-scope">
                    <div class="twrbo-l-productCard__thumb">
                        <span class="twrbo-c-thumb picturefill-background" style="background-image: url(&quot;/content/dam/twrbo/images/creditcard/offer/F202319.jpg&quot;); background-size: cover; background-repeat: no-repeat; background-position: 50% 50%;">
                            <span data-src="/content/dam/twrbo/images/creditcard/offer/F202319.jpg" data-src-default="/content/dam/twrbo/images/matchCard.png"></span>
                        </span>
                        <div class="twrbo-h-gutters-out-sm-v">
                            <ul class="twrbo-c-label twrbo-c-label--trim">
                                <li ng-show="dealItem.promTag != ''">
                                    <ul class="twrbo-c-label twrbo-c-label--promo twrbo-c-label--trim">
                                        <li>
                                            <i class="twrbo-c-iLabel twrbo-c-iLabel--fire"></i>
                                            <span ng-bind="dealItem.promTag" class="ng-binding">熱門</span>
                                        </li>
                                    </ul>
                                </li>
                                <!-- ngRepeat: tag in dealItem.C --><li ng-repeat="tag in dealItem.C" ng-show="dealItem.hasOwnProperty('C')" class="ng-scope">
                                    <a ng-click="onTagClick(tag.filterItemKey, tag.filterItemName)">
                                        <sapn ng-bind="tag.filterItemName" class="ng-binding">折扣優惠</sapn></a>
                                </li><!-- end ngRepeat: tag in dealItem.C -->
                            </ul>
                        </div>
                    </div>
                    <div class="twrbo-l-productCard__text">
                        <div class="twrbo-h-margin-bottom-md">
                            <span class="twrbo-c-h3 twrbo-c-link twrbo-c-link--ignoreEffect">
                                <span ng-bind="dealItem.name" class="ng-binding">犇 極上 微風信義館</span>
                            </span>
                        </div>
                        <div class="twrbo-l-productTextCard">
                            <div class="twrbo-l-productTextCard__detail">
                                <p><span ng-bind-html="dealItem.promDesc" class="ng-binding">最優享88折優惠</span></p>
                                <div class="twrbo-h-margin-top-sm">
                                    <ul class="twrbo-c-list twrbo-c-list--data twrbo-c-list--small twrbo-c-list--small">
                                        <li ng-show="dealItem.startDay != '' &amp;&amp; dealItem.endDay != ''">
                                            <div class="twrbo-c-additionalicon">
                                                <img src="/content/dam/twrbo/images/icon/icon_clock_dark.svg" alt="" width="16" height="16">
                                                <span ng-bind="dealItem.startDay" class="ng-binding">2023/06/01</span>
                                                <span>~</span>
                                                <span ng-bind="dealItem.endDay" class="ng-binding">2023/12/31</span>
                                            </div>
                                        </li>
                                        <li ng-show="dealItem.hasOwnProperty('B') &amp;&amp; dealItem.B.length > 0" class="ng-hide">
                                            <div class="twrbo-c-additionalicon">
                                                <img src="/content/dam/twrbo/images/icon/icon_card_dark.svg" alt="" width="16" height="16">
                                                <span>適用
                                                    <!-- ngRepeat: card in dealItem.B -->
                                                </span>
                                            </div>
                                        </li>
                                        <li>
                                            <ul class="twrbo-l-listHorizontal twrbo-l-listHorizontal--additional twrbo-c-fSmall">
                                                <li ng-show="dealItem.phone != ''" class="ng-hide">
                                                    <div class="twrbo-c-additionalicon">
                                                        <img src="/content/dam/twrbo/images/icon/icon_phone_dark.svg" alt="" width="16" height="16">
                                                        <a ng-href="tel:" target="_parent" class="twrbo-h-linkEffect-url--gy twrbo-c-link--tel" href="tel:">
                                                            <span ng-bind="dealItem.phone" class="ng-binding"></span>
                                                        </a>
                                                    </div>
                                                </li>
                                                <li ng-show="dealItem.address != ''" class="ng-hide">
                                                    <div class="twrbo-c-additionalicon">
                                                        <img src="/content/dam/twrbo/images/icon/icon_location_dark.svg" alt="" width="16" height="16">
                                                        <a ng-click="clickPopup(dealItem.promId, dealItem.name, dealItem.promDesc, dealItem.address, dealItem.lng, dealItem.lat, dealItem.phone)" class="twrbo-h-linkEffect-url--gy">
                                                            <span>地址</span>
                                                        </a>
                                                    </div>
                                                </li>
                                                <li ng-show="dealItem.storeUrl != ''" class="ng-hide">
                                                    <div class="twrbo-c-additionalicon">
                                                        <img src="/content/dam/twrbo/images/icon/icon_global_dark.svg" alt="" width="16" height="16">
                                                        <a ng-href="" class="twrbo-h-linkEffect-url--gy">
                                                            <span>網址</span>
                                                        </a>
                                                    </div>
                                                </li>
                                                <li ng-show="dealItem.promUrl != ''">
                                                    <div class="twrbo-c-additionalicon">
                                                        <img src="/content/dam/twrbo/images/icon/icon_link_dark.svg" alt="" width="16" height="16">
                                                        <a ng-href="https://www.ctbcbank.com/content/dam/minisite/long/creditcard/foodsedm/index.html" class="twrbo-h-linkEffect-url--gy" href="https://www.ctbcbank.com/content/dam/minisite/long/creditcard/foodsedm/index.html">
                                                            <span>活動網頁</span>
                                                        </a>
                                                    </div>
                                                </li>
                                                <li ng-show="dealItem.notice != ''">
                                                    <div class="twrbo-c-additionalicon">
                                                        <img src="/content/dam/twrbo/images/icon/icon_notice_dark.svg" alt="" width="16" height="16">
                                                        <a ng-click="noticePopup(dealItem.notice)" class="twrbo-h-linkEffect-url--gy">
                                                            <span>注意事項</span>
                                                        </a>
                                                    </div>
                                                </li>
                                            </ul>
                                        </li>
                                    </ul>
                                </div>
                            </div>
                        </div>
                    </div>
                </div><!-- end ngRepeat: dealItem in dealList.promotionDetailList --><div ng-repeat="dealItem in dealList.promotionDetailList" class="twrbo-l-productCard twrbo-l-productCard--list ng-scope">
                    <div class="twrbo-l-productCard__thumb">
                        <span class="twrbo-c-thumb picturefill-background" style="background-image: url(&quot;/content/dam/twrbo/images/creditcard/offer/F202321.jpg&quot;); background-size: cover; background-repeat: no-repeat; background-position: 50% 50%;">
                            <span data-src="/content/dam/twrbo/images/creditcard/offer/F202321.jpg" data-src-default="/content/dam/twrbo/images/matchCard.png"></span>
                        </span>
                        <div class="twrbo-h-gutters-out-sm-v">
                            <ul class="twrbo-c-label twrbo-c-label--trim">
                                <li ng-show="dealItem.promTag != ''">
                                    <ul class="twrbo-c-label twrbo-c-label--promo twrbo-c-label--trim">
                                        <li>
                                            <i class="twrbo-c-iLabel twrbo-c-iLabel--fire"></i>
                                            <span ng-bind="dealItem.promTag" class="ng-binding">熱門</span>
                                        </li>
                                    </ul>
                                </li>
                                <!-- ngRepeat: tag in dealItem.C --><li ng-repeat="tag in dealItem.C" ng-show="dealItem.hasOwnProperty('C')" class="ng-scope">
                                    <a ng-click="onTagClick(tag.filterItemKey, tag.filterItemName)">
                                        <sapn ng-bind="tag.filterItemName" class="ng-binding">滿額送菜</sapn></a>
                                </li><!-- end ngRepeat: tag in dealItem.C -->
                            </ul>
                        </div>
                    </div>
                    <div class="twrbo-l-productCard__text">
                        <div class="twrbo-h-margin-bottom-md">
                            <span class="twrbo-c-h3 twrbo-c-link twrbo-c-link--ignoreEffect">
                                <span ng-bind="dealItem.name" class="ng-binding">金爸爸</span>
                            </span>
                        </div>
                        <div class="twrbo-l-productTextCard">
                            <div class="twrbo-l-productTextCard__detail">
                                <p><span ng-bind-html="dealItem.promDesc" class="ng-binding">贈【開運祝壽桃】</span></p>
                                <div class="twrbo-h-margin-top-sm">
                                    <ul class="twrbo-c-list twrbo-c-list--data twrbo-c-list--small twrbo-c-list--small">
                                        <li ng-show="dealItem.startDay != '' &amp;&amp; dealItem.endDay != ''">
                                            <div class="twrbo-c-additionalicon">
                                                <img src="/content/dam/twrbo/images/icon/icon_clock_dark.svg" alt="" width="16" height="16">
                                                <span ng-bind="dealItem.startDay" class="ng-binding">2023/01/01</span>
                                                <span>~</span>
                                                <span ng-bind="dealItem.endDay" class="ng-binding">2023/12/31</span>
                                            </div>
                                        </li>
                                        <li ng-show="dealItem.hasOwnProperty('B') &amp;&amp; dealItem.B.length > 0" class="ng-hide">
                                            <div class="twrbo-c-additionalicon">
                                                <img src="/content/dam/twrbo/images/icon/icon_card_dark.svg" alt="" width="16" height="16">
                                                <span>適用
                                                    <!-- ngRepeat: card in dealItem.B -->
                                                </span>
                                            </div>
                                        </li>
                                        <li>
                                            <ul class="twrbo-l-listHorizontal twrbo-l-listHorizontal--additional twrbo-c-fSmall">
                                                <li ng-show="dealItem.phone != ''" class="ng-hide">
                                                    <div class="twrbo-c-additionalicon">
                                                        <img src="/content/dam/twrbo/images/icon/icon_phone_dark.svg" alt="" width="16" height="16">
                                                        <a ng-href="tel:" target="_parent" class="twrbo-h-linkEffect-url--gy twrbo-c-link--tel" href="tel:">
                                                            <span ng-bind="dealItem.phone" class="ng-binding"></span>
                                                        </a>
                                                    </div>
                                                </li>
                                                <li ng-show="dealItem.address != ''" class="ng-hide">
                                                    <div class="twrbo-c-additionalicon">
                                                        <img src="/content/dam/twrbo/images/icon/icon_location_dark.svg" alt="" width="16" height="16">
                                                        <a ng-click="clickPopup(dealItem.promId, dealItem.name, dealItem.promDesc, dealItem.address, dealItem.lng, dealItem.lat, dealItem.phone)" class="twrbo-h-linkEffect-url--gy">
                                                            <span>地址</span>
                                                        </a>
                                                    </div>
                                                </li>
                                                <li ng-show="dealItem.storeUrl != ''" class="ng-hide">
                                                    <div class="twrbo-c-additionalicon">
                                                        <img src="/content/dam/twrbo/images/icon/icon_global_dark.svg" alt="" width="16" height="16">
                                                        <a ng-href="" class="twrbo-h-linkEffect-url--gy">
                                                            <span>網址</span>
                                                        </a>
                                                    </div>
                                                </li>
                                                <li ng-show="dealItem.promUrl != ''">
                                                    <div class="twrbo-c-additionalicon">
                                                        <img src="/content/dam/twrbo/images/icon/icon_link_dark.svg" alt="" width="16" height="16">
                                                        <a ng-href="https://www.ctbcbank.com/content/dam/minisite/long/creditcard/foodsedm/index.html" class="twrbo-h-linkEffect-url--gy" href="https://www.ctbcbank.com/content/dam/minisite/long/creditcard/foodsedm/index.html">
                                                            <span>活動網頁</span>
                                                        </a>
                                                    </div>
                                                </li>
                                                <li ng-show="dealItem.notice != ''">
                                                    <div class="twrbo-c-additionalicon">
                                                        <img src="/content/dam/twrbo/images/icon/icon_notice_dark.svg" alt="" width="16" height="16">
                                                        <a ng-click="noticePopup(dealItem.notice)" class="twrbo-h-linkEffect-url--gy">
                                                            <span>注意事項</span>
                                                        </a>
                                                    </div>
                                                </li>
                                            </ul>
                                        </li>
                                    </ul>
                                </div>
                            </div>
                        </div>
                    </div>
                </div><!-- end ngRepeat: dealItem in dealList.promotionDetailList --><div ng-repeat="dealItem in dealList.promotionDetailList" class="twrbo-l-productCard twrbo-l-productCard--list ng-scope">
                    <div class="twrbo-l-productCard__thumb">
                        <span class="twrbo-c-thumb picturefill-background" style="background-image: url(&quot;/content/dam/twrbo/images/creditcard/offer/F202322.jpg&quot;); background-size: cover; background-repeat: no-repeat; background-position: 50% 50%;">
                            <span data-src="/content/dam/twrbo/images/creditcard/offer/F202322.jpg" data-src-default="/content/dam/twrbo/images/matchCard.png"></span>
                        </span>
                        <div class="twrbo-h-gutters-out-sm-v">
                            <ul class="twrbo-c-label twrbo-c-label--trim">
                                <li ng-show="dealItem.promTag != ''">
                                    <ul class="twrbo-c-label twrbo-c-label--promo twrbo-c-label--trim">
                                        <li>
                                            <i class="twrbo-c-iLabel twrbo-c-iLabel--fire"></i>
                                            <span ng-bind="dealItem.promTag" class="ng-binding">熱門</span>
                                        </li>
                                    </ul>
                                </li>
                                <!-- ngRepeat: tag in dealItem.C --><li ng-repeat="tag in dealItem.C" ng-show="dealItem.hasOwnProperty('C')" class="ng-scope">
                                    <a ng-click="onTagClick(tag.filterItemKey, tag.filterItemName)">
                                        <sapn ng-bind="tag.filterItemName" class="ng-binding">折扣優惠</sapn></a>
                                </li><!-- end ngRepeat: tag in dealItem.C -->
                            </ul>
                        </div>
                    </div>
                    <div class="twrbo-l-productCard__text">
                        <div class="twrbo-h-margin-bottom-md">
                            <span class="twrbo-c-h3 twrbo-c-link twrbo-c-link--ignoreEffect">
                                <span ng-bind="dealItem.name" class="ng-binding">Mega 50</span>
                            </span>
                        </div>
                        <div class="twrbo-l-productTextCard">
                            <div class="twrbo-l-productTextCard__detail">
                                <p><span ng-bind-html="dealItem.promDesc" class="ng-binding">享85折優惠</span></p>
                                <div class="twrbo-h-margin-top-sm">
                                    <ul class="twrbo-c-list twrbo-c-list--data twrbo-c-list--small twrbo-c-list--small">
                                        <li ng-show="dealItem.startDay != '' &amp;&amp; dealItem.endDay != ''">
                                            <div class="twrbo-c-additionalicon">
                                                <img src="/content/dam/twrbo/images/icon/icon_clock_dark.svg" alt="" width="16" height="16">
                                                <span ng-bind="dealItem.startDay" class="ng-binding">2023/01/01</span>
                                                <span>~</span>
                                                <span ng-bind="dealItem.endDay" class="ng-binding">2023/12/31</span>
                                            </div>
                                        </li>
                                        <li ng-show="dealItem.hasOwnProperty('B') &amp;&amp; dealItem.B.length > 0" class="ng-hide">
                                            <div class="twrbo-c-additionalicon">
                                                <img src="/content/dam/twrbo/images/icon/icon_card_dark.svg" alt="" width="16" height="16">
                                                <span>適用
                                                    <!-- ngRepeat: card in dealItem.B -->
                                                </span>
                                            </div>
                                        </li>
                                        <li>
                                            <ul class="twrbo-l-listHorizontal twrbo-l-listHorizontal--additional twrbo-c-fSmall">
                                                <li ng-show="dealItem.phone != ''" class="ng-hide">
                                                    <div class="twrbo-c-additionalicon">
                                                        <img src="/content/dam/twrbo/images/icon/icon_phone_dark.svg" alt="" width="16" height="16">
                                                        <a ng-href="tel:" target="_parent" class="twrbo-h-linkEffect-url--gy twrbo-c-link--tel" href="tel:">
                                                            <span ng-bind="dealItem.phone" class="ng-binding"></span>
                                                        </a>
                                                    </div>
                                                </li>
                                                <li ng-show="dealItem.address != ''" class="ng-hide">
                                                    <div class="twrbo-c-additionalicon">
                                                        <img src="/content/dam/twrbo/images/icon/icon_location_dark.svg" alt="" width="16" height="16">
                                                        <a ng-click="clickPopup(dealItem.promId, dealItem.name, dealItem.promDesc, dealItem.address, dealItem.lng, dealItem.lat, dealItem.phone)" class="twrbo-h-linkEffect-url--gy">
                                                            <span>地址</span>
                                                        </a>
                                                    </div>
                                                </li>
                                                <li ng-show="dealItem.storeUrl != ''" class="ng-hide">
                                                    <div class="twrbo-c-additionalicon">
                                                        <img src="/content/dam/twrbo/images/icon/icon_global_dark.svg" alt="" width="16" height="16">
                                                        <a ng-href="" class="twrbo-h-linkEffect-url--gy">
                                                            <span>網址</span>
                                                        </a>
                                                    </div>
                                                </li>
                                                <li ng-show="dealItem.promUrl != ''">
                                                    <div class="twrbo-c-additionalicon">
                                                        <img src="/content/dam/twrbo/images/icon/icon_link_dark.svg" alt="" width="16" height="16">
                                                        <a ng-href="https://www.ctbcbank.com/content/dam/minisite/long/creditcard/foodsedm/index.html" class="twrbo-h-linkEffect-url--gy" href="https://www.ctbcbank.com/content/dam/minisite/long/creditcard/foodsedm/index.html">
                                                            <span>活動網頁</span>
                                                        </a>
                                                    </div>
                                                </li>
                                                <li ng-show="dealItem.notice != ''">
                                                    <div class="twrbo-c-additionalicon">
                                                        <img src="/content/dam/twrbo/images/icon/icon_notice_dark.svg" alt="" width="16" height="16">
                                                        <a ng-click="noticePopup(dealItem.notice)" class="twrbo-h-linkEffect-url--gy">
                                                            <span>注意事項</span>
                                                        </a>
                                                    </div>
                                                </li>
                                            </ul>
                                        </li>
                                    </ul>
                                </div>
                            </div>
                        </div>
                    </div>
                </div><!-- end ngRepeat: dealItem in dealList.promotionDetailList --><div ng-repeat="dealItem in dealList.promotionDetailList" class="twrbo-l-productCard twrbo-l-productCard--list ng-scope">
                    <div class="twrbo-l-productCard__thumb">
                        <span class="twrbo-c-thumb picturefill-background" style="background-image: url(&quot;/content/dam/twrbo/images/creditcard/offer/F202323.jpg&quot;); background-size: cover; background-repeat: no-repeat; background-position: 50% 50%;">
                            <span data-src="/content/dam/twrbo/images/creditcard/offer/F202323.jpg" data-src-default="/content/dam/twrbo/images/matchCard.png"></span>
                        </span>
                        <div class="twrbo-h-gutters-out-sm-v">
                            <ul class="twrbo-c-label twrbo-c-label--trim">
                                <li ng-show="dealItem.promTag != ''">
                                    <ul class="twrbo-c-label twrbo-c-label--promo twrbo-c-label--trim">
                                        <li>
                                            <i class="twrbo-c-iLabel twrbo-c-iLabel--fire"></i>
                                            <span ng-bind="dealItem.promTag" class="ng-binding">熱門</span>
                                        </li>
                                    </ul>
                                </li>
                                <!-- ngRepeat: tag in dealItem.C --><li ng-repeat="tag in dealItem.C" ng-show="dealItem.hasOwnProperty('C')" class="ng-scope">
                                    <a ng-click="onTagClick(tag.filterItemKey, tag.filterItemName)">
                                        <sapn ng-bind="tag.filterItemName" class="ng-binding">滿額送菜</sapn></a>
                                </li><!-- end ngRepeat: tag in dealItem.C -->
                            </ul>
                        </div>
                    </div>
                    <div class="twrbo-l-productCard__text">
                        <div class="twrbo-h-margin-bottom-md">
                            <span class="twrbo-c-h3 twrbo-c-link twrbo-c-link--ignoreEffect">
                                <span ng-bind="dealItem.name" class="ng-binding">帕泰家</span>
                            </span>
                        </div>
                        <div class="twrbo-l-productTextCard">
                            <div class="twrbo-l-productTextCard__detail">
                                <p><span ng-bind-html="dealItem.promDesc" class="ng-binding">贈【蝦醬芥藍】</span></p>
                                <div class="twrbo-h-margin-top-sm">
                                    <ul class="twrbo-c-list twrbo-c-list--data twrbo-c-list--small twrbo-c-list--small">
                                        <li ng-show="dealItem.startDay != '' &amp;&amp; dealItem.endDay != ''">
                                            <div class="twrbo-c-additionalicon">
                                                <img src="/content/dam/twrbo/images/icon/icon_clock_dark.svg" alt="" width="16" height="16">
                                                <span ng-bind="dealItem.startDay" class="ng-binding">2023/01/01</span>
                                                <span>~</span>
                                                <span ng-bind="dealItem.endDay" class="ng-binding">2023/12/31</span>
                                            </div>
                                        </li>
                                        <li ng-show="dealItem.hasOwnProperty('B') &amp;&amp; dealItem.B.length > 0" class="ng-hide">
                                            <div class="twrbo-c-additionalicon">
                                                <img src="/content/dam/twrbo/images/icon/icon_card_dark.svg" alt="" width="16" height="16">
                                                <span>適用
                                                    <!-- ngRepeat: card in dealItem.B -->
                                                </span>
                                            </div>
                                        </li>
                                        <li>
                                            <ul class="twrbo-l-listHorizontal twrbo-l-listHorizontal--additional twrbo-c-fSmall">
                                                <li ng-show="dealItem.phone != ''" class="ng-hide">
                                                    <div class="twrbo-c-additionalicon">
                                                        <img src="/content/dam/twrbo/images/icon/icon_phone_dark.svg" alt="" width="16" height="16">
                                                        <a ng-href="tel:" target="_parent" class="twrbo-h-linkEffect-url--gy twrbo-c-link--tel" href="tel:">
                                                            <span ng-bind="dealItem.phone" class="ng-binding"></span>
                                                        </a>
                                                    </div>
                                                </li>
                                                <li ng-show="dealItem.address != ''" class="ng-hide">
                                                    <div class="twrbo-c-additionalicon">
                                                        <img src="/content/dam/twrbo/images/icon/icon_location_dark.svg" alt="" width="16" height="16">
                                                        <a ng-click="clickPopup(dealItem.promId, dealItem.name, dealItem.promDesc, dealItem.address, dealItem.lng, dealItem.lat, dealItem.phone)" class="twrbo-h-linkEffect-url--gy">
                                                            <span>地址</span>
                                                        </a>
                                                    </div>
                                                </li>
                                                <li ng-show="dealItem.storeUrl != ''" class="ng-hide">
                                                    <div class="twrbo-c-additionalicon">
                                                        <img src="/content/dam/twrbo/images/icon/icon_global_dark.svg" alt="" width="16" height="16">
                                                        <a ng-href="" class="twrbo-h-linkEffect-url--gy">
                                                            <span>網址</span>
                                                        </a>
                                                    </div>
                                                </li>
                                                <li ng-show="dealItem.promUrl != ''">
                                                    <div class="twrbo-c-additionalicon">
                                                        <img src="/content/dam/twrbo/images/icon/icon_link_dark.svg" alt="" width="16" height="16">
                                                        <a ng-href="https://www.ctbcbank.com/content/dam/minisite/long/creditcard/foodsedm/index.html" class="twrbo-h-linkEffect-url--gy" href="https://www.ctbcbank.com/content/dam/minisite/long/creditcard/foodsedm/index.html">
                                                            <span>活動網頁</span>
                                                        </a>
                                                    </div>
                                                </li>
                                                <li ng-show="dealItem.notice != ''">
                                                    <div class="twrbo-c-additionalicon">
                                                        <img src="/content/dam/twrbo/images/icon/icon_notice_dark.svg" alt="" width="16" height="16">
                                                        <a ng-click="noticePopup(dealItem.notice)" class="twrbo-h-linkEffect-url--gy">
                                                            <span>注意事項</span>
                                                        </a>
                                                    </div>
                                                </li>
                                            </ul>
                                        </li>
                                    </ul>
                                </div>
                            </div>
                        </div>
                    </div>
                </div><!-- end ngRepeat: dealItem in dealList.promotionDetailList --><div ng-repeat="dealItem in dealList.promotionDetailList" class="twrbo-l-productCard twrbo-l-productCard--list ng-scope">
                    <div class="twrbo-l-productCard__thumb">
                        <span class="twrbo-c-thumb picturefill-background" style="background-image: url(&quot;/content/dam/twrbo/images/creditcard/offer/F202324.jpg&quot;); background-size: cover; background-repeat: no-repeat; background-position: 50% 50%;">
                            <span data-src="/content/dam/twrbo/images/creditcard/offer/F202324.jpg" data-src-default="/content/dam/twrbo/images/matchCard.png"></span>
                        </span>
                        <div class="twrbo-h-gutters-out-sm-v">
                            <ul class="twrbo-c-label twrbo-c-label--trim">
                                <li ng-show="dealItem.promTag != ''">
                                    <ul class="twrbo-c-label twrbo-c-label--promo twrbo-c-label--trim">
                                        <li>
                                            <i class="twrbo-c-iLabel twrbo-c-iLabel--fire"></i>
                                            <span ng-bind="dealItem.promTag" class="ng-binding">熱門</span>
                                        </li>
                                    </ul>
                                </li>
                                <!-- ngRepeat: tag in dealItem.C --><li ng-repeat="tag in dealItem.C" ng-show="dealItem.hasOwnProperty('C')" class="ng-scope">
                                    <a ng-click="onTagClick(tag.filterItemKey, tag.filterItemName)">
                                        <sapn ng-bind="tag.filterItemName" class="ng-binding">折扣優惠</sapn></a>
                                </li><!-- end ngRepeat: tag in dealItem.C -->
                            </ul>
                        </div>
                    </div>
                    <div class="twrbo-l-productCard__text">
                        <div class="twrbo-h-margin-bottom-md">
                            <span class="twrbo-c-h3 twrbo-c-link twrbo-c-link--ignoreEffect">
                                <span ng-bind="dealItem.name" class="ng-binding">foodpanda</span>
                            </span>
                        </div>
                        <div class="twrbo-l-productTextCard">
                            <div class="twrbo-l-productTextCard__detail">
                                <p><span ng-bind-html="dealItem.promDesc" class="ng-binding">最優享5折</span></p>
                                <div class="twrbo-h-margin-top-sm">
                                    <ul class="twrbo-c-list twrbo-c-list--data twrbo-c-list--small twrbo-c-list--small">
                                        <li ng-show="dealItem.startDay != '' &amp;&amp; dealItem.endDay != ''">
                                            <div class="twrbo-c-additionalicon">
                                                <img src="/content/dam/twrbo/images/icon/icon_clock_dark.svg" alt="" width="16" height="16">
                                                <span ng-bind="dealItem.startDay" class="ng-binding">2023/01/01</span>
                                                <span>~</span>
                                                <span ng-bind="dealItem.endDay" class="ng-binding">2023/12/31</span>
                                            </div>
                                        </li>
                                        <li ng-show="dealItem.hasOwnProperty('B') &amp;&amp; dealItem.B.length > 0" class="ng-hide">
                                            <div class="twrbo-c-additionalicon">
                                                <img src="/content/dam/twrbo/images/icon/icon_card_dark.svg" alt="" width="16" height="16">
                                                <span>適用
                                                    <!-- ngRepeat: card in dealItem.B -->
                                                </span>
                                            </div>
                                        </li>
                                        <li>
                                            <ul class="twrbo-l-listHorizontal twrbo-l-listHorizontal--additional twrbo-c-fSmall">
                                                <li ng-show="dealItem.phone != ''" class="ng-hide">
                                                    <div class="twrbo-c-additionalicon">
                                                        <img src="/content/dam/twrbo/images/icon/icon_phone_dark.svg" alt="" width="16" height="16">
                                                        <a ng-href="tel:" target="_parent" class="twrbo-h-linkEffect-url--gy twrbo-c-link--tel" href="tel:">
                                                            <span ng-bind="dealItem.phone" class="ng-binding"></span>
                                                        </a>
                                                    </div>
                                                </li>
                                                <li ng-show="dealItem.address != ''" class="ng-hide">
                                                    <div class="twrbo-c-additionalicon">
                                                        <img src="/content/dam/twrbo/images/icon/icon_location_dark.svg" alt="" width="16" height="16">
                                                        <a ng-click="clickPopup(dealItem.promId, dealItem.name, dealItem.promDesc, dealItem.address, dealItem.lng, dealItem.lat, dealItem.phone)" class="twrbo-h-linkEffect-url--gy">
                                                            <span>地址</span>
                                                        </a>
                                                    </div>
                                                </li>
                                                <li ng-show="dealItem.storeUrl != ''" class="ng-hide">
                                                    <div class="twrbo-c-additionalicon">
                                                        <img src="/content/dam/twrbo/images/icon/icon_global_dark.svg" alt="" width="16" height="16">
                                                        <a ng-href="" class="twrbo-h-linkEffect-url--gy">
                                                            <span>網址</span>
                                                        </a>
                                                    </div>
                                                </li>
                                                <li ng-show="dealItem.promUrl != ''">
                                                    <div class="twrbo-c-additionalicon">
                                                        <img src="/content/dam/twrbo/images/icon/icon_link_dark.svg" alt="" width="16" height="16">
                                                        <a ng-href="https://www.ctbcbank.com/content/dam/minisite/long/creditcard/foodsedm/index.html" class="twrbo-h-linkEffect-url--gy" href="https://www.ctbcbank.com/content/dam/minisite/long/creditcard/foodsedm/index.html">
                                                            <span>活動網頁</span>
                                                        </a>
                                                    </div>
                                                </li>
                                                <li ng-show="dealItem.notice != ''">
                                                    <div class="twrbo-c-additionalicon">
                                                        <img src="/content/dam/twrbo/images/icon/icon_notice_dark.svg" alt="" width="16" height="16">
                                                        <a ng-click="noticePopup(dealItem.notice)" class="twrbo-h-linkEffect-url--gy">
                                                            <span>注意事項</span>
                                                        </a>
                                                    </div>
                                                </li>
                                            </ul>
                                        </li>
                                    </ul>
                                </div>
                            </div>
                        </div>
                    </div>
                </div><!-- end ngRepeat: dealItem in dealList.promotionDetailList --><div ng-repeat="dealItem in dealList.promotionDetailList" class="twrbo-l-productCard twrbo-l-productCard--list ng-scope">
                    <div class="twrbo-l-productCard__thumb">
                        <span class="twrbo-c-thumb picturefill-background" style="background-image: url(&quot;/content/dam/twrbo/images/creditcard/offer/F202325.jpg&quot;); background-size: cover; background-repeat: no-repeat; background-position: 50% 50%;">
                            <span data-src="/content/dam/twrbo/images/creditcard/offer/F202325.jpg" data-src-default="/content/dam/twrbo/images/matchCard.png"></span>
                        </span>
                        <div class="twrbo-h-gutters-out-sm-v">
                            <ul class="twrbo-c-label twrbo-c-label--trim">
                                <li ng-show="dealItem.promTag != ''">
                                    <ul class="twrbo-c-label twrbo-c-label--promo twrbo-c-label--trim">
                                        <li>
                                            <i class="twrbo-c-iLabel twrbo-c-iLabel--fire"></i>
                                            <span ng-bind="dealItem.promTag" class="ng-binding">熱門</span>
                                        </li>
                                    </ul>
                                </li>
                                <!-- ngRepeat: tag in dealItem.C --><li ng-repeat="tag in dealItem.C" ng-show="dealItem.hasOwnProperty('C')" class="ng-scope">
                                    <a ng-click="onTagClick(tag.filterItemKey, tag.filterItemName)">
                                        <sapn ng-bind="tag.filterItemName" class="ng-binding">折扣優惠</sapn></a>
                                </li><!-- end ngRepeat: tag in dealItem.C -->
                            </ul>
                        </div>
                    </div>
                    <div class="twrbo-l-productCard__text">
                        <div class="twrbo-h-margin-bottom-md">
                            <span class="twrbo-c-h3 twrbo-c-link twrbo-c-link--ignoreEffect">
                                <span ng-bind="dealItem.name" class="ng-binding">COLD STONE</span>
                            </span>
                        </div>
                        <div class="twrbo-l-productTextCard">
                            <div class="twrbo-l-productTextCard__detail">
                                <p><span ng-bind-html="dealItem.promDesc" class="ng-binding">第二件5折</span></p>
                                <div class="twrbo-h-margin-top-sm">
                                    <ul class="twrbo-c-list twrbo-c-list--data twrbo-c-list--small twrbo-c-list--small">
                                        <li ng-show="dealItem.startDay != '' &amp;&amp; dealItem.endDay != ''">
                                            <div class="twrbo-c-additionalicon">
                                                <img src="/content/dam/twrbo/images/icon/icon_clock_dark.svg" alt="" width="16" height="16">
                                                <span ng-bind="dealItem.startDay" class="ng-binding">2023/01/01</span>
                                                <span>~</span>
                                                <span ng-bind="dealItem.endDay" class="ng-binding">2023/12/31</span>
                                            </div>
                                        </li>
                                        <li ng-show="dealItem.hasOwnProperty('B') &amp;&amp; dealItem.B.length > 0" class="ng-hide">
                                            <div class="twrbo-c-additionalicon">
                                                <img src="/content/dam/twrbo/images/icon/icon_card_dark.svg" alt="" width="16" height="16">
                                                <span>適用
                                                    <!-- ngRepeat: card in dealItem.B -->
                                                </span>
                                            </div>
                                        </li>
                                        <li>
                                            <ul class="twrbo-l-listHorizontal twrbo-l-listHorizontal--additional twrbo-c-fSmall">
                                                <li ng-show="dealItem.phone != ''" class="ng-hide">
                                                    <div class="twrbo-c-additionalicon">
                                                        <img src="/content/dam/twrbo/images/icon/icon_phone_dark.svg" alt="" width="16" height="16">
                                                        <a ng-href="tel:" target="_parent" class="twrbo-h-linkEffect-url--gy twrbo-c-link--tel" href="tel:">
                                                            <span ng-bind="dealItem.phone" class="ng-binding"></span>
                                                        </a>
                                                    </div>
                                                </li>
                                                <li ng-show="dealItem.address != ''" class="ng-hide">
                                                    <div class="twrbo-c-additionalicon">
                                                        <img src="/content/dam/twrbo/images/icon/icon_location_dark.svg" alt="" width="16" height="16">
                                                        <a ng-click="clickPopup(dealItem.promId, dealItem.name, dealItem.promDesc, dealItem.address, dealItem.lng, dealItem.lat, dealItem.phone)" class="twrbo-h-linkEffect-url--gy">
                                                            <span>地址</span>
                                                        </a>
                                                    </div>
                                                </li>
                                                <li ng-show="dealItem.storeUrl != ''" class="ng-hide">
                                                    <div class="twrbo-c-additionalicon">
                                                        <img src="/content/dam/twrbo/images/icon/icon_global_dark.svg" alt="" width="16" height="16">
                                                        <a ng-href="" class="twrbo-h-linkEffect-url--gy">
                                                            <span>網址</span>
                                                        </a>
                                                    </div>
                                                </li>
                                                <li ng-show="dealItem.promUrl != ''">
                                                    <div class="twrbo-c-additionalicon">
                                                        <img src="/content/dam/twrbo/images/icon/icon_link_dark.svg" alt="" width="16" height="16">
                                                        <a ng-href="https://www.ctbcbank.com/content/dam/minisite/long/creditcard/foodsedm/index.html" class="twrbo-h-linkEffect-url--gy" href="https://www.ctbcbank.com/content/dam/minisite/long/creditcard/foodsedm/index.html">
                                                            <span>活動網頁</span>
                                                        </a>
                                                    </div>
                                                </li>
                                                <li ng-show="dealItem.notice != ''">
                                                    <div class="twrbo-c-additionalicon">
                                                        <img src="/content/dam/twrbo/images/icon/icon_notice_dark.svg" alt="" width="16" height="16">
                                                        <a ng-click="noticePopup(dealItem.notice)" class="twrbo-h-linkEffect-url--gy">
                                                            <span>注意事項</span>
                                                        </a>
                                                    </div>
                                                </li>
                                            </ul>
                                        </li>
                                    </ul>
                                </div>
                            </div>
                        </div>
                    </div>
                </div><!-- end ngRepeat: dealItem in dealList.promotionDetailList --><div ng-repeat="dealItem in dealList.promotionDetailList" class="twrbo-l-productCard twrbo-l-productCard--list ng-scope">
                    <div class="twrbo-l-productCard__thumb">
                        <span class="twrbo-c-thumb picturefill-background" style="background-image: url(&quot;/content/dam/twrbo/images/creditcard/offer/F202326.jpg&quot;); background-size: cover; background-repeat: no-repeat; background-position: 50% 50%;">
                            <span data-src="/content/dam/twrbo/images/creditcard/offer/F202326.jpg" data-src-default="/content/dam/twrbo/images/matchCard.png"></span>
                        </span>
                        <div class="twrbo-h-gutters-out-sm-v">
                            <ul class="twrbo-c-label twrbo-c-label--trim">
                                <li ng-show="dealItem.promTag != ''">
                                    <ul class="twrbo-c-label twrbo-c-label--promo twrbo-c-label--trim">
                                        <li>
                                            <i class="twrbo-c-iLabel twrbo-c-iLabel--fire"></i>
                                            <span ng-bind="dealItem.promTag" class="ng-binding">熱門</span>
                                        </li>
                                    </ul>
                                </li>
                                <!-- ngRepeat: tag in dealItem.C --><li ng-repeat="tag in dealItem.C" ng-show="dealItem.hasOwnProperty('C')" class="ng-scope">
                                    <a ng-click="onTagClick(tag.filterItemKey, tag.filterItemName)">
                                        <sapn ng-bind="tag.filterItemName" class="ng-binding">滿額送菜</sapn></a>
                                </li><!-- end ngRepeat: tag in dealItem.C -->
                            </ul>
                        </div>
                    </div>
                    <div class="twrbo-l-productCard__text">
                        <div class="twrbo-h-margin-bottom-md">
                            <span class="twrbo-c-h3 twrbo-c-link twrbo-c-link--ignoreEffect">
                                <span ng-bind="dealItem.name" class="ng-binding">Mister Donut</span>
                            </span>
                        </div>
                        <div class="twrbo-l-productTextCard">
                            <div class="twrbo-l-productTextCard__detail">
                                <p><span ng-bind-html="dealItem.promDesc" class="ng-binding">享買四送一優惠</span></p>
                                <div class="twrbo-h-margin-top-sm">
                                    <ul class="twrbo-c-list twrbo-c-list--data twrbo-c-list--small twrbo-c-list--small">
                                        <li ng-show="dealItem.startDay != '' &amp;&amp; dealItem.endDay != ''">
                                            <div class="twrbo-c-additionalicon">
                                                <img src="/content/dam/twrbo/images/icon/icon_clock_dark.svg" alt="" width="16" height="16">
                                                <span ng-bind="dealItem.startDay" class="ng-binding">2023/01/01</span>
                                                <span>~</span>
                                                <span ng-bind="dealItem.endDay" class="ng-binding">2023/12/31</span>
                                            </div>
                                        </li>
                                        <li ng-show="dealItem.hasOwnProperty('B') &amp;&amp; dealItem.B.length > 0" class="ng-hide">
                                            <div class="twrbo-c-additionalicon">
                                                <img src="/content/dam/twrbo/images/icon/icon_card_dark.svg" alt="" width="16" height="16">
                                                <span>適用
                                                    <!-- ngRepeat: card in dealItem.B -->
                                                </span>
                                            </div>
                                        </li>
                                        <li>
                                            <ul class="twrbo-l-listHorizontal twrbo-l-listHorizontal--additional twrbo-c-fSmall">
                                                <li ng-show="dealItem.phone != ''" class="ng-hide">
                                                    <div class="twrbo-c-additionalicon">
                                                        <img src="/content/dam/twrbo/images/icon/icon_phone_dark.svg" alt="" width="16" height="16">
                                                        <a ng-href="tel:" target="_parent" class="twrbo-h-linkEffect-url--gy twrbo-c-link--tel" href="tel:">
                                                            <span ng-bind="dealItem.phone" class="ng-binding"></span>
                                                        </a>
                                                    </div>
                                                </li>
                                                <li ng-show="dealItem.address != ''" class="ng-hide">
                                                    <div class="twrbo-c-additionalicon">
                                                        <img src="/content/dam/twrbo/images/icon/icon_location_dark.svg" alt="" width="16" height="16">
                                                        <a ng-click="clickPopup(dealItem.promId, dealItem.name, dealItem.promDesc, dealItem.address, dealItem.lng, dealItem.lat, dealItem.phone)" class="twrbo-h-linkEffect-url--gy">
                                                            <span>地址</span>
                                                        </a>
                                                    </div>
                                                </li>
                                                <li ng-show="dealItem.storeUrl != ''" class="ng-hide">
                                                    <div class="twrbo-c-additionalicon">
                                                        <img src="/content/dam/twrbo/images/icon/icon_global_dark.svg" alt="" width="16" height="16">
                                                        <a ng-href="" class="twrbo-h-linkEffect-url--gy">
                                                            <span>網址</span>
                                                        </a>
                                                    </div>
                                                </li>
                                                <li ng-show="dealItem.promUrl != ''">
                                                    <div class="twrbo-c-additionalicon">
                                                        <img src="/content/dam/twrbo/images/icon/icon_link_dark.svg" alt="" width="16" height="16">
                                                        <a ng-href="https://www.ctbcbank.com/content/dam/minisite/long/creditcard/foodsedm/index.html" class="twrbo-h-linkEffect-url--gy" href="https://www.ctbcbank.com/content/dam/minisite/long/creditcard/foodsedm/index.html">
                                                            <span>活動網頁</span>
                                                        </a>
                                                    </div>
                                                </li>
                                                <li ng-show="dealItem.notice != ''">
                                                    <div class="twrbo-c-additionalicon">
                                                        <img src="/content/dam/twrbo/images/icon/icon_notice_dark.svg" alt="" width="16" height="16">
                                                        <a ng-click="noticePopup(dealItem.notice)" class="twrbo-h-linkEffect-url--gy">
                                                            <span>注意事項</span>
                                                        </a>
                                                    </div>
                                                </li>
                                            </ul>
                                        </li>
                                    </ul>
                                </div>
                            </div>
                        </div>
                    </div>
                </div><!-- end ngRepeat: dealItem in dealList.promotionDetailList --><div ng-repeat="dealItem in dealList.promotionDetailList" class="twrbo-l-productCard twrbo-l-productCard--list ng-scope">
                    <div class="twrbo-l-productCard__thumb">
                        <span class="twrbo-c-thumb picturefill-background" style="background-image: url(&quot;/content/dam/twrbo/images/creditcard/offer/F202327.jpg&quot;); background-size: cover; background-repeat: no-repeat; background-position: 50% 50%;">
                            <span data-src="/content/dam/twrbo/images/creditcard/offer/F202327.jpg" data-src-default="/content/dam/twrbo/images/matchCard.png"></span>
                        </span>
                        <div class="twrbo-h-gutters-out-sm-v">
                            <ul class="twrbo-c-label twrbo-c-label--trim">
                                <li ng-show="dealItem.promTag != ''">
                                    <ul class="twrbo-c-label twrbo-c-label--promo twrbo-c-label--trim">
                                        <li>
                                            <i class="twrbo-c-iLabel twrbo-c-iLabel--fire"></i>
                                            <span ng-bind="dealItem.promTag" class="ng-binding">熱門</span>
                                        </li>
                                    </ul>
                                </li>
                                <!-- ngRepeat: tag in dealItem.C --><li ng-repeat="tag in dealItem.C" ng-show="dealItem.hasOwnProperty('C')" class="ng-scope">
                                    <a ng-click="onTagClick(tag.filterItemKey, tag.filterItemName)">
                                        <sapn ng-bind="tag.filterItemName" class="ng-binding">折扣優惠</sapn></a>
                                </li><!-- end ngRepeat: tag in dealItem.C -->
                            </ul>
                        </div>
                    </div>
                    <div class="twrbo-l-productCard__text">
                        <div class="twrbo-h-margin-bottom-md">
                            <span class="twrbo-c-h3 twrbo-c-link twrbo-c-link--ignoreEffect">
                                <span ng-bind="dealItem.name" class="ng-binding">台北凱撒大飯店</span>
                            </span>
                        </div>
                        <div class="twrbo-l-productTextCard">
                            <div class="twrbo-l-productTextCard__detail">
                                <p><span ng-bind-html="dealItem.promDesc" class="ng-binding">享8折優惠</span></p>
                                <div class="twrbo-h-margin-top-sm">
                                    <ul class="twrbo-c-list twrbo-c-list--data twrbo-c-list--small twrbo-c-list--small">
                                        <li ng-show="dealItem.startDay != '' &amp;&amp; dealItem.endDay != ''">
                                            <div class="twrbo-c-additionalicon">
                                                <img src="/content/dam/twrbo/images/icon/icon_clock_dark.svg" alt="" width="16" height="16">
                                                <span ng-bind="dealItem.startDay" class="ng-binding">2023/04/01</span>
                                                <span>~</span>
                                                <span ng-bind="dealItem.endDay" class="ng-binding">2023/12/31</span>
                                            </div>
                                        </li>
                                        <li ng-show="dealItem.hasOwnProperty('B') &amp;&amp; dealItem.B.length > 0" class="ng-hide">
                                            <div class="twrbo-c-additionalicon">
                                                <img src="/content/dam/twrbo/images/icon/icon_card_dark.svg" alt="" width="16" height="16">
                                                <span>適用
                                                    <!-- ngRepeat: card in dealItem.B -->
                                                </span>
                                            </div>
                                        </li>
                                        <li>
                                            <ul class="twrbo-l-listHorizontal twrbo-l-listHorizontal--additional twrbo-c-fSmall">
                                                <li ng-show="dealItem.phone != ''" class="ng-hide">
                                                    <div class="twrbo-c-additionalicon">
                                                        <img src="/content/dam/twrbo/images/icon/icon_phone_dark.svg" alt="" width="16" height="16">
                                                        <a ng-href="tel:" target="_parent" class="twrbo-h-linkEffect-url--gy twrbo-c-link--tel" href="tel:">
                                                            <span ng-bind="dealItem.phone" class="ng-binding"></span>
                                                        </a>
                                                    </div>
                                                </li>
                                                <li ng-show="dealItem.address != ''" class="ng-hide">
                                                    <div class="twrbo-c-additionalicon">
                                                        <img src="/content/dam/twrbo/images/icon/icon_location_dark.svg" alt="" width="16" height="16">
                                                        <a ng-click="clickPopup(dealItem.promId, dealItem.name, dealItem.promDesc, dealItem.address, dealItem.lng, dealItem.lat, dealItem.phone)" class="twrbo-h-linkEffect-url--gy">
                                                            <span>地址</span>
                                                        </a>
                                                    </div>
                                                </li>
                                                <li ng-show="dealItem.storeUrl != ''" class="ng-hide">
                                                    <div class="twrbo-c-additionalicon">
                                                        <img src="/content/dam/twrbo/images/icon/icon_global_dark.svg" alt="" width="16" height="16">
                                                        <a ng-href="" class="twrbo-h-linkEffect-url--gy">
                                                            <span>網址</span>
                                                        </a>
                                                    </div>
                                                </li>
                                                <li ng-show="dealItem.promUrl != ''">
                                                    <div class="twrbo-c-additionalicon">
                                                        <img src="/content/dam/twrbo/images/icon/icon_link_dark.svg" alt="" width="16" height="16">
                                                        <a ng-href="https://www.ctbcbank.com/content/dam/minisite/long/creditcard/foodsedm/index.html" class="twrbo-h-linkEffect-url--gy" href="https://www.ctbcbank.com/content/dam/minisite/long/creditcard/foodsedm/index.html">
                                                            <span>活動網頁</span>
                                                        </a>
                                                    </div>
                                                </li>
                                                <li ng-show="dealItem.notice != ''">
                                                    <div class="twrbo-c-additionalicon">
                                                        <img src="/content/dam/twrbo/images/icon/icon_notice_dark.svg" alt="" width="16" height="16">
                                                        <a ng-click="noticePopup(dealItem.notice)" class="twrbo-h-linkEffect-url--gy">
                                                            <span>注意事項</span>
                                                        </a>
                                                    </div>
                                                </li>
                                            </ul>
                                        </li>
                                    </ul>
                                </div>
                            </div>
                        </div>
                    </div>
                </div><!-- end ngRepeat: dealItem in dealList.promotionDetailList --><div ng-repeat="dealItem in dealList.promotionDetailList" class="twrbo-l-productCard twrbo-l-productCard--list ng-scope">
                    <div class="twrbo-l-productCard__thumb">
                        <span class="twrbo-c-thumb picturefill-background" style="background-image: url(&quot;/content/dam/twrbo/images/creditcard/offer/F202328.jpg&quot;); background-size: cover; background-repeat: no-repeat; background-position: 50% 50%;">
                            <span data-src="/content/dam/twrbo/images/creditcard/offer/F202328.jpg" data-src-default="/content/dam/twrbo/images/matchCard.png"></span>
                        </span>
                        <div class="twrbo-h-gutters-out-sm-v">
                            <ul class="twrbo-c-label twrbo-c-label--trim">
                                <li ng-show="dealItem.promTag != ''">
                                    <ul class="twrbo-c-label twrbo-c-label--promo twrbo-c-label--trim">
                                        <li>
                                            <i class="twrbo-c-iLabel twrbo-c-iLabel--fire"></i>
                                            <span ng-bind="dealItem.promTag" class="ng-binding">熱門</span>
                                        </li>
                                    </ul>
                                </li>
                                <!-- ngRepeat: tag in dealItem.C --><li ng-repeat="tag in dealItem.C" ng-show="dealItem.hasOwnProperty('C')" class="ng-scope">
                                    <a ng-click="onTagClick(tag.filterItemKey, tag.filterItemName)">
                                        <sapn ng-bind="tag.filterItemName" class="ng-binding">折扣優惠</sapn></a>
                                </li><!-- end ngRepeat: tag in dealItem.C -->
                            </ul>
                        </div>
                    </div>
                    <div class="twrbo-l-productCard__text">
                        <div class="twrbo-h-margin-bottom-md">
                            <span class="twrbo-c-h3 twrbo-c-link twrbo-c-link--ignoreEffect">
                                <span ng-bind="dealItem.name" class="ng-binding">青青燒肉</span>
                            </span>
                        </div>
                        <div class="twrbo-l-productTextCard">
                            <div class="twrbo-l-productTextCard__detail">
                                <p><span ng-bind-html="dealItem.promDesc" class="ng-binding">最優享9折優惠</span></p>
                                <div class="twrbo-h-margin-top-sm">
                                    <ul class="twrbo-c-list twrbo-c-list--data twrbo-c-list--small twrbo-c-list--small">
                                        <li ng-show="dealItem.startDay != '' &amp;&amp; dealItem.endDay != ''">
                                            <div class="twrbo-c-additionalicon">
                                                <img src="/content/dam/twrbo/images/icon/icon_clock_dark.svg" alt="" width="16" height="16">
                                                <span ng-bind="dealItem.startDay" class="ng-binding">2023/04/01</span>
                                                <span>~</span>
                                                <span ng-bind="dealItem.endDay" class="ng-binding">2023/12/31</span>
                                            </div>
                                        </li>
                                        <li ng-show="dealItem.hasOwnProperty('B') &amp;&amp; dealItem.B.length > 0" class="ng-hide">
                                            <div class="twrbo-c-additionalicon">
                                                <img src="/content/dam/twrbo/images/icon/icon_card_dark.svg" alt="" width="16" height="16">
                                                <span>適用
                                                    <!-- ngRepeat: card in dealItem.B -->
                                                </span>
                                            </div>
                                        </li>
                                        <li>
                                            <ul class="twrbo-l-listHorizontal twrbo-l-listHorizontal--additional twrbo-c-fSmall">
                                                <li ng-show="dealItem.phone != ''" class="ng-hide">
                                                    <div class="twrbo-c-additionalicon">
                                                        <img src="/content/dam/twrbo/images/icon/icon_phone_dark.svg" alt="" width="16" height="16">
                                                        <a ng-href="tel:" target="_parent" class="twrbo-h-linkEffect-url--gy twrbo-c-link--tel" href="tel:">
                                                            <span ng-bind="dealItem.phone" class="ng-binding"></span>
                                                        </a>
                                                    </div>
                                                </li>
                                                <li ng-show="dealItem.address != ''" class="ng-hide">
                                                    <div class="twrbo-c-additionalicon">
                                                        <img src="/content/dam/twrbo/images/icon/icon_location_dark.svg" alt="" width="16" height="16">
                                                        <a ng-click="clickPopup(dealItem.promId, dealItem.name, dealItem.promDesc, dealItem.address, dealItem.lng, dealItem.lat, dealItem.phone)" class="twrbo-h-linkEffect-url--gy">
                                                            <span>地址</span>
                                                        </a>
                                                    </div>
                                                </li>
                                                <li ng-show="dealItem.storeUrl != ''" class="ng-hide">
                                                    <div class="twrbo-c-additionalicon">
                                                        <img src="/content/dam/twrbo/images/icon/icon_global_dark.svg" alt="" width="16" height="16">
                                                        <a ng-href="" class="twrbo-h-linkEffect-url--gy">
                                                            <span>網址</span>
                                                        </a>
                                                    </div>
                                                </li>
                                                <li ng-show="dealItem.promUrl != ''">
                                                    <div class="twrbo-c-additionalicon">
                                                        <img src="/content/dam/twrbo/images/icon/icon_link_dark.svg" alt="" width="16" height="16">
                                                        <a ng-href="https://www.ctbcbank.com/content/dam/minisite/long/creditcard/foodsedm/index.html" class="twrbo-h-linkEffect-url--gy" href="https://www.ctbcbank.com/content/dam/minisite/long/creditcard/foodsedm/index.html">
                                                            <span>活動網頁</span>
                                                        </a>
                                                    </div>
                                                </li>
                                                <li ng-show="dealItem.notice != ''">
                                                    <div class="twrbo-c-additionalicon">
                                                        <img src="/content/dam/twrbo/images/icon/icon_notice_dark.svg" alt="" width="16" height="16">
                                                        <a ng-click="noticePopup(dealItem.notice)" class="twrbo-h-linkEffect-url--gy">
                                                            <span>注意事項</span>
                                                        </a>
                                                    </div>
                                                </li>
                                            </ul>
                                        </li>
                                    </ul>
                                </div>
                            </div>
                        </div>
                    </div>
                </div><!-- end ngRepeat: dealItem in dealList.promotionDetailList --><div ng-repeat="dealItem in dealList.promotionDetailList" class="twrbo-l-productCard twrbo-l-productCard--list ng-scope">
                    <div class="twrbo-l-productCard__thumb">
                        <span class="twrbo-c-thumb picturefill-background" style="background-image: url(&quot;/content/dam/twrbo/images/creditcard/offer/F202329.jpg&quot;); background-size: cover; background-repeat: no-repeat; background-position: 50% 50%;">
                            <span data-src="/content/dam/twrbo/images/creditcard/offer/F202329.jpg" data-src-default="/content/dam/twrbo/images/matchCard.png"></span>
                        </span>
                        <div class="twrbo-h-gutters-out-sm-v">
                            <ul class="twrbo-c-label twrbo-c-label--trim">
                                <li ng-show="dealItem.promTag != ''">
                                    <ul class="twrbo-c-label twrbo-c-label--promo twrbo-c-label--trim">
                                        <li>
                                            <i class="twrbo-c-iLabel twrbo-c-iLabel--fire"></i>
                                            <span ng-bind="dealItem.promTag" class="ng-binding">熱門</span>
                                        </li>
                                    </ul>
                                </li>
                                <!-- ngRepeat: tag in dealItem.C --><li ng-repeat="tag in dealItem.C" ng-show="dealItem.hasOwnProperty('C')" class="ng-scope">
                                    <a ng-click="onTagClick(tag.filterItemKey, tag.filterItemName)">
                                        <sapn ng-bind="tag.filterItemName" class="ng-binding">折扣優惠</sapn></a>
                                </li><!-- end ngRepeat: tag in dealItem.C -->
                            </ul>
                        </div>
                    </div>
                    <div class="twrbo-l-productCard__text">
                        <div class="twrbo-h-margin-bottom-md">
                            <span class="twrbo-c-h3 twrbo-c-link twrbo-c-link--ignoreEffect">
                                <span ng-bind="dealItem.name" class="ng-binding">十色鍋物</span>
                            </span>
                        </div>
                        <div class="twrbo-l-productTextCard">
                            <div class="twrbo-l-productTextCard__detail">
                                <p><span ng-bind-html="dealItem.promDesc" class="ng-binding">最優享7折優惠</span></p>
                                <div class="twrbo-h-margin-top-sm">
                                    <ul class="twrbo-c-list twrbo-c-list--data twrbo-c-list--small twrbo-c-list--small">
                                        <li ng-show="dealItem.startDay != '' &amp;&amp; dealItem.endDay != ''">
                                            <div class="twrbo-c-additionalicon">
                                                <img src="/content/dam/twrbo/images/icon/icon_clock_dark.svg" alt="" width="16" height="16">
                                                <span ng-bind="dealItem.startDay" class="ng-binding">2023/04/01</span>
                                                <span>~</span>
                                                <span ng-bind="dealItem.endDay" class="ng-binding">2023/12/31</span>
                                            </div>
                                        </li>
                                        <li ng-show="dealItem.hasOwnProperty('B') &amp;&amp; dealItem.B.length > 0" class="ng-hide">
                                            <div class="twrbo-c-additionalicon">
                                                <img src="/content/dam/twrbo/images/icon/icon_card_dark.svg" alt="" width="16" height="16">
                                                <span>適用
                                                    <!-- ngRepeat: card in dealItem.B -->
                                                </span>
                                            </div>
                                        </li>
                                        <li>
                                            <ul class="twrbo-l-listHorizontal twrbo-l-listHorizontal--additional twrbo-c-fSmall">
                                                <li ng-show="dealItem.phone != ''" class="ng-hide">
                                                    <div class="twrbo-c-additionalicon">
                                                        <img src="/content/dam/twrbo/images/icon/icon_phone_dark.svg" alt="" width="16" height="16">
                                                        <a ng-href="tel:" target="_parent" class="twrbo-h-linkEffect-url--gy twrbo-c-link--tel" href="tel:">
                                                            <span ng-bind="dealItem.phone" class="ng-binding"></span>
                                                        </a>
                                                    </div>
                                                </li>
                                                <li ng-show="dealItem.address != ''" class="ng-hide">
                                                    <div class="twrbo-c-additionalicon">
                                                        <img src="/content/dam/twrbo/images/icon/icon_location_dark.svg" alt="" width="16" height="16">
                                                        <a ng-click="clickPopup(dealItem.promId, dealItem.name, dealItem.promDesc, dealItem.address, dealItem.lng, dealItem.lat, dealItem.phone)" class="twrbo-h-linkEffect-url--gy">
                                                            <span>地址</span>
                                                        </a>
                                                    </div>
                                                </li>
                                                <li ng-show="dealItem.storeUrl != ''" class="ng-hide">
                                                    <div class="twrbo-c-additionalicon">
                                                        <img src="/content/dam/twrbo/images/icon/icon_global_dark.svg" alt="" width="16" height="16">
                                                        <a ng-href="" class="twrbo-h-linkEffect-url--gy">
                                                            <span>網址</span>
                                                        </a>
                                                    </div>
                                                </li>
                                                <li ng-show="dealItem.promUrl != ''">
                                                    <div class="twrbo-c-additionalicon">
                                                        <img src="/content/dam/twrbo/images/icon/icon_link_dark.svg" alt="" width="16" height="16">
                                                        <a ng-href="https://www.ctbcbank.com/content/dam/minisite/long/creditcard/foodsedm/index.html" class="twrbo-h-linkEffect-url--gy" href="https://www.ctbcbank.com/content/dam/minisite/long/creditcard/foodsedm/index.html">
                                                            <span>活動網頁</span>
                                                        </a>
                                                    </div>
                                                </li>
                                                <li ng-show="dealItem.notice != ''">
                                                    <div class="twrbo-c-additionalicon">
                                                        <img src="/content/dam/twrbo/images/icon/icon_notice_dark.svg" alt="" width="16" height="16">
                                                        <a ng-click="noticePopup(dealItem.notice)" class="twrbo-h-linkEffect-url--gy">
                                                            <span>注意事項</span>
                                                        </a>
                                                    </div>
                                                </li>
                                            </ul>
                                        </li>
                                    </ul>
                                </div>
                            </div>
                        </div>
                    </div>
                </div><!-- end ngRepeat: dealItem in dealList.promotionDetailList -->
            </div>
            <div class="twrbo-l-resultList__noResult ng-hide" ng-show="!isDealListSuccess ||  dealList.totalDataRows == 0 || dealList.promotionDetailList == 0">
                <div class="twrbo-c-tac">
                    <img src="/content/dam/twrbo/images/littleb/b_noResult.svg">
                </div>
                <h3 class="twrbo-c-h3 twrbo-l-resultList__noResult">很抱歉，目前沒有符合條件的優惠</h3>
                <div class="twrbo-c-tips">您可重新勾選篩選條件或查看其他優惠頁面！</div>
            </div>
        </div>
"""

soup = BeautifulSoup(html, 'html.parser')

# 從每個class為'twrbo-h-margin-bottom-md'的div擷取資料
result_data = []

for div in soup.find_all('div', class_='twrbo-h-margin-bottom-md'):
    deal_name = div.find('span', class_='ng-binding').get_text(strip=True)
    
    # 從相應的class為'twrbo-l-productTextCard__detail'的div擷取資料
    detail_div = div.find_next('div', class_='twrbo-l-productTextCard__detail')
    
    # 從巢狀元素中擷取資料
    prom_desc = detail_div.find('span', class_='ng-binding').get_text(strip=True)
    start_day = detail_div.find('span', {'ng-bind': 'dealItem.startDay', 'class': 'ng-binding'}).get_text(strip=True)
    end_day = detail_div.find('span', {'ng-bind': 'dealItem.endDay', 'class': 'ng-binding'}).get_text(strip=True)
    
    card_filter_item_names = [item.get_text(strip=True) for item in detail_div.find_all('span', {'ng-bind': 'card.filterItemName', 'class': 'ng-binding'})]
    
    result_data.append({
        '優惠名稱': deal_name,
        '促銷描述': prom_desc,
        '開始日期': start_day,
        '結束日期': end_day,
        '適用卡片範疇': '/'.join(card_filter_item_names)
    })

# 將資料保存到CSV檔案
csv_file_path = '中信餐飲短期優惠3.csv'
csv_columns = ['優惠名稱', '促銷描述', '開始日期', '結束日期', '適用卡片範疇']

with open(csv_file_path, 'w', newline='', encoding='utf-8-sig') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=csv_columns)
    writer.writeheader()
    for data in result_data:
        writer.writerow(data)

print(f'資料已經擷取並保存到 {csv_file_path}')