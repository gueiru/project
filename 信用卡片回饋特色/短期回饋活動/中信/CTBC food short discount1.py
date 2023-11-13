import csv
from bs4 import BeautifulSoup

html = """
    <div class="twrbo-l-result__data">
            <div class="twrbo-l-resultList" data-list-id="creditcard" ng-show="isDealListSuccess &amp;&amp; dealList.totalDataRows > 0 ">
                
                <!-- ngRepeat: dealItem in dealList.promotionDetailList --><div ng-repeat="dealItem in dealList.promotionDetailList" class="twrbo-l-productCard twrbo-l-productCard--list ng-scope">
                    <div class="twrbo-l-productCard__thumb">
                        <span class="twrbo-c-thumb picturefill-background" style="background-image: url(&quot;/content/dam/twrbo/images/creditcard/offer/FOOD2301.jpg&quot;); background-size: cover; background-repeat: no-repeat; background-position: 50% 50%;">
                            <span data-src="/content/dam/twrbo/images/creditcard/offer/FOOD2301.jpg" data-src-default="/content/dam/twrbo/images/matchCard.png"></span>
                        </span>
                        <div class="twrbo-h-gutters-out-sm-v">
                            <ul class="twrbo-c-label twrbo-c-label--trim">
                                <li ng-show="dealItem.promTag != ''" class="ng-hide">
                                    <ul class="twrbo-c-label twrbo-c-label--promo twrbo-c-label--trim">
                                        <li>
                                            <i class="twrbo-c-iLabel twrbo-c-iLabel--fire"></i>
                                            <span ng-bind="dealItem.promTag" class="ng-binding"></span>
                                        </li>
                                    </ul>
                                </li>
                                <!-- ngRepeat: tag in dealItem.C --><li ng-repeat="tag in dealItem.C" ng-show="dealItem.hasOwnProperty('C')" class="ng-scope">
                                    <a ng-click="onTagClick(tag.filterItemKey, tag.filterItemName)">
                                        <sapn ng-bind="tag.filterItemName" class="ng-binding">點數回饋</sapn></a>
                                </li><!-- end ngRepeat: tag in dealItem.C -->
                            </ul>
                        </div>
                    </div>
                    <div class="twrbo-l-productCard__text">
                        <div class="twrbo-h-margin-bottom-md">
                            <span class="twrbo-c-h3 twrbo-c-link twrbo-c-link--ignoreEffect">
                                <span ng-bind="dealItem.name" class="ng-binding">天冷吃個鍋</span>
                            </span>
                        </div>
                        <div class="twrbo-l-productTextCard">
                            <div class="twrbo-l-productTextCard__detail">
                                <p><span ng-bind-html="dealItem.promDesc" class="ng-binding">指定餐廳刷中信卡單月累積滿額贈3%刷卡金(需登錄)</span></p>
                                <div class="twrbo-h-margin-top-sm">
                                    <ul class="twrbo-c-list twrbo-c-list--data twrbo-c-list--small twrbo-c-list--small">
                                        <li ng-show="dealItem.startDay != '' &amp;&amp; dealItem.endDay != ''">
                                            <div class="twrbo-c-additionalicon">
                                                <img src="/content/dam/twrbo/images/icon/icon_clock_dark.svg" alt="" width="16" height="16">
                                                <span ng-bind="dealItem.startDay" class="ng-binding">2023/10/01</span>
                                                <span>~</span>
                                                <span ng-bind="dealItem.endDay" class="ng-binding">2023/12/31</span>
                                            </div>
                                        </li>
                                        <li ng-show="dealItem.hasOwnProperty('B') &amp;&amp; dealItem.B.length > 0">
                                            <div class="twrbo-c-additionalicon">
                                                <img src="/content/dam/twrbo/images/icon/icon_card_dark.svg" alt="" width="16" height="16">
                                                <span>適用
                                                    <!-- ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">無限卡</span>
                                                        <span ng-show="!$last">/</span>
                                                    </span><!-- end ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">世界卡</span>
                                                        <span ng-show="!$last">/</span>
                                                    </span><!-- end ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">極緻卡</span>
                                                        <span ng-show="!$last">/</span>
                                                    </span><!-- end ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">御璽卡</span>
                                                        <span ng-show="!$last">/</span>
                                                    </span><!-- end ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">鈦金卡</span>
                                                        <span ng-show="!$last">/</span>
                                                    </span><!-- end ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">晶緻卡</span>
                                                        <span ng-show="!$last">/</span>
                                                    </span><!-- end ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">聯名認同卡</span>
                                                        <span ng-show="!$last">/</span>
                                                    </span><!-- end ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">所有卡</span>
                                                        <span ng-show="!$last" class="ng-hide">/</span>
                                                    </span><!-- end ngRepeat: card in dealItem.B -->
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
                                                        <a ng-href="https://www.ctbcbank.com/content/dam/minisite/long/creditcard/food2023/index.html" class="twrbo-h-linkEffect-url--gy" href="https://www.ctbcbank.com/content/dam/minisite/long/creditcard/food2023/index.html">
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
                        <span class="twrbo-c-thumb picturefill-background" style="background-image: url(&quot;/content/dam/twrbo/images/creditcard/offer/WOW09.jpg&quot;); background-size: cover; background-repeat: no-repeat; background-position: 50% 50%;">
                            <span data-src="/content/dam/twrbo/images/creditcard/offer/WOW09.jpg" data-src-default="/content/dam/twrbo/images/matchCard.png"></span>
                        </span>
                        <div class="twrbo-h-gutters-out-sm-v">
                            <ul class="twrbo-c-label twrbo-c-label--trim">
                                <li ng-show="dealItem.promTag != ''" class="ng-hide">
                                    <ul class="twrbo-c-label twrbo-c-label--promo twrbo-c-label--trim">
                                        <li>
                                            <i class="twrbo-c-iLabel twrbo-c-iLabel--fire"></i>
                                            <span ng-bind="dealItem.promTag" class="ng-binding"></span>
                                        </li>
                                    </ul>
                                </li>
                                <!-- ngRepeat: tag in dealItem.C --><li ng-repeat="tag in dealItem.C" ng-show="dealItem.hasOwnProperty('C')" class="ng-scope">
                                    <a ng-click="onTagClick(tag.filterItemKey, tag.filterItemName)">
                                        <sapn ng-bind="tag.filterItemName" class="ng-binding">點數回饋</sapn></a>
                                </li><!-- end ngRepeat: tag in dealItem.C -->
                            </ul>
                        </div>
                    </div>
                    <div class="twrbo-l-productCard__text">
                        <div class="twrbo-h-margin-bottom-md">
                            <span class="twrbo-c-h3 twrbo-c-link twrbo-c-link--ignoreEffect">
                                <span ng-bind="dealItem.name" class="ng-binding">聚日式鍋物</span>
                            </span>
                        </div>
                        <div class="twrbo-l-productTextCard">
                            <div class="twrbo-l-productTextCard__detail">
                                <p><span ng-bind-html="dealItem.promDesc" class="ng-binding">使用王品瘋美食App電子錢包瘋Pay且綁定中信卡消費付款，享週六~週日10%瘋點數回饋、週一~週五3%瘋點數回饋。</span></p>
                                <div class="twrbo-h-margin-top-sm">
                                    <ul class="twrbo-c-list twrbo-c-list--data twrbo-c-list--small twrbo-c-list--small">
                                        <li ng-show="dealItem.startDay != '' &amp;&amp; dealItem.endDay != ''">
                                            <div class="twrbo-c-additionalicon">
                                                <img src="/content/dam/twrbo/images/icon/icon_clock_dark.svg" alt="" width="16" height="16">
                                                <span ng-bind="dealItem.startDay" class="ng-binding">2023/10/01</span>
                                                <span>~</span>
                                                <span ng-bind="dealItem.endDay" class="ng-binding">2023/12/31</span>
                                            </div>
                                        </li>
                                        <li ng-show="dealItem.hasOwnProperty('B') &amp;&amp; dealItem.B.length > 0">
                                            <div class="twrbo-c-additionalicon">
                                                <img src="/content/dam/twrbo/images/icon/icon_card_dark.svg" alt="" width="16" height="16">
                                                <span>適用
                                                    <!-- ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">無限卡</span>
                                                        <span ng-show="!$last">/</span>
                                                    </span><!-- end ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">世界卡</span>
                                                        <span ng-show="!$last">/</span>
                                                    </span><!-- end ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">極緻卡</span>
                                                        <span ng-show="!$last">/</span>
                                                    </span><!-- end ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">御璽卡</span>
                                                        <span ng-show="!$last">/</span>
                                                    </span><!-- end ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">鈦金卡</span>
                                                        <span ng-show="!$last">/</span>
                                                    </span><!-- end ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">晶緻卡</span>
                                                        <span ng-show="!$last">/</span>
                                                    </span><!-- end ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">聯名認同卡</span>
                                                        <span ng-show="!$last">/</span>
                                                    </span><!-- end ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">所有卡</span>
                                                        <span ng-show="!$last" class="ng-hide">/</span>
                                                    </span><!-- end ngRepeat: card in dealItem.B -->
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
                                                        <a ng-href="https://www.ctbcbank.com/content/dam/minisite/long/creditcard/wowapp/index.html" class="twrbo-h-linkEffect-url--gy" href="https://www.ctbcbank.com/content/dam/minisite/long/creditcard/wowapp/index.html">
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
                        <span class="twrbo-c-thumb picturefill-background" style="background-image: url(&quot;/content/dam/twrbo/images/creditcard/offer/MC001.jpg&quot;); background-size: cover; background-repeat: no-repeat; background-position: 50% 50%;">
                            <span data-src="/content/dam/twrbo/images/creditcard/offer/MC001.jpg" data-src-default="/content/dam/twrbo/images/matchCard.png"></span>
                        </span>
                        <div class="twrbo-h-gutters-out-sm-v">
                            <ul class="twrbo-c-label twrbo-c-label--trim">
                                <li ng-show="dealItem.promTag != ''" class="ng-hide">
                                    <ul class="twrbo-c-label twrbo-c-label--promo twrbo-c-label--trim">
                                        <li>
                                            <i class="twrbo-c-iLabel twrbo-c-iLabel--fire"></i>
                                            <span ng-bind="dealItem.promTag" class="ng-binding"></span>
                                        </li>
                                    </ul>
                                </li>
                                <!-- ngRepeat: tag in dealItem.C -->
                            </ul>
                        </div>
                    </div>
                    <div class="twrbo-l-productCard__text">
                        <div class="twrbo-h-margin-bottom-md">
                            <span class="twrbo-c-h3 twrbo-c-link twrbo-c-link--ignoreEffect">
                                <span ng-bind="dealItem.name" class="ng-binding">麥當勞冰氛日</span>
                            </span>
                        </div>
                        <div class="twrbo-l-productTextCard">
                            <div class="twrbo-l-productTextCard__detail">
                                <p><span ng-bind-html="dealItem.promDesc" class="ng-binding">每週一刷中信卡單筆滿99元贈【蛋捲冰淇淋兌換券】乙張，刷LINE Pay卡再享LINE POINTS 3%回饋</span></p>
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
                                                        <a ng-href="https://www.ctbcbank.com/content/dam/minisite/long/creditcard/mcdonalds/index.html" class="twrbo-h-linkEffect-url--gy" href="https://www.ctbcbank.com/content/dam/minisite/long/creditcard/mcdonalds/index.html">
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
                        <span class="twrbo-c-thumb picturefill-background" style="background-image: url(&quot;/content/dam/twrbo/images/creditcard/offer/Redeem000097.jpg&quot;); background-size: cover; background-repeat: no-repeat; background-position: 50% 50%;">
                            <span data-src="/content/dam/twrbo/images/creditcard/offer/Redeem000097.jpg" data-src-default="/content/dam/twrbo/images/matchCard.png"></span>
                        </span>
                        <div class="twrbo-h-gutters-out-sm-v">
                            <ul class="twrbo-c-label twrbo-c-label--trim">
                                <li ng-show="dealItem.promTag != ''" class="ng-hide">
                                    <ul class="twrbo-c-label twrbo-c-label--promo twrbo-c-label--trim">
                                        <li>
                                            <i class="twrbo-c-iLabel twrbo-c-iLabel--fire"></i>
                                            <span ng-bind="dealItem.promTag" class="ng-binding"></span>
                                        </li>
                                    </ul>
                                </li>
                                <!-- ngRepeat: tag in dealItem.C --><li ng-repeat="tag in dealItem.C" ng-show="dealItem.hasOwnProperty('C')" class="ng-scope">
                                    <a ng-click="onTagClick(tag.filterItemKey, tag.filterItemName)">
                                        <sapn ng-bind="tag.filterItemName" class="ng-binding">紅利折抵</sapn></a>
                                </li><!-- end ngRepeat: tag in dealItem.C -->
                            </ul>
                        </div>
                    </div>
                    <div class="twrbo-l-productCard__text">
                        <div class="twrbo-h-margin-bottom-md">
                            <span class="twrbo-c-h3 twrbo-c-link twrbo-c-link--ignoreEffect">
                                <span ng-bind="dealItem.name" class="ng-binding">春一籠港式茶樓</span>
                            </span>
                        </div>
                        <div class="twrbo-l-productTextCard">
                            <div class="twrbo-l-productTextCard__detail">
                                <p><span ng-bind-html="dealItem.promDesc" class="ng-binding">*中信卡紅利點數每1,000點折抵NT60元，折抵上限為單筆消費金額100%。</span></p>
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
                                        <li ng-show="dealItem.hasOwnProperty('B') &amp;&amp; dealItem.B.length > 0">
                                            <div class="twrbo-c-additionalicon">
                                                <img src="/content/dam/twrbo/images/icon/icon_card_dark.svg" alt="" width="16" height="16">
                                                <span>適用
                                                    <!-- ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">所有卡</span>
                                                        <span ng-show="!$last" class="ng-hide">/</span>
                                                    </span><!-- end ngRepeat: card in dealItem.B -->
                                                </span>
                                            </div>
                                        </li>
                                        <li>
                                            <ul class="twrbo-l-listHorizontal twrbo-l-listHorizontal--additional twrbo-c-fSmall">
                                                <li ng-show="dealItem.phone != ''">
                                                    <div class="twrbo-c-additionalicon">
                                                        <img src="/content/dam/twrbo/images/icon/icon_phone_dark.svg" alt="" width="16" height="16">
                                                        <a ng-href="tel:062959666" target="_parent" class="twrbo-h-linkEffect-url--gy twrbo-c-link--tel" href="tel:062959666">
                                                            <span ng-bind="dealItem.phone" class="ng-binding">06-2959666</span>
                                                        </a>
                                                    </div>
                                                </li>
                                                <li ng-show="dealItem.address != ''">
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
                                                <li ng-show="dealItem.promUrl != ''" class="ng-hide">
                                                    <div class="twrbo-c-additionalicon">
                                                        <img src="/content/dam/twrbo/images/icon/icon_link_dark.svg" alt="" width="16" height="16">
                                                        <a ng-href="" class="twrbo-h-linkEffect-url--gy">
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
                        <span class="twrbo-c-thumb picturefill-background" style="background-image: url(&quot;/content/dam/twrbo/images/creditcard/offer/WOW32.jpg&quot;); background-size: cover; background-repeat: no-repeat; background-position: 50% 50%;">
                            <span data-src="/content/dam/twrbo/images/creditcard/offer/WOW32.jpg" data-src-default="/content/dam/twrbo/images/matchCard.png"></span>
                        </span>
                        <div class="twrbo-h-gutters-out-sm-v">
                            <ul class="twrbo-c-label twrbo-c-label--trim">
                                <li ng-show="dealItem.promTag != ''" class="ng-hide">
                                    <ul class="twrbo-c-label twrbo-c-label--promo twrbo-c-label--trim">
                                        <li>
                                            <i class="twrbo-c-iLabel twrbo-c-iLabel--fire"></i>
                                            <span ng-bind="dealItem.promTag" class="ng-binding"></span>
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
                                <span ng-bind="dealItem.name" class="ng-binding">王品牛排</span>
                            </span>
                        </div>
                        <div class="twrbo-l-productTextCard">
                            <div class="twrbo-l-productTextCard__detail">
                                <p><span ng-bind-html="dealItem.promDesc" class="ng-binding">刷中信卡內用兩客套餐，款待香蒜海螺佐大蝦乙份(價值688元)</span></p>
                                <div class="twrbo-h-margin-top-sm">
                                    <ul class="twrbo-c-list twrbo-c-list--data twrbo-c-list--small twrbo-c-list--small">
                                        <li ng-show="dealItem.startDay != '' &amp;&amp; dealItem.endDay != ''">
                                            <div class="twrbo-c-additionalicon">
                                                <img src="/content/dam/twrbo/images/icon/icon_clock_dark.svg" alt="" width="16" height="16">
                                                <span ng-bind="dealItem.startDay" class="ng-binding">2023/11/01</span>
                                                <span>~</span>
                                                <span ng-bind="dealItem.endDay" class="ng-binding">2023/12/31</span>
                                            </div>
                                        </li>
                                        <li ng-show="dealItem.hasOwnProperty('B') &amp;&amp; dealItem.B.length > 0">
                                            <div class="twrbo-c-additionalicon">
                                                <img src="/content/dam/twrbo/images/icon/icon_card_dark.svg" alt="" width="16" height="16">
                                                <span>適用
                                                    <!-- ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">無限卡</span>
                                                        <span ng-show="!$last">/</span>
                                                    </span><!-- end ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">世界卡</span>
                                                        <span ng-show="!$last">/</span>
                                                    </span><!-- end ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">極緻卡</span>
                                                        <span ng-show="!$last">/</span>
                                                    </span><!-- end ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">御璽卡</span>
                                                        <span ng-show="!$last">/</span>
                                                    </span><!-- end ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">鈦金卡</span>
                                                        <span ng-show="!$last">/</span>
                                                    </span><!-- end ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">晶緻卡</span>
                                                        <span ng-show="!$last">/</span>
                                                    </span><!-- end ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">聯名認同卡</span>
                                                        <span ng-show="!$last">/</span>
                                                    </span><!-- end ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">所有卡</span>
                                                        <span ng-show="!$last" class="ng-hide">/</span>
                                                    </span><!-- end ngRepeat: card in dealItem.B -->
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
                                                        <a ng-href="https://mkt.ctbcbank.com/long/creditcard/wangsteak/index.html" class="twrbo-h-linkEffect-url--gy" href="https://mkt.ctbcbank.com/long/creditcard/wangsteak/index.html">
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
                        <span class="twrbo-c-thumb picturefill-background" style="background-image: url(&quot;/content/dam/twrbo/images/creditcard/offer/WOW10.jpg&quot;); background-size: cover; background-repeat: no-repeat; background-position: 50% 50%;">
                            <span data-src="/content/dam/twrbo/images/creditcard/offer/WOW10.jpg" data-src-default="/content/dam/twrbo/images/matchCard.png"></span>
                        </span>
                        <div class="twrbo-h-gutters-out-sm-v">
                            <ul class="twrbo-c-label twrbo-c-label--trim">
                                <li ng-show="dealItem.promTag != ''" class="ng-hide">
                                    <ul class="twrbo-c-label twrbo-c-label--promo twrbo-c-label--trim">
                                        <li>
                                            <i class="twrbo-c-iLabel twrbo-c-iLabel--fire"></i>
                                            <span ng-bind="dealItem.promTag" class="ng-binding"></span>
                                        </li>
                                    </ul>
                                </li>
                                <!-- ngRepeat: tag in dealItem.C --><li ng-repeat="tag in dealItem.C" ng-show="dealItem.hasOwnProperty('C')" class="ng-scope">
                                    <a ng-click="onTagClick(tag.filterItemKey, tag.filterItemName)">
                                        <sapn ng-bind="tag.filterItemName" class="ng-binding">點數回饋</sapn></a>
                                </li><!-- end ngRepeat: tag in dealItem.C -->
                            </ul>
                        </div>
                    </div>
                    <div class="twrbo-l-productCard__text">
                        <div class="twrbo-h-margin-bottom-md">
                            <span class="twrbo-c-h3 twrbo-c-link twrbo-c-link--ignoreEffect">
                                <span ng-bind="dealItem.name" class="ng-binding">享鴨 烤鴨與中華料理</span>
                            </span>
                        </div>
                        <div class="twrbo-l-productTextCard">
                            <div class="twrbo-l-productTextCard__detail">
                                <p><span ng-bind-html="dealItem.promDesc" class="ng-binding">使用王品瘋美食App電子錢包瘋Pay且綁定中信卡消費付款，享週六~週日10%瘋點數回饋、週一~週五3%瘋點數回饋。</span></p>
                                <div class="twrbo-h-margin-top-sm">
                                    <ul class="twrbo-c-list twrbo-c-list--data twrbo-c-list--small twrbo-c-list--small">
                                        <li ng-show="dealItem.startDay != '' &amp;&amp; dealItem.endDay != ''">
                                            <div class="twrbo-c-additionalicon">
                                                <img src="/content/dam/twrbo/images/icon/icon_clock_dark.svg" alt="" width="16" height="16">
                                                <span ng-bind="dealItem.startDay" class="ng-binding">2023/10/01</span>
                                                <span>~</span>
                                                <span ng-bind="dealItem.endDay" class="ng-binding">2023/12/31</span>
                                            </div>
                                        </li>
                                        <li ng-show="dealItem.hasOwnProperty('B') &amp;&amp; dealItem.B.length > 0">
                                            <div class="twrbo-c-additionalicon">
                                                <img src="/content/dam/twrbo/images/icon/icon_card_dark.svg" alt="" width="16" height="16">
                                                <span>適用
                                                    <!-- ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">無限卡</span>
                                                        <span ng-show="!$last">/</span>
                                                    </span><!-- end ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">世界卡</span>
                                                        <span ng-show="!$last">/</span>
                                                    </span><!-- end ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">極緻卡</span>
                                                        <span ng-show="!$last">/</span>
                                                    </span><!-- end ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">御璽卡</span>
                                                        <span ng-show="!$last">/</span>
                                                    </span><!-- end ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">鈦金卡</span>
                                                        <span ng-show="!$last">/</span>
                                                    </span><!-- end ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">晶緻卡</span>
                                                        <span ng-show="!$last">/</span>
                                                    </span><!-- end ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">聯名認同卡</span>
                                                        <span ng-show="!$last">/</span>
                                                    </span><!-- end ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">所有卡</span>
                                                        <span ng-show="!$last" class="ng-hide">/</span>
                                                    </span><!-- end ngRepeat: card in dealItem.B -->
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
                                                        <a ng-href="https://www.ctbcbank.com/content/dam/minisite/long/creditcard/wowapp/index.html" class="twrbo-h-linkEffect-url--gy" href="https://www.ctbcbank.com/content/dam/minisite/long/creditcard/wowapp/index.html">
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
                        <span class="twrbo-c-thumb picturefill-background" style="background-image: url(&quot;/content/dam/twrbo/images/creditcard/offer/MC001.jpg&quot;); background-size: cover; background-repeat: no-repeat; background-position: 50% 50%;">
                            <span data-src="/content/dam/twrbo/images/creditcard/offer/MC001.jpg" data-src-default="/content/dam/twrbo/images/matchCard.png"></span>
                        </span>
                        <div class="twrbo-h-gutters-out-sm-v">
                            <ul class="twrbo-c-label twrbo-c-label--trim">
                                <li ng-show="dealItem.promTag != ''" class="ng-hide">
                                    <ul class="twrbo-c-label twrbo-c-label--promo twrbo-c-label--trim">
                                        <li>
                                            <i class="twrbo-c-iLabel twrbo-c-iLabel--fire"></i>
                                            <span ng-bind="dealItem.promTag" class="ng-binding"></span>
                                        </li>
                                    </ul>
                                </li>
                                <!-- ngRepeat: tag in dealItem.C -->
                            </ul>
                        </div>
                    </div>
                    <div class="twrbo-l-productCard__text">
                        <div class="twrbo-h-margin-bottom-md">
                            <span class="twrbo-c-h3 twrbo-c-link twrbo-c-link--ignoreEffect">
                                <span ng-bind="dealItem.name" class="ng-binding">麥當勞歡樂送</span>
                            </span>
                        </div>
                        <div class="twrbo-l-productTextCard">
                            <div class="twrbo-l-productTextCard__detail">
                                <p><span ng-bind-html="dealItem.promDesc" class="ng-binding">歡樂送訂餐刷中信卡，單筆滿199元贈最高59元刷卡金</span></p>
                                <div class="twrbo-h-margin-top-sm">
                                    <ul class="twrbo-c-list twrbo-c-list--data twrbo-c-list--small twrbo-c-list--small">
                                        <li ng-show="dealItem.startDay != '' &amp;&amp; dealItem.endDay != ''">
                                            <div class="twrbo-c-additionalicon">
                                                <img src="/content/dam/twrbo/images/icon/icon_clock_dark.svg" alt="" width="16" height="16">
                                                <span ng-bind="dealItem.startDay" class="ng-binding">2023/10/01</span>
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
                                                        <a ng-href="https://www.ctbcbank.com/content/dam/minisite/long/creditcard/mcdonalds/index.html" class="twrbo-h-linkEffect-url--gy" href="https://www.ctbcbank.com/content/dam/minisite/long/creditcard/mcdonalds/index.html">
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
                        <span class="twrbo-c-thumb picturefill-background" style="background-image: url(&quot;/content/dam/twrbo/images/creditcard/offer/Redeem000098.jpg&quot;); background-size: cover; background-repeat: no-repeat; background-position: 50% 50%;">
                            <span data-src="/content/dam/twrbo/images/creditcard/offer/Redeem000098.jpg" data-src-default="/content/dam/twrbo/images/matchCard.png"></span>
                        </span>
                        <div class="twrbo-h-gutters-out-sm-v">
                            <ul class="twrbo-c-label twrbo-c-label--trim">
                                <li ng-show="dealItem.promTag != ''" class="ng-hide">
                                    <ul class="twrbo-c-label twrbo-c-label--promo twrbo-c-label--trim">
                                        <li>
                                            <i class="twrbo-c-iLabel twrbo-c-iLabel--fire"></i>
                                            <span ng-bind="dealItem.promTag" class="ng-binding"></span>
                                        </li>
                                    </ul>
                                </li>
                                <!-- ngRepeat: tag in dealItem.C --><li ng-repeat="tag in dealItem.C" ng-show="dealItem.hasOwnProperty('C')" class="ng-scope">
                                    <a ng-click="onTagClick(tag.filterItemKey, tag.filterItemName)">
                                        <sapn ng-bind="tag.filterItemName" class="ng-binding">紅利折抵</sapn></a>
                                </li><!-- end ngRepeat: tag in dealItem.C -->
                            </ul>
                        </div>
                    </div>
                    <div class="twrbo-l-productCard__text">
                        <div class="twrbo-h-margin-bottom-md">
                            <span class="twrbo-c-h3 twrbo-c-link twrbo-c-link--ignoreEffect">
                                <span ng-bind="dealItem.name" class="ng-binding">春一籠港式茶樓</span>
                            </span>
                        </div>
                        <div class="twrbo-l-productTextCard">
                            <div class="twrbo-l-productTextCard__detail">
                                <p><span ng-bind-html="dealItem.promDesc" class="ng-binding">*中信卡紅利點數每1,000點折抵NT60元，折抵上限為單筆消費金額100%。</span></p>
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
                                        <li ng-show="dealItem.hasOwnProperty('B') &amp;&amp; dealItem.B.length > 0">
                                            <div class="twrbo-c-additionalicon">
                                                <img src="/content/dam/twrbo/images/icon/icon_card_dark.svg" alt="" width="16" height="16">
                                                <span>適用
                                                    <!-- ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">所有卡</span>
                                                        <span ng-show="!$last" class="ng-hide">/</span>
                                                    </span><!-- end ngRepeat: card in dealItem.B -->
                                                </span>
                                            </div>
                                        </li>
                                        <li>
                                            <ul class="twrbo-l-listHorizontal twrbo-l-listHorizontal--additional twrbo-c-fSmall">
                                                <li ng-show="dealItem.phone != ''">
                                                    <div class="twrbo-c-additionalicon">
                                                        <img src="/content/dam/twrbo/images/icon/icon_phone_dark.svg" alt="" width="16" height="16">
                                                        <a ng-href="tel:0422595888" target="_parent" class="twrbo-h-linkEffect-url--gy twrbo-c-link--tel" href="tel:0422595888">
                                                            <span ng-bind="dealItem.phone" class="ng-binding">04-22595888</span>
                                                        </a>
                                                    </div>
                                                </li>
                                                <li ng-show="dealItem.address != ''">
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
                                                <li ng-show="dealItem.promUrl != ''" class="ng-hide">
                                                    <div class="twrbo-c-additionalicon">
                                                        <img src="/content/dam/twrbo/images/icon/icon_link_dark.svg" alt="" width="16" height="16">
                                                        <a ng-href="" class="twrbo-h-linkEffect-url--gy">
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
                        <span class="twrbo-c-thumb picturefill-background" style="background-image: url(&quot;/content/dam/twrbo/images/creditcard/offer/FOOD2303.jpg&quot;); background-size: cover; background-repeat: no-repeat; background-position: 50% 50%;">
                            <span data-src="/content/dam/twrbo/images/creditcard/offer/FOOD2303.jpg" data-src-default="/content/dam/twrbo/images/matchCard.png"></span>
                        </span>
                        <div class="twrbo-h-gutters-out-sm-v">
                            <ul class="twrbo-c-label twrbo-c-label--trim">
                                <li ng-show="dealItem.promTag != ''" class="ng-hide">
                                    <ul class="twrbo-c-label twrbo-c-label--promo twrbo-c-label--trim">
                                        <li>
                                            <i class="twrbo-c-iLabel twrbo-c-iLabel--fire"></i>
                                            <span ng-bind="dealItem.promTag" class="ng-binding"></span>
                                        </li>
                                    </ul>
                                </li>
                                <!-- ngRepeat: tag in dealItem.C --><li ng-repeat="tag in dealItem.C" ng-show="dealItem.hasOwnProperty('C')" class="ng-scope">
                                    <a ng-click="onTagClick(tag.filterItemKey, tag.filterItemName)">
                                        <sapn ng-bind="tag.filterItemName" class="ng-binding">點數回饋</sapn></a>
                                </li><!-- end ngRepeat: tag in dealItem.C -->
                            </ul>
                        </div>
                    </div>
                    <div class="twrbo-l-productCard__text">
                        <div class="twrbo-h-margin-bottom-md">
                            <span class="twrbo-c-h3 twrbo-c-link twrbo-c-link--ignoreEffect">
                                <span ng-bind="dealItem.name" class="ng-binding">小蒙牛頂級麻辣養生鍋</span>
                            </span>
                        </div>
                        <div class="twrbo-l-productTextCard">
                            <div class="twrbo-l-productTextCard__detail">
                                <p><span ng-bind-html="dealItem.promDesc" class="ng-binding">刷中信卡單月累積滿額贈3%刷卡金(需登錄)</span></p>
                                <div class="twrbo-h-margin-top-sm">
                                    <ul class="twrbo-c-list twrbo-c-list--data twrbo-c-list--small twrbo-c-list--small">
                                        <li ng-show="dealItem.startDay != '' &amp;&amp; dealItem.endDay != ''">
                                            <div class="twrbo-c-additionalicon">
                                                <img src="/content/dam/twrbo/images/icon/icon_clock_dark.svg" alt="" width="16" height="16">
                                                <span ng-bind="dealItem.startDay" class="ng-binding">2023/10/01</span>
                                                <span>~</span>
                                                <span ng-bind="dealItem.endDay" class="ng-binding">2023/12/31</span>
                                            </div>
                                        </li>
                                        <li ng-show="dealItem.hasOwnProperty('B') &amp;&amp; dealItem.B.length > 0">
                                            <div class="twrbo-c-additionalicon">
                                                <img src="/content/dam/twrbo/images/icon/icon_card_dark.svg" alt="" width="16" height="16">
                                                <span>適用
                                                    <!-- ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">無限卡</span>
                                                        <span ng-show="!$last">/</span>
                                                    </span><!-- end ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">世界卡</span>
                                                        <span ng-show="!$last">/</span>
                                                    </span><!-- end ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">極緻卡</span>
                                                        <span ng-show="!$last">/</span>
                                                    </span><!-- end ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">御璽卡</span>
                                                        <span ng-show="!$last">/</span>
                                                    </span><!-- end ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">鈦金卡</span>
                                                        <span ng-show="!$last">/</span>
                                                    </span><!-- end ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">晶緻卡</span>
                                                        <span ng-show="!$last">/</span>
                                                    </span><!-- end ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">聯名認同卡</span>
                                                        <span ng-show="!$last">/</span>
                                                    </span><!-- end ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">所有卡</span>
                                                        <span ng-show="!$last" class="ng-hide">/</span>
                                                    </span><!-- end ngRepeat: card in dealItem.B -->
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
                                                        <a ng-href="https://www.ctbcbank.com/content/dam/minisite/long/creditcard/food2023/index.html" class="twrbo-h-linkEffect-url--gy" href="https://www.ctbcbank.com/content/dam/minisite/long/creditcard/food2023/index.html">
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
                        <span class="twrbo-c-thumb picturefill-background" style="background-image: url(&quot;/content/dam/twrbo/images/creditcard/offer/WOW17.jpg&quot;); background-size: cover; background-repeat: no-repeat; background-position: 50% 50%;">
                            <span data-src="/content/dam/twrbo/images/creditcard/offer/WOW17.jpg" data-src-default="/content/dam/twrbo/images/matchCard.png"></span>
                        </span>
                        <div class="twrbo-h-gutters-out-sm-v">
                            <ul class="twrbo-c-label twrbo-c-label--trim">
                                <li ng-show="dealItem.promTag != ''" class="ng-hide">
                                    <ul class="twrbo-c-label twrbo-c-label--promo twrbo-c-label--trim">
                                        <li>
                                            <i class="twrbo-c-iLabel twrbo-c-iLabel--fire"></i>
                                            <span ng-bind="dealItem.promTag" class="ng-binding"></span>
                                        </li>
                                    </ul>
                                </li>
                                <!-- ngRepeat: tag in dealItem.C --><li ng-repeat="tag in dealItem.C" ng-show="dealItem.hasOwnProperty('C')" class="ng-scope">
                                    <a ng-click="onTagClick(tag.filterItemKey, tag.filterItemName)">
                                        <sapn ng-bind="tag.filterItemName" class="ng-binding">點數回饋</sapn></a>
                                </li><!-- end ngRepeat: tag in dealItem.C -->
                            </ul>
                        </div>
                    </div>
                    <div class="twrbo-l-productCard__text">
                        <div class="twrbo-h-margin-bottom-md">
                            <span class="twrbo-c-h3 twrbo-c-link twrbo-c-link--ignoreEffect">
                                <span ng-bind="dealItem.name" class="ng-binding">THE WANG PRIME  STEAK</span>
                            </span>
                        </div>
                        <div class="twrbo-l-productTextCard">
                            <div class="twrbo-l-productTextCard__detail">
                                <p><span ng-bind-html="dealItem.promDesc" class="ng-binding">使用王品瘋美食App電子錢包瘋Pay且綁定中信卡消費付款，享週六~週日10%瘋點數回饋、週一~週五3%瘋點數回饋。</span></p>
                                <div class="twrbo-h-margin-top-sm">
                                    <ul class="twrbo-c-list twrbo-c-list--data twrbo-c-list--small twrbo-c-list--small">
                                        <li ng-show="dealItem.startDay != '' &amp;&amp; dealItem.endDay != ''">
                                            <div class="twrbo-c-additionalicon">
                                                <img src="/content/dam/twrbo/images/icon/icon_clock_dark.svg" alt="" width="16" height="16">
                                                <span ng-bind="dealItem.startDay" class="ng-binding">2023/10/01</span>
                                                <span>~</span>
                                                <span ng-bind="dealItem.endDay" class="ng-binding">2023/12/31</span>
                                            </div>
                                        </li>
                                        <li ng-show="dealItem.hasOwnProperty('B') &amp;&amp; dealItem.B.length > 0">
                                            <div class="twrbo-c-additionalicon">
                                                <img src="/content/dam/twrbo/images/icon/icon_card_dark.svg" alt="" width="16" height="16">
                                                <span>適用
                                                    <!-- ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">無限卡</span>
                                                        <span ng-show="!$last">/</span>
                                                    </span><!-- end ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">世界卡</span>
                                                        <span ng-show="!$last">/</span>
                                                    </span><!-- end ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">極緻卡</span>
                                                        <span ng-show="!$last">/</span>
                                                    </span><!-- end ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">御璽卡</span>
                                                        <span ng-show="!$last">/</span>
                                                    </span><!-- end ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">鈦金卡</span>
                                                        <span ng-show="!$last">/</span>
                                                    </span><!-- end ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">晶緻卡</span>
                                                        <span ng-show="!$last">/</span>
                                                    </span><!-- end ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">聯名認同卡</span>
                                                        <span ng-show="!$last">/</span>
                                                    </span><!-- end ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">所有卡</span>
                                                        <span ng-show="!$last" class="ng-hide">/</span>
                                                    </span><!-- end ngRepeat: card in dealItem.B -->
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
                                                        <a ng-href="https://www.ctbcbank.com/content/dam/minisite/long/creditcard/wowapp/index.html" class="twrbo-h-linkEffect-url--gy" href="https://www.ctbcbank.com/content/dam/minisite/long/creditcard/wowapp/index.html">
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
                        <span class="twrbo-c-thumb picturefill-background" style="background-image: url(&quot;/content/dam/twrbo/images/creditcard/offer/Redeem000099.jpg&quot;); background-size: cover; background-repeat: no-repeat; background-position: 50% 50%;">
                            <span data-src="/content/dam/twrbo/images/creditcard/offer/Redeem000099.jpg" data-src-default="/content/dam/twrbo/images/matchCard.png"></span>
                        </span>
                        <div class="twrbo-h-gutters-out-sm-v">
                            <ul class="twrbo-c-label twrbo-c-label--trim">
                                <li ng-show="dealItem.promTag != ''" class="ng-hide">
                                    <ul class="twrbo-c-label twrbo-c-label--promo twrbo-c-label--trim">
                                        <li>
                                            <i class="twrbo-c-iLabel twrbo-c-iLabel--fire"></i>
                                            <span ng-bind="dealItem.promTag" class="ng-binding"></span>
                                        </li>
                                    </ul>
                                </li>
                                <!-- ngRepeat: tag in dealItem.C --><li ng-repeat="tag in dealItem.C" ng-show="dealItem.hasOwnProperty('C')" class="ng-scope">
                                    <a ng-click="onTagClick(tag.filterItemKey, tag.filterItemName)">
                                        <sapn ng-bind="tag.filterItemName" class="ng-binding">紅利折抵</sapn></a>
                                </li><!-- end ngRepeat: tag in dealItem.C -->
                            </ul>
                        </div>
                    </div>
                    <div class="twrbo-l-productCard__text">
                        <div class="twrbo-h-margin-bottom-md">
                            <span class="twrbo-c-h3 twrbo-c-link twrbo-c-link--ignoreEffect">
                                <span ng-bind="dealItem.name" class="ng-binding">大手前鐵板燒</span>
                            </span>
                        </div>
                        <div class="twrbo-l-productTextCard">
                            <div class="twrbo-l-productTextCard__detail">
                                <p><span ng-bind-html="dealItem.promDesc" class="ng-binding">*中信卡紅利點數每1,000點折抵NT60元，折抵上限為單筆消費金額100%。</span></p>
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
                                        <li ng-show="dealItem.hasOwnProperty('B') &amp;&amp; dealItem.B.length > 0">
                                            <div class="twrbo-c-additionalicon">
                                                <img src="/content/dam/twrbo/images/icon/icon_card_dark.svg" alt="" width="16" height="16">
                                                <span>適用
                                                    <!-- ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">所有卡</span>
                                                        <span ng-show="!$last" class="ng-hide">/</span>
                                                    </span><!-- end ngRepeat: card in dealItem.B -->
                                                </span>
                                            </div>
                                        </li>
                                        <li>
                                            <ul class="twrbo-l-listHorizontal twrbo-l-listHorizontal--additional twrbo-c-fSmall">
                                                <li ng-show="dealItem.phone != ''">
                                                    <div class="twrbo-c-additionalicon">
                                                        <img src="/content/dam/twrbo/images/icon/icon_phone_dark.svg" alt="" width="16" height="16">
                                                        <a ng-href="tel:0422503131" target="_parent" class="twrbo-h-linkEffect-url--gy twrbo-c-link--tel" href="tel:0422503131">
                                                            <span ng-bind="dealItem.phone" class="ng-binding">04-22503131</span>
                                                        </a>
                                                    </div>
                                                </li>
                                                <li ng-show="dealItem.address != ''">
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
                                                <li ng-show="dealItem.promUrl != ''" class="ng-hide">
                                                    <div class="twrbo-c-additionalicon">
                                                        <img src="/content/dam/twrbo/images/icon/icon_link_dark.svg" alt="" width="16" height="16">
                                                        <a ng-href="" class="twrbo-h-linkEffect-url--gy">
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
                        <span class="twrbo-c-thumb picturefill-background" style="background-image: url(&quot;/content/dam/twrbo/images/creditcard/offer/WOW01.jpg&quot;); background-size: cover; background-repeat: no-repeat; background-position: 50% 50%;">
                            <span data-src="/content/dam/twrbo/images/creditcard/offer/WOW01.jpg" data-src-default="/content/dam/twrbo/images/matchCard.png"></span>
                        </span>
                        <div class="twrbo-h-gutters-out-sm-v">
                            <ul class="twrbo-c-label twrbo-c-label--trim">
                                <li ng-show="dealItem.promTag != ''" class="ng-hide">
                                    <ul class="twrbo-c-label twrbo-c-label--promo twrbo-c-label--trim">
                                        <li>
                                            <i class="twrbo-c-iLabel twrbo-c-iLabel--fire"></i>
                                            <span ng-bind="dealItem.promTag" class="ng-binding"></span>
                                        </li>
                                    </ul>
                                </li>
                                <!-- ngRepeat: tag in dealItem.C --><li ng-repeat="tag in dealItem.C" ng-show="dealItem.hasOwnProperty('C')" class="ng-scope">
                                    <a ng-click="onTagClick(tag.filterItemKey, tag.filterItemName)">
                                        <sapn ng-bind="tag.filterItemName" class="ng-binding">點數回饋</sapn></a>
                                </li><!-- end ngRepeat: tag in dealItem.C -->
                            </ul>
                        </div>
                    </div>
                    <div class="twrbo-l-productCard__text">
                        <div class="twrbo-h-margin-bottom-md">
                            <span class="twrbo-c-h3 twrbo-c-link twrbo-c-link--ignoreEffect">
                                <span ng-bind="dealItem.name" class="ng-binding">石二鍋</span>
                            </span>
                        </div>
                        <div class="twrbo-l-productTextCard">
                            <div class="twrbo-l-productTextCard__detail">
                                <p><span ng-bind-html="dealItem.promDesc" class="ng-binding">使用王品瘋美食App電子錢包瘋Pay且綁定中信卡消費付款，享週六~週日6%瘋點數回饋、週一~週五3%瘋點數回饋。</span></p>
                                <div class="twrbo-h-margin-top-sm">
                                    <ul class="twrbo-c-list twrbo-c-list--data twrbo-c-list--small twrbo-c-list--small">
                                        <li ng-show="dealItem.startDay != '' &amp;&amp; dealItem.endDay != ''">
                                            <div class="twrbo-c-additionalicon">
                                                <img src="/content/dam/twrbo/images/icon/icon_clock_dark.svg" alt="" width="16" height="16">
                                                <span ng-bind="dealItem.startDay" class="ng-binding">2023/10/01</span>
                                                <span>~</span>
                                                <span ng-bind="dealItem.endDay" class="ng-binding">2023/12/31</span>
                                            </div>
                                        </li>
                                        <li ng-show="dealItem.hasOwnProperty('B') &amp;&amp; dealItem.B.length > 0">
                                            <div class="twrbo-c-additionalicon">
                                                <img src="/content/dam/twrbo/images/icon/icon_card_dark.svg" alt="" width="16" height="16">
                                                <span>適用
                                                    <!-- ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">無限卡</span>
                                                        <span ng-show="!$last">/</span>
                                                    </span><!-- end ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">世界卡</span>
                                                        <span ng-show="!$last">/</span>
                                                    </span><!-- end ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">極緻卡</span>
                                                        <span ng-show="!$last">/</span>
                                                    </span><!-- end ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">御璽卡</span>
                                                        <span ng-show="!$last">/</span>
                                                    </span><!-- end ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">鈦金卡</span>
                                                        <span ng-show="!$last">/</span>
                                                    </span><!-- end ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">晶緻卡</span>
                                                        <span ng-show="!$last">/</span>
                                                    </span><!-- end ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">聯名認同卡</span>
                                                        <span ng-show="!$last">/</span>
                                                    </span><!-- end ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">所有卡</span>
                                                        <span ng-show="!$last" class="ng-hide">/</span>
                                                    </span><!-- end ngRepeat: card in dealItem.B -->
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
                                                        <a ng-href="https://www.ctbcbank.com/content/dam/minisite/long/creditcard/wowapp/index.html" class="twrbo-h-linkEffect-url--gy" href="https://www.ctbcbank.com/content/dam/minisite/long/creditcard/wowapp/index.html">
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
                        <span class="twrbo-c-thumb picturefill-background" style="background-image: url(&quot;/content/dam/twrbo/images/creditcard/offer/Redeem000100.jpg&quot;); background-size: cover; background-repeat: no-repeat; background-position: 50% 50%;">
                            <span data-src="/content/dam/twrbo/images/creditcard/offer/Redeem000100.jpg" data-src-default="/content/dam/twrbo/images/matchCard.png"></span>
                        </span>
                        <div class="twrbo-h-gutters-out-sm-v">
                            <ul class="twrbo-c-label twrbo-c-label--trim">
                                <li ng-show="dealItem.promTag != ''" class="ng-hide">
                                    <ul class="twrbo-c-label twrbo-c-label--promo twrbo-c-label--trim">
                                        <li>
                                            <i class="twrbo-c-iLabel twrbo-c-iLabel--fire"></i>
                                            <span ng-bind="dealItem.promTag" class="ng-binding"></span>
                                        </li>
                                    </ul>
                                </li>
                                <!-- ngRepeat: tag in dealItem.C --><li ng-repeat="tag in dealItem.C" ng-show="dealItem.hasOwnProperty('C')" class="ng-scope">
                                    <a ng-click="onTagClick(tag.filterItemKey, tag.filterItemName)">
                                        <sapn ng-bind="tag.filterItemName" class="ng-binding">紅利折抵</sapn></a>
                                </li><!-- end ngRepeat: tag in dealItem.C -->
                            </ul>
                        </div>
                    </div>
                    <div class="twrbo-l-productCard__text">
                        <div class="twrbo-h-margin-bottom-md">
                            <span class="twrbo-c-h3 twrbo-c-link twrbo-c-link--ignoreEffect">
                                <span ng-bind="dealItem.name" class="ng-binding">大手前鐵板燒</span>
                            </span>
                        </div>
                        <div class="twrbo-l-productTextCard">
                            <div class="twrbo-l-productTextCard__detail">
                                <p><span ng-bind-html="dealItem.promDesc" class="ng-binding">*中信卡紅利點數每1,000點折抵NT60元，折抵上限為單筆消費金額100%。</span></p>
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
                                        <li ng-show="dealItem.hasOwnProperty('B') &amp;&amp; dealItem.B.length > 0">
                                            <div class="twrbo-c-additionalicon">
                                                <img src="/content/dam/twrbo/images/icon/icon_card_dark.svg" alt="" width="16" height="16">
                                                <span>適用
                                                    <!-- ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">所有卡</span>
                                                        <span ng-show="!$last" class="ng-hide">/</span>
                                                    </span><!-- end ngRepeat: card in dealItem.B -->
                                                </span>
                                            </div>
                                        </li>
                                        <li>
                                            <ul class="twrbo-l-listHorizontal twrbo-l-listHorizontal--additional twrbo-c-fSmall">
                                                <li ng-show="dealItem.phone != ''">
                                                    <div class="twrbo-c-additionalicon">
                                                        <img src="/content/dam/twrbo/images/icon/icon_phone_dark.svg" alt="" width="16" height="16">
                                                        <a ng-href="tel:055347111" target="_parent" class="twrbo-h-linkEffect-url--gy twrbo-c-link--tel" href="tel:055347111">
                                                            <span ng-bind="dealItem.phone" class="ng-binding">05-5347111</span>
                                                        </a>
                                                    </div>
                                                </li>
                                                <li ng-show="dealItem.address != ''">
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
                                                <li ng-show="dealItem.promUrl != ''" class="ng-hide">
                                                    <div class="twrbo-c-additionalicon">
                                                        <img src="/content/dam/twrbo/images/icon/icon_link_dark.svg" alt="" width="16" height="16">
                                                        <a ng-href="" class="twrbo-h-linkEffect-url--gy">
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
                        <span class="twrbo-c-thumb picturefill-background" style="background-image: url(&quot;/content/dam/twrbo/images/creditcard/offer/WOW33.jpg&quot;); background-size: cover; background-repeat: no-repeat; background-position: 50% 50%;">
                            <span data-src="/content/dam/twrbo/images/creditcard/offer/WOW33.jpg" data-src-default="/content/dam/twrbo/images/matchCard.png"></span>
                        </span>
                        <div class="twrbo-h-gutters-out-sm-v">
                            <ul class="twrbo-c-label twrbo-c-label--trim">
                                <li ng-show="dealItem.promTag != ''" class="ng-hide">
                                    <ul class="twrbo-c-label twrbo-c-label--promo twrbo-c-label--trim">
                                        <li>
                                            <i class="twrbo-c-iLabel twrbo-c-iLabel--fire"></i>
                                            <span ng-bind="dealItem.promTag" class="ng-binding"></span>
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
                                <span ng-bind="dealItem.name" class="ng-binding">丰禾台式小館</span>
                            </span>
                        </div>
                        <div class="twrbo-l-productTextCard">
                            <div class="twrbo-l-productTextCard__detail">
                                <p><span ng-bind-html="dealItem.promDesc" class="ng-binding">刷中信卡內用消費多人套餐，款待鐵板紅燒豆腐乙份(價值220元)</span></p>
                                <div class="twrbo-h-margin-top-sm">
                                    <ul class="twrbo-c-list twrbo-c-list--data twrbo-c-list--small twrbo-c-list--small">
                                        <li ng-show="dealItem.startDay != '' &amp;&amp; dealItem.endDay != ''">
                                            <div class="twrbo-c-additionalicon">
                                                <img src="/content/dam/twrbo/images/icon/icon_clock_dark.svg" alt="" width="16" height="16">
                                                <span ng-bind="dealItem.startDay" class="ng-binding">2023/11/01</span>
                                                <span>~</span>
                                                <span ng-bind="dealItem.endDay" class="ng-binding">2023/12/31</span>
                                            </div>
                                        </li>
                                        <li ng-show="dealItem.hasOwnProperty('B') &amp;&amp; dealItem.B.length > 0">
                                            <div class="twrbo-c-additionalicon">
                                                <img src="/content/dam/twrbo/images/icon/icon_card_dark.svg" alt="" width="16" height="16">
                                                <span>適用
                                                    <!-- ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">無限卡</span>
                                                        <span ng-show="!$last">/</span>
                                                    </span><!-- end ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">世界卡</span>
                                                        <span ng-show="!$last">/</span>
                                                    </span><!-- end ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">極緻卡</span>
                                                        <span ng-show="!$last">/</span>
                                                    </span><!-- end ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">御璽卡</span>
                                                        <span ng-show="!$last">/</span>
                                                    </span><!-- end ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">鈦金卡</span>
                                                        <span ng-show="!$last">/</span>
                                                    </span><!-- end ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">晶緻卡</span>
                                                        <span ng-show="!$last">/</span>
                                                    </span><!-- end ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">聯名認同卡</span>
                                                        <span ng-show="!$last">/</span>
                                                    </span><!-- end ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">所有卡</span>
                                                        <span ng-show="!$last" class="ng-hide">/</span>
                                                    </span><!-- end ngRepeat: card in dealItem.B -->
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
                                                        <a ng-href="https://mkt.ctbcbank.com/long/creditcard/veggtable/index.html" class="twrbo-h-linkEffect-url--gy" href="https://mkt.ctbcbank.com/long/creditcard/veggtable/index.html">
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
                        <span class="twrbo-c-thumb picturefill-background" style="background-image: url(&quot;/content/dam/twrbo/images/creditcard/offer/FOOD2301.jpg&quot;); background-size: cover; background-repeat: no-repeat; background-position: 50% 50%;">
                            <span data-src="/content/dam/twrbo/images/creditcard/offer/FOOD2301.jpg" data-src-default="/content/dam/twrbo/images/matchCard.png"></span>
                        </span>
                        <div class="twrbo-h-gutters-out-sm-v">
                            <ul class="twrbo-c-label twrbo-c-label--trim">
                                <li ng-show="dealItem.promTag != ''" class="ng-hide">
                                    <ul class="twrbo-c-label twrbo-c-label--promo twrbo-c-label--trim">
                                        <li>
                                            <i class="twrbo-c-iLabel twrbo-c-iLabel--fire"></i>
                                            <span ng-bind="dealItem.promTag" class="ng-binding"></span>
                                        </li>
                                    </ul>
                                </li>
                                <!-- ngRepeat: tag in dealItem.C --><li ng-repeat="tag in dealItem.C" ng-show="dealItem.hasOwnProperty('C')" class="ng-scope">
                                    <a ng-click="onTagClick(tag.filterItemKey, tag.filterItemName)">
                                        <sapn ng-bind="tag.filterItemName" class="ng-binding">點數回饋</sapn></a>
                                </li><!-- end ngRepeat: tag in dealItem.C -->
                            </ul>
                        </div>
                    </div>
                    <div class="twrbo-l-productCard__text">
                        <div class="twrbo-h-margin-bottom-md">
                            <span class="twrbo-c-h3 twrbo-c-link twrbo-c-link--ignoreEffect">
                                <span ng-bind="dealItem.name" class="ng-binding">老四川餐飲集團</span>
                            </span>
                        </div>
                        <div class="twrbo-l-productTextCard">
                            <div class="twrbo-l-productTextCard__detail">
                                <p><span ng-bind-html="dealItem.promDesc" class="ng-binding">刷中信卡單月累積滿額贈3%刷卡金(需登錄)</span></p>
                                <div class="twrbo-h-margin-top-sm">
                                    <ul class="twrbo-c-list twrbo-c-list--data twrbo-c-list--small twrbo-c-list--small">
                                        <li ng-show="dealItem.startDay != '' &amp;&amp; dealItem.endDay != ''">
                                            <div class="twrbo-c-additionalicon">
                                                <img src="/content/dam/twrbo/images/icon/icon_clock_dark.svg" alt="" width="16" height="16">
                                                <span ng-bind="dealItem.startDay" class="ng-binding">2023/10/01</span>
                                                <span>~</span>
                                                <span ng-bind="dealItem.endDay" class="ng-binding">2023/12/31</span>
                                            </div>
                                        </li>
                                        <li ng-show="dealItem.hasOwnProperty('B') &amp;&amp; dealItem.B.length > 0">
                                            <div class="twrbo-c-additionalicon">
                                                <img src="/content/dam/twrbo/images/icon/icon_card_dark.svg" alt="" width="16" height="16">
                                                <span>適用
                                                    <!-- ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">無限卡</span>
                                                        <span ng-show="!$last">/</span>
                                                    </span><!-- end ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">世界卡</span>
                                                        <span ng-show="!$last">/</span>
                                                    </span><!-- end ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">極緻卡</span>
                                                        <span ng-show="!$last">/</span>
                                                    </span><!-- end ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">御璽卡</span>
                                                        <span ng-show="!$last">/</span>
                                                    </span><!-- end ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">鈦金卡</span>
                                                        <span ng-show="!$last">/</span>
                                                    </span><!-- end ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">晶緻卡</span>
                                                        <span ng-show="!$last">/</span>
                                                    </span><!-- end ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">聯名認同卡</span>
                                                        <span ng-show="!$last">/</span>
                                                    </span><!-- end ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">所有卡</span>
                                                        <span ng-show="!$last" class="ng-hide">/</span>
                                                    </span><!-- end ngRepeat: card in dealItem.B -->
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
                                                        <a ng-href="https://www.ctbcbank.com/content/dam/minisite/long/creditcard/food2023/index.html" class="twrbo-h-linkEffect-url--gy" href="https://www.ctbcbank.com/content/dam/minisite/long/creditcard/food2023/index.html">
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
                        <span class="twrbo-c-thumb picturefill-background" style="background-image: url(&quot;/content/dam/twrbo/images/creditcard/offer/WOW03.jpg&quot;); background-size: cover; background-repeat: no-repeat; background-position: 50% 50%;">
                            <span data-src="/content/dam/twrbo/images/creditcard/offer/WOW03.jpg" data-src-default="/content/dam/twrbo/images/matchCard.png"></span>
                        </span>
                        <div class="twrbo-h-gutters-out-sm-v">
                            <ul class="twrbo-c-label twrbo-c-label--trim">
                                <li ng-show="dealItem.promTag != ''" class="ng-hide">
                                    <ul class="twrbo-c-label twrbo-c-label--promo twrbo-c-label--trim">
                                        <li>
                                            <i class="twrbo-c-iLabel twrbo-c-iLabel--fire"></i>
                                            <span ng-bind="dealItem.promTag" class="ng-binding"></span>
                                        </li>
                                    </ul>
                                </li>
                                <!-- ngRepeat: tag in dealItem.C --><li ng-repeat="tag in dealItem.C" ng-show="dealItem.hasOwnProperty('C')" class="ng-scope">
                                    <a ng-click="onTagClick(tag.filterItemKey, tag.filterItemName)">
                                        <sapn ng-bind="tag.filterItemName" class="ng-binding">點數回饋</sapn></a>
                                </li><!-- end ngRepeat: tag in dealItem.C -->
                            </ul>
                        </div>
                    </div>
                    <div class="twrbo-l-productCard__text">
                        <div class="twrbo-h-margin-bottom-md">
                            <span class="twrbo-c-h3 twrbo-c-link twrbo-c-link--ignoreEffect">
                                <span ng-bind="dealItem.name" class="ng-binding">青花驕麻辣鍋</span>
                            </span>
                        </div>
                        <div class="twrbo-l-productTextCard">
                            <div class="twrbo-l-productTextCard__detail">
                                <p><span ng-bind-html="dealItem.promDesc" class="ng-binding">使用王品瘋美食App電子錢包瘋Pay且綁定中信卡消費付款，享週六~週日6%瘋點數回饋、週一~週五3%瘋點數回饋。</span></p>
                                <div class="twrbo-h-margin-top-sm">
                                    <ul class="twrbo-c-list twrbo-c-list--data twrbo-c-list--small twrbo-c-list--small">
                                        <li ng-show="dealItem.startDay != '' &amp;&amp; dealItem.endDay != ''">
                                            <div class="twrbo-c-additionalicon">
                                                <img src="/content/dam/twrbo/images/icon/icon_clock_dark.svg" alt="" width="16" height="16">
                                                <span ng-bind="dealItem.startDay" class="ng-binding">2023/10/01</span>
                                                <span>~</span>
                                                <span ng-bind="dealItem.endDay" class="ng-binding">2023/12/31</span>
                                            </div>
                                        </li>
                                        <li ng-show="dealItem.hasOwnProperty('B') &amp;&amp; dealItem.B.length > 0">
                                            <div class="twrbo-c-additionalicon">
                                                <img src="/content/dam/twrbo/images/icon/icon_card_dark.svg" alt="" width="16" height="16">
                                                <span>適用
                                                    <!-- ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">無限卡</span>
                                                        <span ng-show="!$last">/</span>
                                                    </span><!-- end ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">世界卡</span>
                                                        <span ng-show="!$last">/</span>
                                                    </span><!-- end ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">極緻卡</span>
                                                        <span ng-show="!$last">/</span>
                                                    </span><!-- end ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">御璽卡</span>
                                                        <span ng-show="!$last">/</span>
                                                    </span><!-- end ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">鈦金卡</span>
                                                        <span ng-show="!$last">/</span>
                                                    </span><!-- end ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">晶緻卡</span>
                                                        <span ng-show="!$last">/</span>
                                                    </span><!-- end ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">聯名認同卡</span>
                                                        <span ng-show="!$last">/</span>
                                                    </span><!-- end ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">所有卡</span>
                                                        <span ng-show="!$last" class="ng-hide">/</span>
                                                    </span><!-- end ngRepeat: card in dealItem.B -->
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
                                                        <a ng-href="https://www.ctbcbank.com/content/dam/minisite/long/creditcard/wowapp/index.html" class="twrbo-h-linkEffect-url--gy" href="https://www.ctbcbank.com/content/dam/minisite/long/creditcard/wowapp/index.html">
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
                        <span class="twrbo-c-thumb picturefill-background" style="background-image: url(&quot;/content/dam/twrbo/images/creditcard/offer/Redeem000101.jpg&quot;); background-size: cover; background-repeat: no-repeat; background-position: 50% 50%;">
                            <span data-src="/content/dam/twrbo/images/creditcard/offer/Redeem000101.jpg" data-src-default="/content/dam/twrbo/images/matchCard.png"></span>
                        </span>
                        <div class="twrbo-h-gutters-out-sm-v">
                            <ul class="twrbo-c-label twrbo-c-label--trim">
                                <li ng-show="dealItem.promTag != ''" class="ng-hide">
                                    <ul class="twrbo-c-label twrbo-c-label--promo twrbo-c-label--trim">
                                        <li>
                                            <i class="twrbo-c-iLabel twrbo-c-iLabel--fire"></i>
                                            <span ng-bind="dealItem.promTag" class="ng-binding"></span>
                                        </li>
                                    </ul>
                                </li>
                                <!-- ngRepeat: tag in dealItem.C --><li ng-repeat="tag in dealItem.C" ng-show="dealItem.hasOwnProperty('C')" class="ng-scope">
                                    <a ng-click="onTagClick(tag.filterItemKey, tag.filterItemName)">
                                        <sapn ng-bind="tag.filterItemName" class="ng-binding">紅利折抵</sapn></a>
                                </li><!-- end ngRepeat: tag in dealItem.C -->
                            </ul>
                        </div>
                    </div>
                    <div class="twrbo-l-productCard__text">
                        <div class="twrbo-h-margin-bottom-md">
                            <span class="twrbo-c-h3 twrbo-c-link twrbo-c-link--ignoreEffect">
                                <span ng-bind="dealItem.name" class="ng-binding">大手前鐵板燒</span>
                            </span>
                        </div>
                        <div class="twrbo-l-productTextCard">
                            <div class="twrbo-l-productTextCard__detail">
                                <p><span ng-bind-html="dealItem.promDesc" class="ng-binding">*中信卡紅利點數每1,000點折抵NT60元，折抵上限為單筆消費金額100%。</span></p>
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
                                        <li ng-show="dealItem.hasOwnProperty('B') &amp;&amp; dealItem.B.length > 0">
                                            <div class="twrbo-c-additionalicon">
                                                <img src="/content/dam/twrbo/images/icon/icon_card_dark.svg" alt="" width="16" height="16">
                                                <span>適用
                                                    <!-- ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">所有卡</span>
                                                        <span ng-show="!$last" class="ng-hide">/</span>
                                                    </span><!-- end ngRepeat: card in dealItem.B -->
                                                </span>
                                            </div>
                                        </li>
                                        <li>
                                            <ul class="twrbo-l-listHorizontal twrbo-l-listHorizontal--additional twrbo-c-fSmall">
                                                <li ng-show="dealItem.phone != ''">
                                                    <div class="twrbo-c-additionalicon">
                                                        <img src="/content/dam/twrbo/images/icon/icon_phone_dark.svg" alt="" width="16" height="16">
                                                        <a ng-href="tel:073927555" target="_parent" class="twrbo-h-linkEffect-url--gy twrbo-c-link--tel" href="tel:073927555">
                                                            <span ng-bind="dealItem.phone" class="ng-binding">07-3927555</span>
                                                        </a>
                                                    </div>
                                                </li>
                                                <li ng-show="dealItem.address != ''">
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
                                                <li ng-show="dealItem.promUrl != ''" class="ng-hide">
                                                    <div class="twrbo-c-additionalicon">
                                                        <img src="/content/dam/twrbo/images/icon/icon_link_dark.svg" alt="" width="16" height="16">
                                                        <a ng-href="" class="twrbo-h-linkEffect-url--gy">
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
                        <span class="twrbo-c-thumb picturefill-background" style="background-image: url(&quot;/content/dam/twrbo/images/creditcard/offer/WOW05.jpg&quot;); background-size: cover; background-repeat: no-repeat; background-position: 50% 50%;">
                            <span data-src="/content/dam/twrbo/images/creditcard/offer/WOW05.jpg" data-src-default="/content/dam/twrbo/images/matchCard.png"></span>
                        </span>
                        <div class="twrbo-h-gutters-out-sm-v">
                            <ul class="twrbo-c-label twrbo-c-label--trim">
                                <li ng-show="dealItem.promTag != ''" class="ng-hide">
                                    <ul class="twrbo-c-label twrbo-c-label--promo twrbo-c-label--trim">
                                        <li>
                                            <i class="twrbo-c-iLabel twrbo-c-iLabel--fire"></i>
                                            <span ng-bind="dealItem.promTag" class="ng-binding"></span>
                                        </li>
                                    </ul>
                                </li>
                                <!-- ngRepeat: tag in dealItem.C --><li ng-repeat="tag in dealItem.C" ng-show="dealItem.hasOwnProperty('C')" class="ng-scope">
                                    <a ng-click="onTagClick(tag.filterItemKey, tag.filterItemName)">
                                        <sapn ng-bind="tag.filterItemName" class="ng-binding">點數回饋</sapn></a>
                                </li><!-- end ngRepeat: tag in dealItem.C -->
                            </ul>
                        </div>
                    </div>
                    <div class="twrbo-l-productCard__text">
                        <div class="twrbo-h-margin-bottom-md">
                            <span class="twrbo-c-h3 twrbo-c-link twrbo-c-link--ignoreEffect">
                                <span ng-bind="dealItem.name" class="ng-binding">陶板屋 和風創作料理</span>
                            </span>
                        </div>
                        <div class="twrbo-l-productTextCard">
                            <div class="twrbo-l-productTextCard__detail">
                                <p><span ng-bind-html="dealItem.promDesc" class="ng-binding">使用王品瘋美食App電子錢包瘋Pay且綁定中信卡消費付款，享週六~週日6%瘋點數回饋、週一~週五3%瘋點數回饋。</span></p>
                                <div class="twrbo-h-margin-top-sm">
                                    <ul class="twrbo-c-list twrbo-c-list--data twrbo-c-list--small twrbo-c-list--small">
                                        <li ng-show="dealItem.startDay != '' &amp;&amp; dealItem.endDay != ''">
                                            <div class="twrbo-c-additionalicon">
                                                <img src="/content/dam/twrbo/images/icon/icon_clock_dark.svg" alt="" width="16" height="16">
                                                <span ng-bind="dealItem.startDay" class="ng-binding">2023/10/01</span>
                                                <span>~</span>
                                                <span ng-bind="dealItem.endDay" class="ng-binding">2023/12/31</span>
                                            </div>
                                        </li>
                                        <li ng-show="dealItem.hasOwnProperty('B') &amp;&amp; dealItem.B.length > 0">
                                            <div class="twrbo-c-additionalicon">
                                                <img src="/content/dam/twrbo/images/icon/icon_card_dark.svg" alt="" width="16" height="16">
                                                <span>適用
                                                    <!-- ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">無限卡</span>
                                                        <span ng-show="!$last">/</span>
                                                    </span><!-- end ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">世界卡</span>
                                                        <span ng-show="!$last">/</span>
                                                    </span><!-- end ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">極緻卡</span>
                                                        <span ng-show="!$last">/</span>
                                                    </span><!-- end ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">御璽卡</span>
                                                        <span ng-show="!$last">/</span>
                                                    </span><!-- end ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">鈦金卡</span>
                                                        <span ng-show="!$last">/</span>
                                                    </span><!-- end ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">晶緻卡</span>
                                                        <span ng-show="!$last">/</span>
                                                    </span><!-- end ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">聯名認同卡</span>
                                                        <span ng-show="!$last">/</span>
                                                    </span><!-- end ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">所有卡</span>
                                                        <span ng-show="!$last" class="ng-hide">/</span>
                                                    </span><!-- end ngRepeat: card in dealItem.B -->
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
                                                        <a ng-href="https://www.ctbcbank.com/content/dam/minisite/long/creditcard/wowapp/index.html" class="twrbo-h-linkEffect-url--gy" href="https://www.ctbcbank.com/content/dam/minisite/long/creditcard/wowapp/index.html">
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
                        <span class="twrbo-c-thumb picturefill-background" style="background-image: url(&quot;/content/dam/twrbo/images/creditcard/offer/Redeem000102.jpg&quot;); background-size: cover; background-repeat: no-repeat; background-position: 50% 50%;">
                            <span data-src="/content/dam/twrbo/images/creditcard/offer/Redeem000102.jpg" data-src-default="/content/dam/twrbo/images/matchCard.png"></span>
                        </span>
                        <div class="twrbo-h-gutters-out-sm-v">
                            <ul class="twrbo-c-label twrbo-c-label--trim">
                                <li ng-show="dealItem.promTag != ''" class="ng-hide">
                                    <ul class="twrbo-c-label twrbo-c-label--promo twrbo-c-label--trim">
                                        <li>
                                            <i class="twrbo-c-iLabel twrbo-c-iLabel--fire"></i>
                                            <span ng-bind="dealItem.promTag" class="ng-binding"></span>
                                        </li>
                                    </ul>
                                </li>
                                <!-- ngRepeat: tag in dealItem.C --><li ng-repeat="tag in dealItem.C" ng-show="dealItem.hasOwnProperty('C')" class="ng-scope">
                                    <a ng-click="onTagClick(tag.filterItemKey, tag.filterItemName)">
                                        <sapn ng-bind="tag.filterItemName" class="ng-binding">紅利折抵</sapn></a>
                                </li><!-- end ngRepeat: tag in dealItem.C -->
                            </ul>
                        </div>
                    </div>
                    <div class="twrbo-l-productCard__text">
                        <div class="twrbo-h-margin-bottom-md">
                            <span class="twrbo-c-h3 twrbo-c-link twrbo-c-link--ignoreEffect">
                                <span ng-bind="dealItem.name" class="ng-binding">大手前鐵板燒</span>
                            </span>
                        </div>
                        <div class="twrbo-l-productTextCard">
                            <div class="twrbo-l-productTextCard__detail">
                                <p><span ng-bind-html="dealItem.promDesc" class="ng-binding">*中信卡紅利點數每1,000點折抵NT60元，折抵上限為單筆消費金額100%。</span></p>
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
                                        <li ng-show="dealItem.hasOwnProperty('B') &amp;&amp; dealItem.B.length > 0">
                                            <div class="twrbo-c-additionalicon">
                                                <img src="/content/dam/twrbo/images/icon/icon_card_dark.svg" alt="" width="16" height="16">
                                                <span>適用
                                                    <!-- ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">所有卡</span>
                                                        <span ng-show="!$last" class="ng-hide">/</span>
                                                    </span><!-- end ngRepeat: card in dealItem.B -->
                                                </span>
                                            </div>
                                        </li>
                                        <li>
                                            <ul class="twrbo-l-listHorizontal twrbo-l-listHorizontal--additional twrbo-c-fSmall">
                                                <li ng-show="dealItem.phone != ''">
                                                    <div class="twrbo-c-additionalicon">
                                                        <img src="/content/dam/twrbo/images/icon/icon_phone_dark.svg" alt="" width="16" height="16">
                                                        <a ng-href="tel:073649292" target="_parent" class="twrbo-h-linkEffect-url--gy twrbo-c-link--tel" href="tel:073649292">
                                                            <span ng-bind="dealItem.phone" class="ng-binding">07-3649292</span>
                                                        </a>
                                                    </div>
                                                </li>
                                                <li ng-show="dealItem.address != ''">
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
                                                <li ng-show="dealItem.promUrl != ''" class="ng-hide">
                                                    <div class="twrbo-c-additionalicon">
                                                        <img src="/content/dam/twrbo/images/icon/icon_link_dark.svg" alt="" width="16" height="16">
                                                        <a ng-href="" class="twrbo-h-linkEffect-url--gy">
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
                        <span class="twrbo-c-thumb picturefill-background" style="background-image: url(&quot;/content/dam/twrbo/images/creditcard/offer/FOOD2301.jpg&quot;); background-size: cover; background-repeat: no-repeat; background-position: 50% 50%;">
                            <span data-src="/content/dam/twrbo/images/creditcard/offer/FOOD2301.jpg" data-src-default="/content/dam/twrbo/images/matchCard.png"></span>
                        </span>
                        <div class="twrbo-h-gutters-out-sm-v">
                            <ul class="twrbo-c-label twrbo-c-label--trim">
                                <li ng-show="dealItem.promTag != ''" class="ng-hide">
                                    <ul class="twrbo-c-label twrbo-c-label--promo twrbo-c-label--trim">
                                        <li>
                                            <i class="twrbo-c-iLabel twrbo-c-iLabel--fire"></i>
                                            <span ng-bind="dealItem.promTag" class="ng-binding"></span>
                                        </li>
                                    </ul>
                                </li>
                                <!-- ngRepeat: tag in dealItem.C --><li ng-repeat="tag in dealItem.C" ng-show="dealItem.hasOwnProperty('C')" class="ng-scope">
                                    <a ng-click="onTagClick(tag.filterItemKey, tag.filterItemName)">
                                        <sapn ng-bind="tag.filterItemName" class="ng-binding">點數回饋</sapn></a>
                                </li><!-- end ngRepeat: tag in dealItem.C -->
                            </ul>
                        </div>
                    </div>
                    <div class="twrbo-l-productCard__text">
                        <div class="twrbo-h-margin-bottom-md">
                            <span class="twrbo-c-h3 twrbo-c-link twrbo-c-link--ignoreEffect">
                                <span ng-bind="dealItem.name" class="ng-binding">海底撈火鍋</span>
                            </span>
                        </div>
                        <div class="twrbo-l-productTextCard">
                            <div class="twrbo-l-productTextCard__detail">
                                <p><span ng-bind-html="dealItem.promDesc" class="ng-binding">刷中信卡單月累積滿額贈3%刷卡金(需登錄)</span></p>
                                <div class="twrbo-h-margin-top-sm">
                                    <ul class="twrbo-c-list twrbo-c-list--data twrbo-c-list--small twrbo-c-list--small">
                                        <li ng-show="dealItem.startDay != '' &amp;&amp; dealItem.endDay != ''">
                                            <div class="twrbo-c-additionalicon">
                                                <img src="/content/dam/twrbo/images/icon/icon_clock_dark.svg" alt="" width="16" height="16">
                                                <span ng-bind="dealItem.startDay" class="ng-binding">2023/10/01</span>
                                                <span>~</span>
                                                <span ng-bind="dealItem.endDay" class="ng-binding">2023/12/31</span>
                                            </div>
                                        </li>
                                        <li ng-show="dealItem.hasOwnProperty('B') &amp;&amp; dealItem.B.length > 0">
                                            <div class="twrbo-c-additionalicon">
                                                <img src="/content/dam/twrbo/images/icon/icon_card_dark.svg" alt="" width="16" height="16">
                                                <span>適用
                                                    <!-- ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">無限卡</span>
                                                        <span ng-show="!$last">/</span>
                                                    </span><!-- end ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">世界卡</span>
                                                        <span ng-show="!$last">/</span>
                                                    </span><!-- end ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">極緻卡</span>
                                                        <span ng-show="!$last">/</span>
                                                    </span><!-- end ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">御璽卡</span>
                                                        <span ng-show="!$last">/</span>
                                                    </span><!-- end ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">鈦金卡</span>
                                                        <span ng-show="!$last">/</span>
                                                    </span><!-- end ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">晶緻卡</span>
                                                        <span ng-show="!$last">/</span>
                                                    </span><!-- end ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">聯名認同卡</span>
                                                        <span ng-show="!$last">/</span>
                                                    </span><!-- end ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">所有卡</span>
                                                        <span ng-show="!$last" class="ng-hide">/</span>
                                                    </span><!-- end ngRepeat: card in dealItem.B -->
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
                                                        <a ng-href="https://www.ctbcbank.com/content/dam/minisite/long/creditcard/food2023/index.html" class="twrbo-h-linkEffect-url--gy" href="https://www.ctbcbank.com/content/dam/minisite/long/creditcard/food2023/index.html">
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
                        <span class="twrbo-c-thumb picturefill-background" style="background-image: url(&quot;/content/dam/twrbo/images/creditcard/offer/WOW06.jpg&quot;); background-size: cover; background-repeat: no-repeat; background-position: 50% 50%;">
                            <span data-src="/content/dam/twrbo/images/creditcard/offer/WOW06.jpg" data-src-default="/content/dam/twrbo/images/matchCard.png"></span>
                        </span>
                        <div class="twrbo-h-gutters-out-sm-v">
                            <ul class="twrbo-c-label twrbo-c-label--trim">
                                <li ng-show="dealItem.promTag != ''" class="ng-hide">
                                    <ul class="twrbo-c-label twrbo-c-label--promo twrbo-c-label--trim">
                                        <li>
                                            <i class="twrbo-c-iLabel twrbo-c-iLabel--fire"></i>
                                            <span ng-bind="dealItem.promTag" class="ng-binding"></span>
                                        </li>
                                    </ul>
                                </li>
                                <!-- ngRepeat: tag in dealItem.C --><li ng-repeat="tag in dealItem.C" ng-show="dealItem.hasOwnProperty('C')" class="ng-scope">
                                    <a ng-click="onTagClick(tag.filterItemKey, tag.filterItemName)">
                                        <sapn ng-bind="tag.filterItemName" class="ng-binding">點數回饋</sapn></a>
                                </li><!-- end ngRepeat: tag in dealItem.C -->
                            </ul>
                        </div>
                    </div>
                    <div class="twrbo-l-productCard__text">
                        <div class="twrbo-h-margin-bottom-md">
                            <span class="twrbo-c-h3 twrbo-c-link twrbo-c-link--ignoreEffect">
                                <span ng-bind="dealItem.name" class="ng-binding">夏慕尼 新香榭鉄板燒</span>
                            </span>
                        </div>
                        <div class="twrbo-l-productTextCard">
                            <div class="twrbo-l-productTextCard__detail">
                                <p><span ng-bind-html="dealItem.promDesc" class="ng-binding">使用王品瘋美食App電子錢包瘋Pay且綁定中信卡消費付款，享週六~週日6%瘋點數回饋、週一~週五3%瘋點數回饋。</span></p>
                                <div class="twrbo-h-margin-top-sm">
                                    <ul class="twrbo-c-list twrbo-c-list--data twrbo-c-list--small twrbo-c-list--small">
                                        <li ng-show="dealItem.startDay != '' &amp;&amp; dealItem.endDay != ''">
                                            <div class="twrbo-c-additionalicon">
                                                <img src="/content/dam/twrbo/images/icon/icon_clock_dark.svg" alt="" width="16" height="16">
                                                <span ng-bind="dealItem.startDay" class="ng-binding">2023/10/01</span>
                                                <span>~</span>
                                                <span ng-bind="dealItem.endDay" class="ng-binding">2023/12/31</span>
                                            </div>
                                        </li>
                                        <li ng-show="dealItem.hasOwnProperty('B') &amp;&amp; dealItem.B.length > 0">
                                            <div class="twrbo-c-additionalicon">
                                                <img src="/content/dam/twrbo/images/icon/icon_card_dark.svg" alt="" width="16" height="16">
                                                <span>適用
                                                    <!-- ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">無限卡</span>
                                                        <span ng-show="!$last">/</span>
                                                    </span><!-- end ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">世界卡</span>
                                                        <span ng-show="!$last">/</span>
                                                    </span><!-- end ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">極緻卡</span>
                                                        <span ng-show="!$last">/</span>
                                                    </span><!-- end ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">御璽卡</span>
                                                        <span ng-show="!$last">/</span>
                                                    </span><!-- end ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">鈦金卡</span>
                                                        <span ng-show="!$last">/</span>
                                                    </span><!-- end ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">晶緻卡</span>
                                                        <span ng-show="!$last">/</span>
                                                    </span><!-- end ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">聯名認同卡</span>
                                                        <span ng-show="!$last">/</span>
                                                    </span><!-- end ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">所有卡</span>
                                                        <span ng-show="!$last" class="ng-hide">/</span>
                                                    </span><!-- end ngRepeat: card in dealItem.B -->
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
                                                        <a ng-href="https://www.ctbcbank.com/content/dam/minisite/long/creditcard/wowapp/index.html" class="twrbo-h-linkEffect-url--gy" href="https://www.ctbcbank.com/content/dam/minisite/long/creditcard/wowapp/index.html">
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
                        <span class="twrbo-c-thumb picturefill-background" style="background-image: url(&quot;/content/dam/twrbo/images/creditcard/offer/WOW07.jpg&quot;); background-size: cover; background-repeat: no-repeat; background-position: 50% 50%;">
                            <span data-src="/content/dam/twrbo/images/creditcard/offer/WOW07.jpg" data-src-default="/content/dam/twrbo/images/matchCard.png"></span>
                        </span>
                        <div class="twrbo-h-gutters-out-sm-v">
                            <ul class="twrbo-c-label twrbo-c-label--trim">
                                <li ng-show="dealItem.promTag != ''" class="ng-hide">
                                    <ul class="twrbo-c-label twrbo-c-label--promo twrbo-c-label--trim">
                                        <li>
                                            <i class="twrbo-c-iLabel twrbo-c-iLabel--fire"></i>
                                            <span ng-bind="dealItem.promTag" class="ng-binding"></span>
                                        </li>
                                    </ul>
                                </li>
                                <!-- ngRepeat: tag in dealItem.C --><li ng-repeat="tag in dealItem.C" ng-show="dealItem.hasOwnProperty('C')" class="ng-scope">
                                    <a ng-click="onTagClick(tag.filterItemKey, tag.filterItemName)">
                                        <sapn ng-bind="tag.filterItemName" class="ng-binding">點數回饋</sapn></a>
                                </li><!-- end ngRepeat: tag in dealItem.C -->
                            </ul>
                        </div>
                    </div>
                    <div class="twrbo-l-productCard__text">
                        <div class="twrbo-h-margin-bottom-md">
                            <span class="twrbo-c-h3 twrbo-c-link twrbo-c-link--ignoreEffect">
                                <span ng-bind="dealItem.name" class="ng-binding">TASTy西堤牛排</span>
                            </span>
                        </div>
                        <div class="twrbo-l-productTextCard">
                            <div class="twrbo-l-productTextCard__detail">
                                <p><span ng-bind-html="dealItem.promDesc" class="ng-binding">使用王品瘋美食App電子錢包瘋Pay且綁定中信卡消費付款，享週六~週日6%瘋點數回饋、週一~週五3%瘋點數回饋。</span></p>
                                <div class="twrbo-h-margin-top-sm">
                                    <ul class="twrbo-c-list twrbo-c-list--data twrbo-c-list--small twrbo-c-list--small">
                                        <li ng-show="dealItem.startDay != '' &amp;&amp; dealItem.endDay != ''">
                                            <div class="twrbo-c-additionalicon">
                                                <img src="/content/dam/twrbo/images/icon/icon_clock_dark.svg" alt="" width="16" height="16">
                                                <span ng-bind="dealItem.startDay" class="ng-binding">2023/10/01</span>
                                                <span>~</span>
                                                <span ng-bind="dealItem.endDay" class="ng-binding">2023/12/31</span>
                                            </div>
                                        </li>
                                        <li ng-show="dealItem.hasOwnProperty('B') &amp;&amp; dealItem.B.length > 0">
                                            <div class="twrbo-c-additionalicon">
                                                <img src="/content/dam/twrbo/images/icon/icon_card_dark.svg" alt="" width="16" height="16">
                                                <span>適用
                                                    <!-- ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">無限卡</span>
                                                        <span ng-show="!$last">/</span>
                                                    </span><!-- end ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">世界卡</span>
                                                        <span ng-show="!$last">/</span>
                                                    </span><!-- end ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">極緻卡</span>
                                                        <span ng-show="!$last">/</span>
                                                    </span><!-- end ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">御璽卡</span>
                                                        <span ng-show="!$last">/</span>
                                                    </span><!-- end ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">鈦金卡</span>
                                                        <span ng-show="!$last">/</span>
                                                    </span><!-- end ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">晶緻卡</span>
                                                        <span ng-show="!$last">/</span>
                                                    </span><!-- end ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">聯名認同卡</span>
                                                        <span ng-show="!$last">/</span>
                                                    </span><!-- end ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">所有卡</span>
                                                        <span ng-show="!$last" class="ng-hide">/</span>
                                                    </span><!-- end ngRepeat: card in dealItem.B -->
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
                                                        <a ng-href="https://www.ctbcbank.com/content/dam/minisite/long/creditcard/wowapp/index.html" class="twrbo-h-linkEffect-url--gy" href="https://www.ctbcbank.com/content/dam/minisite/long/creditcard/wowapp/index.html">
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
                        <span class="twrbo-c-thumb picturefill-background" style="background-image: url(&quot;/content/dam/twrbo/images/creditcard/offer/FOOD2301.jpg&quot;); background-size: cover; background-repeat: no-repeat; background-position: 50% 50%;">
                            <span data-src="/content/dam/twrbo/images/creditcard/offer/FOOD2301.jpg" data-src-default="/content/dam/twrbo/images/matchCard.png"></span>
                        </span>
                        <div class="twrbo-h-gutters-out-sm-v">
                            <ul class="twrbo-c-label twrbo-c-label--trim">
                                <li ng-show="dealItem.promTag != ''" class="ng-hide">
                                    <ul class="twrbo-c-label twrbo-c-label--promo twrbo-c-label--trim">
                                        <li>
                                            <i class="twrbo-c-iLabel twrbo-c-iLabel--fire"></i>
                                            <span ng-bind="dealItem.promTag" class="ng-binding"></span>
                                        </li>
                                    </ul>
                                </li>
                                <!-- ngRepeat: tag in dealItem.C --><li ng-repeat="tag in dealItem.C" ng-show="dealItem.hasOwnProperty('C')" class="ng-scope">
                                    <a ng-click="onTagClick(tag.filterItemKey, tag.filterItemName)">
                                        <sapn ng-bind="tag.filterItemName" class="ng-binding">點數回饋</sapn></a>
                                </li><!-- end ngRepeat: tag in dealItem.C -->
                            </ul>
                        </div>
                    </div>
                    <div class="twrbo-l-productCard__text">
                        <div class="twrbo-h-margin-bottom-md">
                            <span class="twrbo-c-h3 twrbo-c-link twrbo-c-link--ignoreEffect">
                                <span ng-bind="dealItem.name" class="ng-binding">築間幸福鍋物</span>
                            </span>
                        </div>
                        <div class="twrbo-l-productTextCard">
                            <div class="twrbo-l-productTextCard__detail">
                                <p><span ng-bind-html="dealItem.promDesc" class="ng-binding">刷中信卡單月累積滿額贈3%刷卡金(需登錄)</span></p>
                                <div class="twrbo-h-margin-top-sm">
                                    <ul class="twrbo-c-list twrbo-c-list--data twrbo-c-list--small twrbo-c-list--small">
                                        <li ng-show="dealItem.startDay != '' &amp;&amp; dealItem.endDay != ''">
                                            <div class="twrbo-c-additionalicon">
                                                <img src="/content/dam/twrbo/images/icon/icon_clock_dark.svg" alt="" width="16" height="16">
                                                <span ng-bind="dealItem.startDay" class="ng-binding">2023/10/01</span>
                                                <span>~</span>
                                                <span ng-bind="dealItem.endDay" class="ng-binding">2023/12/31</span>
                                            </div>
                                        </li>
                                        <li ng-show="dealItem.hasOwnProperty('B') &amp;&amp; dealItem.B.length > 0">
                                            <div class="twrbo-c-additionalicon">
                                                <img src="/content/dam/twrbo/images/icon/icon_card_dark.svg" alt="" width="16" height="16">
                                                <span>適用
                                                    <!-- ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">無限卡</span>
                                                        <span ng-show="!$last">/</span>
                                                    </span><!-- end ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">世界卡</span>
                                                        <span ng-show="!$last">/</span>
                                                    </span><!-- end ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">極緻卡</span>
                                                        <span ng-show="!$last">/</span>
                                                    </span><!-- end ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">御璽卡</span>
                                                        <span ng-show="!$last">/</span>
                                                    </span><!-- end ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">鈦金卡</span>
                                                        <span ng-show="!$last">/</span>
                                                    </span><!-- end ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">晶緻卡</span>
                                                        <span ng-show="!$last">/</span>
                                                    </span><!-- end ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">聯名認同卡</span>
                                                        <span ng-show="!$last">/</span>
                                                    </span><!-- end ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">所有卡</span>
                                                        <span ng-show="!$last" class="ng-hide">/</span>
                                                    </span><!-- end ngRepeat: card in dealItem.B -->
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
                                                        <a ng-href="https://www.ctbcbank.com/content/dam/minisite/long/creditcard/food2023/index.html" class="twrbo-h-linkEffect-url--gy" href="https://www.ctbcbank.com/content/dam/minisite/long/creditcard/food2023/index.html">
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
                        <span class="twrbo-c-thumb picturefill-background" style="background-image: url(&quot;/content/dam/twrbo/images/creditcard/offer/WOW04.jpg&quot;); background-size: cover; background-repeat: no-repeat; background-position: 50% 50%;">
                            <span data-src="/content/dam/twrbo/images/creditcard/offer/WOW04.jpg" data-src-default="/content/dam/twrbo/images/matchCard.png"></span>
                        </span>
                        <div class="twrbo-h-gutters-out-sm-v">
                            <ul class="twrbo-c-label twrbo-c-label--trim">
                                <li ng-show="dealItem.promTag != ''" class="ng-hide">
                                    <ul class="twrbo-c-label twrbo-c-label--promo twrbo-c-label--trim">
                                        <li>
                                            <i class="twrbo-c-iLabel twrbo-c-iLabel--fire"></i>
                                            <span ng-bind="dealItem.promTag" class="ng-binding"></span>
                                        </li>
                                    </ul>
                                </li>
                                <!-- ngRepeat: tag in dealItem.C --><li ng-repeat="tag in dealItem.C" ng-show="dealItem.hasOwnProperty('C')" class="ng-scope">
                                    <a ng-click="onTagClick(tag.filterItemKey, tag.filterItemName)">
                                        <sapn ng-bind="tag.filterItemName" class="ng-binding">點數回饋</sapn></a>
                                </li><!-- end ngRepeat: tag in dealItem.C -->
                            </ul>
                        </div>
                    </div>
                    <div class="twrbo-l-productCard__text">
                        <div class="twrbo-h-margin-bottom-md">
                            <span class="twrbo-c-h3 twrbo-c-link twrbo-c-link--ignoreEffect">
                                <span ng-bind="dealItem.name" class="ng-binding">Oh my!原燒 日式燒肉</span>
                            </span>
                        </div>
                        <div class="twrbo-l-productTextCard">
                            <div class="twrbo-l-productTextCard__detail">
                                <p><span ng-bind-html="dealItem.promDesc" class="ng-binding">使用王品瘋美食App電子錢包瘋Pay且綁定中信卡消費付款，享週六~週日6%瘋點數回饋、週一~週五3%瘋點數回饋。</span></p>
                                <div class="twrbo-h-margin-top-sm">
                                    <ul class="twrbo-c-list twrbo-c-list--data twrbo-c-list--small twrbo-c-list--small">
                                        <li ng-show="dealItem.startDay != '' &amp;&amp; dealItem.endDay != ''">
                                            <div class="twrbo-c-additionalicon">
                                                <img src="/content/dam/twrbo/images/icon/icon_clock_dark.svg" alt="" width="16" height="16">
                                                <span ng-bind="dealItem.startDay" class="ng-binding">2023/10/01</span>
                                                <span>~</span>
                                                <span ng-bind="dealItem.endDay" class="ng-binding">2023/12/31</span>
                                            </div>
                                        </li>
                                        <li ng-show="dealItem.hasOwnProperty('B') &amp;&amp; dealItem.B.length > 0">
                                            <div class="twrbo-c-additionalicon">
                                                <img src="/content/dam/twrbo/images/icon/icon_card_dark.svg" alt="" width="16" height="16">
                                                <span>適用
                                                    <!-- ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">無限卡</span>
                                                        <span ng-show="!$last">/</span>
                                                    </span><!-- end ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">世界卡</span>
                                                        <span ng-show="!$last">/</span>
                                                    </span><!-- end ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">極緻卡</span>
                                                        <span ng-show="!$last">/</span>
                                                    </span><!-- end ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">御璽卡</span>
                                                        <span ng-show="!$last">/</span>
                                                    </span><!-- end ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">鈦金卡</span>
                                                        <span ng-show="!$last">/</span>
                                                    </span><!-- end ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">晶緻卡</span>
                                                        <span ng-show="!$last">/</span>
                                                    </span><!-- end ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">聯名認同卡</span>
                                                        <span ng-show="!$last">/</span>
                                                    </span><!-- end ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">所有卡</span>
                                                        <span ng-show="!$last" class="ng-hide">/</span>
                                                    </span><!-- end ngRepeat: card in dealItem.B -->
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
                                                        <a ng-href="https://www.ctbcbank.com/content/dam/minisite/long/creditcard/wowapp/index.html" class="twrbo-h-linkEffect-url--gy" href="https://www.ctbcbank.com/content/dam/minisite/long/creditcard/wowapp/index.html">
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
                        <span class="twrbo-c-thumb picturefill-background" style="background-image: url(&quot;/content/dam/twrbo/images/creditcard/offer/WOW08.jpg&quot;); background-size: cover; background-repeat: no-repeat; background-position: 50% 50%;">
                            <span data-src="/content/dam/twrbo/images/creditcard/offer/WOW08.jpg" data-src-default="/content/dam/twrbo/images/matchCard.png"></span>
                        </span>
                        <div class="twrbo-h-gutters-out-sm-v">
                            <ul class="twrbo-c-label twrbo-c-label--trim">
                                <li ng-show="dealItem.promTag != ''" class="ng-hide">
                                    <ul class="twrbo-c-label twrbo-c-label--promo twrbo-c-label--trim">
                                        <li>
                                            <i class="twrbo-c-iLabel twrbo-c-iLabel--fire"></i>
                                            <span ng-bind="dealItem.promTag" class="ng-binding"></span>
                                        </li>
                                    </ul>
                                </li>
                                <!-- ngRepeat: tag in dealItem.C --><li ng-repeat="tag in dealItem.C" ng-show="dealItem.hasOwnProperty('C')" class="ng-scope">
                                    <a ng-click="onTagClick(tag.filterItemKey, tag.filterItemName)">
                                        <sapn ng-bind="tag.filterItemName" class="ng-binding">點數回饋</sapn></a>
                                </li><!-- end ngRepeat: tag in dealItem.C -->
                            </ul>
                        </div>
                    </div>
                    <div class="twrbo-l-productCard__text">
                        <div class="twrbo-h-margin-bottom-md">
                            <span class="twrbo-c-h3 twrbo-c-link twrbo-c-link--ignoreEffect">
                                <span ng-bind="dealItem.name" class="ng-binding">品田牧場</span>
                            </span>
                        </div>
                        <div class="twrbo-l-productTextCard">
                            <div class="twrbo-l-productTextCard__detail">
                                <p><span ng-bind-html="dealItem.promDesc" class="ng-binding">使用王品瘋美食App電子錢包瘋Pay且綁定中信卡消費付款，享週六~週日6%瘋點數回饋、週一~週五3%瘋點數回饋。</span></p>
                                <div class="twrbo-h-margin-top-sm">
                                    <ul class="twrbo-c-list twrbo-c-list--data twrbo-c-list--small twrbo-c-list--small">
                                        <li ng-show="dealItem.startDay != '' &amp;&amp; dealItem.endDay != ''">
                                            <div class="twrbo-c-additionalicon">
                                                <img src="/content/dam/twrbo/images/icon/icon_clock_dark.svg" alt="" width="16" height="16">
                                                <span ng-bind="dealItem.startDay" class="ng-binding">2023/10/01</span>
                                                <span>~</span>
                                                <span ng-bind="dealItem.endDay" class="ng-binding">2023/12/31</span>
                                            </div>
                                        </li>
                                        <li ng-show="dealItem.hasOwnProperty('B') &amp;&amp; dealItem.B.length > 0">
                                            <div class="twrbo-c-additionalicon">
                                                <img src="/content/dam/twrbo/images/icon/icon_card_dark.svg" alt="" width="16" height="16">
                                                <span>適用
                                                    <!-- ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">無限卡</span>
                                                        <span ng-show="!$last">/</span>
                                                    </span><!-- end ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">世界卡</span>
                                                        <span ng-show="!$last">/</span>
                                                    </span><!-- end ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">極緻卡</span>
                                                        <span ng-show="!$last">/</span>
                                                    </span><!-- end ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">御璽卡</span>
                                                        <span ng-show="!$last">/</span>
                                                    </span><!-- end ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">鈦金卡</span>
                                                        <span ng-show="!$last">/</span>
                                                    </span><!-- end ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">晶緻卡</span>
                                                        <span ng-show="!$last">/</span>
                                                    </span><!-- end ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">聯名認同卡</span>
                                                        <span ng-show="!$last">/</span>
                                                    </span><!-- end ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">所有卡</span>
                                                        <span ng-show="!$last" class="ng-hide">/</span>
                                                    </span><!-- end ngRepeat: card in dealItem.B -->
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
                                                        <a ng-href="https://www.ctbcbank.com/content/dam/minisite/long/creditcard/wowapp/index.html" class="twrbo-h-linkEffect-url--gy" href="https://www.ctbcbank.com/content/dam/minisite/long/creditcard/wowapp/index.html">
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
csv_file_path = '中信餐飲短期優惠1.csv'
csv_columns = ['優惠名稱', '促銷描述', '開始日期', '結束日期', '適用卡片範疇']

with open(csv_file_path, 'w', newline='', encoding='utf-8-sig') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=csv_columns)
    writer.writeheader()
    for data in result_data:
        writer.writerow(data)

print(f'資料已經擷取並保存到 {csv_file_path}')