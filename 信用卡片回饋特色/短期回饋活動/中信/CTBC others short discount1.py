import csv
from bs4 import BeautifulSoup

html = """
    <div class="twrbo-l-result__data">
            <div class="twrbo-l-resultList" data-list-id="creditcard" ng-show="isDealListSuccess &amp;&amp; dealList.totalDataRows > 0 ">
                
                <!-- ngRepeat: dealItem in dealList.promotionDetailList --><div ng-repeat="dealItem in dealList.promotionDetailList" class="twrbo-l-productCard twrbo-l-productCard--list ng-scope">
                    <div class="twrbo-l-productCard__thumb">
                        <span class="twrbo-c-thumb picturefill-background" style="background-image: url(&quot;/content/dam/twrbo/images/creditcard/offer/TC001.jpg&quot;); background-size: cover; background-repeat: no-repeat; background-position: 50% 50%;">
                            <span data-src="/content/dam/twrbo/images/creditcard/offer/TC001.jpg" data-src-default="/content/dam/twrbo/images/matchCard.png"></span>
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
                                        <sapn ng-bind="tag.filterItemName" class="ng-binding">分期0利率</sapn></a>
                                </li><!-- end ngRepeat: tag in dealItem.C -->
                            </ul>
                        </div>
                    </div>
                    <div class="twrbo-l-productCard__text">
                        <div class="twrbo-h-margin-bottom-md">
                            <span class="twrbo-c-h3 twrbo-c-link twrbo-c-link--ignoreEffect">
                                <span ng-bind="dealItem.name" class="ng-binding">燦坤</span>
                            </span>
                        </div>
                        <div class="twrbo-l-productTextCard">
                            <div class="twrbo-l-productTextCard__detail">
                                <p><span ng-bind-html="dealItem.promDesc" class="ng-binding">於燦坤線上購物刷中信卡單筆滿額最高折12,000元。</span></p>
                                <div class="twrbo-h-margin-top-sm">
                                    <ul class="twrbo-c-list twrbo-c-list--data twrbo-c-list--small twrbo-c-list--small">
                                        <li ng-show="dealItem.startDay != '' &amp;&amp; dealItem.endDay != ''">
                                            <div class="twrbo-c-additionalicon">
                                                <img src="/content/dam/twrbo/images/icon/icon_clock_dark.svg" alt="" width="16" height="16">
                                                <span ng-bind="dealItem.startDay" class="ng-binding">2023/11/01</span>
                                                <span>~</span>
                                                <span ng-bind="dealItem.endDay" class="ng-binding">2023/11/30</span>
                                            </div>
                                        </li>
                                        <li ng-show="dealItem.hasOwnProperty('B') &amp;&amp; dealItem.B.length > 0">
                                            <div class="twrbo-c-additionalicon">
                                                <img src="/content/dam/twrbo/images/icon/icon_card_dark.svg" alt="" width="16" height="16">
                                                <span>適用
                                                    <!-- ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">鼎極卡</span>
                                                        <span ng-show="!$last">/</span>
                                                    </span><!-- end ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">鈦金/御璽/晶緻卡</span>
                                                        <span ng-show="!$last">/</span>
                                                    </span><!-- end ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">聯名認同卡</span>
                                                        <span ng-show="!$last">/</span>
                                                    </span><!-- end ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">白金卡以上</span>
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
                                                        <a ng-href="https://mkt.ctbcbank.com/long/creditcard/tk3c/index.html" class="twrbo-h-linkEffect-url--gy" href="https://mkt.ctbcbank.com/long/creditcard/tk3c/index.html">
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
                        <span class="twrbo-c-thumb picturefill-background" style="background-image: url(&quot;/content/dam/twrbo/images/creditcard/offer/PAY0703.jpg&quot;); background-size: cover; background-repeat: no-repeat; background-position: 50% 50%;">
                            <span data-src="/content/dam/twrbo/images/creditcard/offer/PAY0703.jpg" data-src-default="/content/dam/twrbo/images/matchCard.png"></span>
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
                                <span ng-bind="dealItem.name" class="ng-binding">寶島眼鏡</span>
                            </span>
                        </div>
                        <div class="twrbo-l-productTextCard">
                            <div class="twrbo-l-productTextCard__detail">
                                <p><span ng-bind-html="dealItem.promDesc" class="ng-binding">全台【寶島眼鏡】實體門市刷中信卡，單筆消費滿3,500元享100元刷卡金。</span></p>
                                <div class="twrbo-h-margin-top-sm">
                                    <ul class="twrbo-c-list twrbo-c-list--data twrbo-c-list--small twrbo-c-list--small">
                                        <li ng-show="dealItem.startDay != '' &amp;&amp; dealItem.endDay != ''">
                                            <div class="twrbo-c-additionalicon">
                                                <img src="/content/dam/twrbo/images/icon/icon_clock_dark.svg" alt="" width="16" height="16">
                                                <span ng-bind="dealItem.startDay" class="ng-binding">2023/07/01</span>
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
                                                        <a ng-href="https://mkt.ctbcbank.com/recent/202312/NB2023060641-31/index.html" class="twrbo-h-linkEffect-url--gy" href="https://mkt.ctbcbank.com/recent/202312/NB2023060641-31/index.html">
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
                        <span class="twrbo-c-thumb picturefill-background" style="background-image: url(&quot;/content/dam/twrbo/images/creditcard/offer/PO000001.jpg&quot;); background-size: cover; background-repeat: no-repeat; background-position: 50% 50%;">
                            <span data-src="/content/dam/twrbo/images/creditcard/offer/PO000001.jpg" data-src-default="/content/dam/twrbo/images/matchCard.png"></span>
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
                                <span ng-bind="dealItem.name" class="ng-binding">新竹保時捷中心</span>
                            </span>
                        </div>
                        <div class="twrbo-l-productTextCard">
                            <div class="twrbo-l-productTextCard__detail">
                                <p><span ng-bind-html="dealItem.promDesc" class="ng-binding">購車/保修刷中信卡，滿額享最高4,500元回饋</span></p>
                                <div class="twrbo-h-margin-top-sm">
                                    <ul class="twrbo-c-list twrbo-c-list--data twrbo-c-list--small twrbo-c-list--small">
                                        <li ng-show="dealItem.startDay != '' &amp;&amp; dealItem.endDay != ''">
                                            <div class="twrbo-c-additionalicon">
                                                <img src="/content/dam/twrbo/images/icon/icon_clock_dark.svg" alt="" width="16" height="16">
                                                <span ng-bind="dealItem.startDay" class="ng-binding">2023/09/01</span>
                                                <span>~</span>
                                                <span ng-bind="dealItem.endDay" class="ng-binding">2023/11/30</span>
                                            </div>
                                        </li>
                                        <li ng-show="dealItem.hasOwnProperty('B') &amp;&amp; dealItem.B.length > 0">
                                            <div class="twrbo-c-additionalicon">
                                                <img src="/content/dam/twrbo/images/icon/icon_card_dark.svg" alt="" width="16" height="16">
                                                <span>適用
                                                    <!-- ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">鼎極卡</span>
                                                        <span ng-show="!$last">/</span>
                                                    </span><!-- end ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">鈦金/御璽/晶緻卡</span>
                                                        <span ng-show="!$last">/</span>
                                                    </span><!-- end ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">聯名認同卡</span>
                                                        <span ng-show="!$last">/</span>
                                                    </span><!-- end ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">白金卡以上</span>
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
                                                        <a ng-href="https://mkt.ctbcbank.com/long/creditcard/porche/index.html" class="twrbo-h-linkEffect-url--gy" href="https://mkt.ctbcbank.com/long/creditcard/porche/index.html">
                                                            <span>活動網頁</span>
                                                        </a>
                                                    </div>
                                                </li>
                                                <li ng-show="dealItem.notice != ''" class="ng-hide">
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
                        <span class="twrbo-c-thumb picturefill-background" style="background-image: url(&quot;/content/dam/twrbo/images/creditcard/offer/TA000001.jpg&quot;); background-size: cover; background-repeat: no-repeat; background-position: 50% 50%;">
                            <span data-src="/content/dam/twrbo/images/creditcard/offer/TA000001.jpg" data-src-default="/content/dam/twrbo/images/matchCard.png"></span>
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
                                        <sapn ng-bind="tag.filterItemName" class="ng-binding">分期0利率</sapn></a>
                                </li><!-- end ngRepeat: tag in dealItem.C -->
                            </ul>
                        </div>
                    </div>
                    <div class="twrbo-l-productCard__text">
                        <div class="twrbo-h-margin-bottom-md">
                            <span class="twrbo-c-h3 twrbo-c-link twrbo-c-link--ignoreEffect">
                                <span ng-bind="dealItem.name" class="ng-binding">TOYOTA/LEXUS</span>
                            </span>
                        </div>
                        <div class="twrbo-l-productTextCard">
                            <div class="twrbo-l-productTextCard__detail">
                                <p><span ng-bind-html="dealItem.promDesc" class="ng-binding">刷中信卡分期，滿額登錄享最高2,000元刷卡金回饋</span></p>
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
                                                        <span ng-bind="card.filterItemName" class="ng-binding">鼎極卡</span>
                                                        <span ng-show="!$last">/</span>
                                                    </span><!-- end ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">鈦金/御璽/晶緻卡</span>
                                                        <span ng-show="!$last">/</span>
                                                    </span><!-- end ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">聯名認同卡</span>
                                                        <span ng-show="!$last">/</span>
                                                    </span><!-- end ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">白金卡以上</span>
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
                                                        <a ng-href="https://www.ctbcbank.com/content/dam/minisite/long/creditcard/toyota/index.html" class="twrbo-h-linkEffect-url--gy" href="https://www.ctbcbank.com/content/dam/minisite/long/creditcard/toyota/index.html">
                                                            <span>活動網頁</span>
                                                        </a>
                                                    </div>
                                                </li>
                                                <li ng-show="dealItem.notice != ''" class="ng-hide">
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
                        <span class="twrbo-c-thumb picturefill-background" style="background-image: url(&quot;/content/dam/twrbo/images/creditcard/offer/IO000001.jpg&quot;); background-size: cover; background-repeat: no-repeat; background-position: 50% 50%;">
                            <span data-src="/content/dam/twrbo/images/creditcard/offer/IO000001.jpg" data-src-default="/content/dam/twrbo/images/matchCard.png"></span>
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
                                <span ng-bind="dealItem.name" class="ng-binding">光陽電動車IONEX</span>
                            </span>
                        </div>
                        <div class="twrbo-l-productTextCard">
                            <div class="twrbo-l-productTextCard__detail">
                                <p><span ng-bind-html="dealItem.promDesc" class="ng-binding">12期分期0利率，滿額登錄享最高2,000元刷卡金</span></p>
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
                                                        <span ng-bind="card.filterItemName" class="ng-binding">鼎極卡</span>
                                                        <span ng-show="!$last">/</span>
                                                    </span><!-- end ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">鈦金/御璽/晶緻卡</span>
                                                        <span ng-show="!$last">/</span>
                                                    </span><!-- end ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">聯名認同卡</span>
                                                        <span ng-show="!$last">/</span>
                                                    </span><!-- end ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">白金卡以上</span>
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
                                                        <a ng-href="https://www.ctbcbank.com/content/dam/minisite/long/creditcard/ionex/index.html" class="twrbo-h-linkEffect-url--gy" href="https://www.ctbcbank.com/content/dam/minisite/long/creditcard/ionex/index.html">
                                                            <span>活動網頁</span>
                                                        </a>
                                                    </div>
                                                </li>
                                                <li ng-show="dealItem.notice != ''" class="ng-hide">
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
                        <span class="twrbo-c-thumb picturefill-background" style="background-image: url(&quot;/content/dam/twrbo/images/creditcard/offer/TR000001.jpg&quot;); background-size: cover; background-repeat: no-repeat; background-position: 50% 50%;">
                            <span data-src="/content/dam/twrbo/images/creditcard/offer/TR000001.jpg" data-src-default="/content/dam/twrbo/images/matchCard.png"></span>
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
                                <span ng-bind="dealItem.name" class="ng-binding">中信卡愛車好行</span>
                            </span>
                        </div>
                        <div class="twrbo-l-productTextCard">
                            <div class="twrbo-l-productTextCard__detail">
                                <p><span ng-bind-html="dealItem.promDesc" class="ng-binding">【購車保修、車用精品】指定商店分期消費且完成登錄，享刷卡金最高2,000元回饋</span></p>
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
                                                        <span ng-bind="card.filterItemName" class="ng-binding">鼎極卡</span>
                                                        <span ng-show="!$last">/</span>
                                                    </span><!-- end ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">鈦金/御璽/晶緻卡</span>
                                                        <span ng-show="!$last">/</span>
                                                    </span><!-- end ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">聯名認同卡</span>
                                                        <span ng-show="!$last">/</span>
                                                    </span><!-- end ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">白金卡以上</span>
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
                                                        <a ng-href="https://www.ctbcbank.com/content/dam/minisite/long/creditcard/traffic/index.html" class="twrbo-h-linkEffect-url--gy" href="https://www.ctbcbank.com/content/dam/minisite/long/creditcard/traffic/index.html">
                                                            <span>活動網頁</span>
                                                        </a>
                                                    </div>
                                                </li>
                                                <li ng-show="dealItem.notice != ''" class="ng-hide">
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
                        <span class="twrbo-c-thumb picturefill-background" style="background-image: url(&quot;/content/dam/twrbo/images/creditcard/offer/KM000001.jpg&quot;); background-size: cover; background-repeat: no-repeat; background-position: 50% 50%;">
                            <span data-src="/content/dam/twrbo/images/creditcard/offer/KM000001.jpg" data-src-default="/content/dam/twrbo/images/matchCard.png"></span>
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
                                <span ng-bind="dealItem.name" class="ng-binding">中信卡搭高捷 車資滿額享30%回饋</span>
                            </span>
                        </div>
                        <div class="twrbo-l-productTextCard">
                            <div class="twrbo-l-productTextCard__detail">
                                <p><span ng-bind-html="dealItem.promDesc" class="ng-binding">使用中信卡（含感應式、綁定手機或穿戴裝置）感應支付搭乘高雄捷運，累積消費達200元即享30%刷卡金回饋。</span></p>
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
                                                        <span ng-bind="card.filterItemName" class="ng-binding">鼎極卡</span>
                                                        <span ng-show="!$last">/</span>
                                                    </span><!-- end ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">鈦金/御璽/晶緻卡</span>
                                                        <span ng-show="!$last">/</span>
                                                    </span><!-- end ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">聯名認同卡</span>
                                                        <span ng-show="!$last">/</span>
                                                    </span><!-- end ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">白金卡以上</span>
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
                                                        <a ng-href="https://www.ctbcbank.com/content/dam/minisite/long/creditcard/krtc/index.html" class="twrbo-h-linkEffect-url--gy" href="https://www.ctbcbank.com/content/dam/minisite/long/creditcard/krtc/index.html">
                                                            <span>活動網頁</span>
                                                        </a>
                                                    </div>
                                                </li>
                                                <li ng-show="dealItem.notice != ''" class="ng-hide">
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
                        <span class="twrbo-c-thumb picturefill-background" style="background-image: url(&quot;/content/dam/twrbo/images/creditcard/offer/GO000001.jpg&quot;); background-size: cover; background-repeat: no-repeat; background-position: 50% 50%;">
                            <span data-src="/content/dam/twrbo/images/creditcard/offer/GO000001.jpg" data-src-default="/content/dam/twrbo/images/matchCard.png"></span>
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
                                        <sapn ng-bind="tag.filterItemName" class="ng-binding">分期0利率</sapn></a>
                                </li><!-- end ngRepeat: tag in dealItem.C -->
                            </ul>
                        </div>
                    </div>
                    <div class="twrbo-l-productCard__text">
                        <div class="twrbo-h-margin-bottom-md">
                            <span class="twrbo-c-h3 twrbo-c-link twrbo-c-link--ignoreEffect">
                                <span ng-bind="dealItem.name" class="ng-binding">中信卡輕鬆購 Gogoro暢快騎</span>
                            </span>
                        </div>
                        <div class="twrbo-l-productTextCard">
                            <div class="twrbo-l-productTextCard__detail">
                                <p><span ng-bind-html="dealItem.promDesc" class="ng-binding">12期分期0利率 滿額贈刷卡金</span></p>
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
                                                        <span ng-bind="card.filterItemName" class="ng-binding">鼎極卡</span>
                                                        <span ng-show="!$last">/</span>
                                                    </span><!-- end ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">鈦金/御璽/晶緻卡</span>
                                                        <span ng-show="!$last">/</span>
                                                    </span><!-- end ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">聯名認同卡</span>
                                                        <span ng-show="!$last">/</span>
                                                    </span><!-- end ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">白金卡以上</span>
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
                                                        <a ng-href="https://www.ctbcbank.com/content/dam/minisite/long/creditcard/gogoro/index.html" class="twrbo-h-linkEffect-url--gy" href="https://www.ctbcbank.com/content/dam/minisite/long/creditcard/gogoro/index.html">
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
                        <span class="twrbo-c-thumb picturefill-background" style="background-image: url(&quot;/content/dam/twrbo/images/creditcard/offer/IR000001.jpg&quot;); background-size: cover; background-repeat: no-repeat; background-position: 50% 50%;">
                            <span data-src="/content/dam/twrbo/images/creditcard/offer/IR000001.jpg" data-src-default="/content/dam/twrbo/images/matchCard.png"></span>
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
                                <span ng-bind="dealItem.name" class="ng-binding">中信卡尊享iRent雙重優惠</span>
                            </span>
                        </div>
                        <div class="twrbo-l-productTextCard">
                            <div class="twrbo-l-productTextCard__detail">
                                <p><span ng-bind-html="dealItem.promDesc" class="ng-binding">最高可獲得汽車120分鐘</span></p>
                                <div class="twrbo-h-margin-top-sm">
                                    <ul class="twrbo-c-list twrbo-c-list--data twrbo-c-list--small twrbo-c-list--small">
                                        <li ng-show="dealItem.startDay != '' &amp;&amp; dealItem.endDay != ''">
                                            <div class="twrbo-c-additionalicon">
                                                <img src="/content/dam/twrbo/images/icon/icon_clock_dark.svg" alt="" width="16" height="16">
                                                <span ng-bind="dealItem.startDay" class="ng-binding">2023/08/10</span>
                                                <span>~</span>
                                                <span ng-bind="dealItem.endDay" class="ng-binding">2023/12/31</span>
                                            </div>
                                        </li>
                                        <li ng-show="dealItem.hasOwnProperty('B') &amp;&amp; dealItem.B.length > 0">
                                            <div class="twrbo-c-additionalicon">
                                                <img src="/content/dam/twrbo/images/icon/icon_card_dark.svg" alt="" width="16" height="16">
                                                <span>適用
                                                    <!-- ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">鼎極卡</span>
                                                        <span ng-show="!$last">/</span>
                                                    </span><!-- end ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">鈦金/御璽/晶緻卡</span>
                                                        <span ng-show="!$last">/</span>
                                                    </span><!-- end ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">聯名認同卡</span>
                                                        <span ng-show="!$last">/</span>
                                                    </span><!-- end ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">白金卡以上</span>
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
                                                        <a ng-href="https://www.ctbcbank.com/content/dam/minisite/long/creditcard/irentcar/index.html" class="twrbo-h-linkEffect-url--gy" href="https://www.ctbcbank.com/content/dam/minisite/long/creditcard/irentcar/index.html">
                                                            <span>活動網頁</span>
                                                        </a>
                                                    </div>
                                                </li>
                                                <li ng-show="dealItem.notice != ''" class="ng-hide">
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
                        <span class="twrbo-c-thumb picturefill-background" style="background-image: url(&quot;/content/dam/twrbo/images/creditcard/offer/O000099.jpg&quot;); background-size: cover; background-repeat: no-repeat; background-position: 50% 50%;">
                            <span data-src="/content/dam/twrbo/images/creditcard/offer/O000099.jpg" data-src-default="/content/dam/twrbo/images/matchCard.png"></span>
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
                                <!-- ngRepeat: tag in dealItem.C -->
                            </ul>
                        </div>
                    </div>
                    <div class="twrbo-l-productCard__text">
                        <div class="twrbo-h-margin-bottom-md">
                            <span class="twrbo-c-h3 twrbo-c-link twrbo-c-link--ignoreEffect">
                                <span ng-bind="dealItem.name" class="ng-binding">中信卡代扣繳  帳單整合不漏單</span>
                            </span>
                        </div>
                        <div class="twrbo-l-productTextCard">
                            <div class="twrbo-l-productTextCard__detail">
                                <p><span ng-bind-html="dealItem.promDesc" class="ng-binding">整合帳單不漏繳，脫單Easy GO!</span></p>
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
                                        <li ng-show="dealItem.hasOwnProperty('B') &amp;&amp; dealItem.B.length > 0">
                                            <div class="twrbo-c-additionalicon">
                                                <img src="/content/dam/twrbo/images/icon/icon_card_dark.svg" alt="" width="16" height="16">
                                                <span>適用
                                                    <!-- ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">鼎極卡</span>
                                                        <span ng-show="!$last">/</span>
                                                    </span><!-- end ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">鈦金/御璽/晶緻卡</span>
                                                        <span ng-show="!$last">/</span>
                                                    </span><!-- end ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">聯名認同卡</span>
                                                        <span ng-show="!$last">/</span>
                                                    </span><!-- end ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">白金卡以上</span>
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
                                                        <a ng-href="https://www.ctbcbank.com/content/dam/minisite/long/creditcard/NB2019070227/index.html" class="twrbo-h-linkEffect-url--gy" href="https://www.ctbcbank.com/content/dam/minisite/long/creditcard/NB2019070227/index.html">
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
                        <span class="twrbo-c-thumb picturefill-background" style="background-image: url(&quot;/content/dam/twrbo/images/creditcard/offer/RT000001.jpg&quot;); background-size: cover; background-repeat: no-repeat; background-position: 50% 50%;">
                            <span data-src="/content/dam/twrbo/images/creditcard/offer/RT000001.jpg" data-src-default="/content/dam/twrbo/images/matchCard.png"></span>
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
                                <span ng-bind="dealItem.name" class="ng-binding">中信卡租車優惠</span>
                            </span>
                        </div>
                        <div class="twrbo-l-productTextCard">
                            <div class="twrbo-l-productTextCard__detail">
                                <p><span ng-bind-html="dealItem.promDesc" class="ng-binding">享租車優惠7折起</span></p>
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
                                                        <span ng-bind="card.filterItemName" class="ng-binding">鼎極卡</span>
                                                        <span ng-show="!$last">/</span>
                                                    </span><!-- end ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">鈦金/御璽/晶緻卡</span>
                                                        <span ng-show="!$last">/</span>
                                                    </span><!-- end ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">聯名認同卡</span>
                                                        <span ng-show="!$last">/</span>
                                                    </span><!-- end ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">白金卡以上</span>
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
                                                        <a ng-href="https://www.ctbcbank.com/content/dam/minisite/long/creditcard/rental/index.html" class="twrbo-h-linkEffect-url--gy" href="https://www.ctbcbank.com/content/dam/minisite/long/creditcard/rental/index.html">
                                                            <span>活動網頁</span>
                                                        </a>
                                                    </div>
                                                </li>
                                                <li ng-show="dealItem.notice != ''" class="ng-hide">
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
                        <span class="twrbo-c-thumb picturefill-background" style="background-image: url(&quot;/content/dam/twrbo/images/creditcard/offer/WHT0001.jpg&quot;); background-size: cover; background-repeat: no-repeat; background-position: 50% 50%;">
                            <span data-src="/content/dam/twrbo/images/creditcard/offer/WHT0001.jpg" data-src-default="/content/dam/twrbo/images/matchCard.png"></span>
                        </span>
                        <div class="twrbo-h-gutters-out-sm-v">
                            <ul class="twrbo-c-label twrbo-c-label--trim">
                                <li ng-show="dealItem.promTag != ''">
                                    <ul class="twrbo-c-label twrbo-c-label--promo twrbo-c-label--trim">
                                        <li>
                                            <i class="twrbo-c-iLabel twrbo-c-iLabel--fire"></i>
                                            <span ng-bind="dealItem.promTag" class="ng-binding">折扣優惠</span>
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
                                <span ng-bind="dealItem.name" class="ng-binding">萬花筒劇團《2023彩虹音樂森林》</span>
                            </span>
                        </div>
                        <div class="twrbo-l-productTextCard">
                            <div class="twrbo-l-productTextCard__detail">
                                <p><span ng-bind-html="dealItem.promDesc" class="ng-binding">網路購票刷中信卡（含簽帳卡），享9折優惠</span></p>
                                <div class="twrbo-h-margin-top-sm">
                                    <ul class="twrbo-c-list twrbo-c-list--data twrbo-c-list--small twrbo-c-list--small">
                                        <li ng-show="dealItem.startDay != '' &amp;&amp; dealItem.endDay != ''">
                                            <div class="twrbo-c-additionalicon">
                                                <img src="/content/dam/twrbo/images/icon/icon_clock_dark.svg" alt="" width="16" height="16">
                                                <span ng-bind="dealItem.startDay" class="ng-binding">2023/09/23</span>
                                                <span>~</span>
                                                <span ng-bind="dealItem.endDay" class="ng-binding">2023/12/16</span>
                                            </div>
                                        </li>
                                        <li ng-show="dealItem.hasOwnProperty('B') &amp;&amp; dealItem.B.length > 0">
                                            <div class="twrbo-c-additionalicon">
                                                <img src="/content/dam/twrbo/images/icon/icon_card_dark.svg" alt="" width="16" height="16">
                                                <span>適用
                                                    <!-- ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">鼎極卡</span>
                                                        <span ng-show="!$last">/</span>
                                                    </span><!-- end ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">鈦金/御璽/晶緻卡</span>
                                                        <span ng-show="!$last">/</span>
                                                    </span><!-- end ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">聯名認同卡</span>
                                                        <span ng-show="!$last">/</span>
                                                    </span><!-- end ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">白金卡以上</span>
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
                                                <li ng-show="dealItem.storeUrl != ''">
                                                    <div class="twrbo-c-additionalicon">
                                                        <img src="/content/dam/twrbo/images/icon/icon_global_dark.svg" alt="" width="16" height="16">
                                                        <a ng-href="https://www.opentix.life/event/1676445432247250945" class="twrbo-h-linkEffect-url--gy" href="https://www.opentix.life/event/1676445432247250945">
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
                        <span class="twrbo-c-thumb picturefill-background" style="background-image: url(&quot;/content/dam/twrbo/images/creditcard/offer/Redeem000001.jpg&quot;); background-size: cover; background-repeat: no-repeat; background-position: 50% 50%;">
                            <span data-src="/content/dam/twrbo/images/creditcard/offer/Redeem000001.jpg" data-src-default="/content/dam/twrbo/images/matchCard.png"></span>
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
                                <span ng-bind="dealItem.name" class="ng-binding">台灣大車隊股份有限公司</span>
                            </span>
                        </div>
                        <div class="twrbo-l-productTextCard">
                            <div class="twrbo-l-productTextCard__detail">
                                <p><span ng-bind-html="dealItem.promDesc" class="ng-binding">*中信卡紅利點數每100點折抵NT8元，折抵上限為單筆消費金額20%。</span></p>
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
                                                        <span ng-bind="card.filterItemName" class="ng-binding">鼎極卡</span>
                                                        <span ng-show="!$last">/</span>
                                                    </span><!-- end ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">鈦金/御璽/晶緻卡</span>
                                                        <span ng-show="!$last">/</span>
                                                    </span><!-- end ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">白金卡以上</span>
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
                                                <li ng-show="dealItem.phone != ''">
                                                    <div class="twrbo-c-additionalicon">
                                                        <img src="/content/dam/twrbo/images/icon/icon_phone_dark.svg" alt="" width="16" height="16">
                                                        <a ng-href="tel:0225160966" target="_parent" class="twrbo-h-linkEffect-url--gy twrbo-c-link--tel" href="tel:0225160966">
                                                            <span ng-bind="dealItem.phone" class="ng-binding">02-25160966</span>
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
                                                <li ng-show="dealItem.storeUrl != ''">
                                                    <div class="twrbo-c-additionalicon">
                                                        <img src="/content/dam/twrbo/images/icon/icon_global_dark.svg" alt="" width="16" height="16">
                                                        <a ng-href="http://www.taiwantaxi.com.tw/" class="twrbo-h-linkEffect-url--gy" href="http://www.taiwantaxi.com.tw/">
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
                        <span class="twrbo-c-thumb picturefill-background" style="background-image: url(&quot;/content/dam/twrbo/images/creditcard/offer/SAX0001.jpg&quot;); background-size: cover; background-repeat: no-repeat; background-position: 50% 50%;">
                            <span data-src="/content/dam/twrbo/images/creditcard/offer/SAX0001.jpg" data-src-default="/content/dam/twrbo/images/matchCard.png"></span>
                        </span>
                        <div class="twrbo-h-gutters-out-sm-v">
                            <ul class="twrbo-c-label twrbo-c-label--trim">
                                <li ng-show="dealItem.promTag != ''">
                                    <ul class="twrbo-c-label twrbo-c-label--promo twrbo-c-label--trim">
                                        <li>
                                            <i class="twrbo-c-iLabel twrbo-c-iLabel--fire"></i>
                                            <span ng-bind="dealItem.promTag" class="ng-binding">折扣優惠</span>
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
                                <span ng-bind="dealItem.name" class="ng-binding">薩克斯瘋四怪客《Super Sax Show》</span>
                            </span>
                        </div>
                        <div class="twrbo-l-productTextCard">
                            <div class="twrbo-l-productTextCard__detail">
                                <p><span ng-bind-html="dealItem.promDesc" class="ng-binding">網路購票刷中信卡（含簽帳卡），享92折優惠 (適用於NT1,200元(含)以上票區)</span></p>
                                <div class="twrbo-h-margin-top-sm">
                                    <ul class="twrbo-c-list twrbo-c-list--data twrbo-c-list--small twrbo-c-list--small">
                                        <li ng-show="dealItem.startDay != '' &amp;&amp; dealItem.endDay != ''">
                                            <div class="twrbo-c-additionalicon">
                                                <img src="/content/dam/twrbo/images/icon/icon_clock_dark.svg" alt="" width="16" height="16">
                                                <span ng-bind="dealItem.startDay" class="ng-binding">2023/11/01</span>
                                                <span>~</span>
                                                <span ng-bind="dealItem.endDay" class="ng-binding">2023/11/26</span>
                                            </div>
                                        </li>
                                        <li ng-show="dealItem.hasOwnProperty('B') &amp;&amp; dealItem.B.length > 0">
                                            <div class="twrbo-c-additionalicon">
                                                <img src="/content/dam/twrbo/images/icon/icon_card_dark.svg" alt="" width="16" height="16">
                                                <span>適用
                                                    <!-- ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">鼎極卡</span>
                                                        <span ng-show="!$last">/</span>
                                                    </span><!-- end ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">鈦金/御璽/晶緻卡</span>
                                                        <span ng-show="!$last">/</span>
                                                    </span><!-- end ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">聯名認同卡</span>
                                                        <span ng-show="!$last">/</span>
                                                    </span><!-- end ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">白金卡以上</span>
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
                                                <li ng-show="dealItem.storeUrl != ''">
                                                    <div class="twrbo-c-additionalicon">
                                                        <img src="/content/dam/twrbo/images/icon/icon_global_dark.svg" alt="" width="16" height="16">
                                                        <a ng-href="https://bit.ly/3MwxkwT" class="twrbo-h-linkEffect-url--gy" href="https://bit.ly/3MwxkwT">
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
                        <span class="twrbo-c-thumb picturefill-background" style="background-image: url(&quot;/content/dam/twrbo/images/creditcard/offer/SPR0001.jpg&quot;); background-size: cover; background-repeat: no-repeat; background-position: 50% 50%;">
                            <span data-src="/content/dam/twrbo/images/creditcard/offer/SPR0001.jpg" data-src-default="/content/dam/twrbo/images/matchCard.png"></span>
                        </span>
                        <div class="twrbo-h-gutters-out-sm-v">
                            <ul class="twrbo-c-label twrbo-c-label--trim">
                                <li ng-show="dealItem.promTag != ''">
                                    <ul class="twrbo-c-label twrbo-c-label--promo twrbo-c-label--trim">
                                        <li>
                                            <i class="twrbo-c-iLabel twrbo-c-iLabel--fire"></i>
                                            <span ng-bind="dealItem.promTag" class="ng-binding">折扣優惠</span>
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
                                <span ng-bind="dealItem.name" class="ng-binding">春河劇團《叫我林彩香！》</span>
                            </span>
                        </div>
                        <div class="twrbo-l-productTextCard">
                            <div class="twrbo-l-productTextCard__detail">
                                <p><span ng-bind-html="dealItem.promDesc" class="ng-binding">網路購票刷中信卡（含簽帳卡），享9折優惠</span></p>
                                <div class="twrbo-h-margin-top-sm">
                                    <ul class="twrbo-c-list twrbo-c-list--data twrbo-c-list--small twrbo-c-list--small">
                                        <li ng-show="dealItem.startDay != '' &amp;&amp; dealItem.endDay != ''">
                                            <div class="twrbo-c-additionalicon">
                                                <img src="/content/dam/twrbo/images/icon/icon_clock_dark.svg" alt="" width="16" height="16">
                                                <span ng-bind="dealItem.startDay" class="ng-binding">2023/10/02</span>
                                                <span>~</span>
                                                <span ng-bind="dealItem.endDay" class="ng-binding">2023/11/18</span>
                                            </div>
                                        </li>
                                        <li ng-show="dealItem.hasOwnProperty('B') &amp;&amp; dealItem.B.length > 0">
                                            <div class="twrbo-c-additionalicon">
                                                <img src="/content/dam/twrbo/images/icon/icon_card_dark.svg" alt="" width="16" height="16">
                                                <span>適用
                                                    <!-- ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">鼎極卡</span>
                                                        <span ng-show="!$last">/</span>
                                                    </span><!-- end ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">鈦金/御璽/晶緻卡</span>
                                                        <span ng-show="!$last">/</span>
                                                    </span><!-- end ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">聯名認同卡</span>
                                                        <span ng-show="!$last">/</span>
                                                    </span><!-- end ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">白金卡以上</span>
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
                                                <li ng-show="dealItem.storeUrl != ''">
                                                    <div class="twrbo-c-additionalicon">
                                                        <img src="/content/dam/twrbo/images/icon/icon_global_dark.svg" alt="" width="16" height="16">
                                                        <a ng-href="https://www.opentix.life/event/1602965254594375682" class="twrbo-h-linkEffect-url--gy" href="https://www.opentix.life/event/1602965254594375682">
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
                        <span class="twrbo-c-thumb picturefill-background" style="background-image: url(&quot;/content/dam/twrbo/images/creditcard/offer/ICE0001.jpg&quot;); background-size: cover; background-repeat: no-repeat; background-position: 50% 50%;">
                            <span data-src="/content/dam/twrbo/images/creditcard/offer/ICE0001.jpg" data-src-default="/content/dam/twrbo/images/matchCard.png"></span>
                        </span>
                        <div class="twrbo-h-gutters-out-sm-v">
                            <ul class="twrbo-c-label twrbo-c-label--trim">
                                <li ng-show="dealItem.promTag != ''">
                                    <ul class="twrbo-c-label twrbo-c-label--promo twrbo-c-label--trim">
                                        <li>
                                            <i class="twrbo-c-iLabel twrbo-c-iLabel--fire"></i>
                                            <span ng-bind="dealItem.promTag" class="ng-binding">折扣優惠</span>
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
                                <span ng-bind="dealItem.name" class="ng-binding">冰上迪士尼 奇幻百年 精彩永恆</span>
                            </span>
                        </div>
                        <div class="twrbo-l-productTextCard">
                            <div class="twrbo-l-productTextCard__detail">
                                <p><span ng-bind-html="dealItem.promDesc" class="ng-binding">網路購票刷中信卡享95折優惠(限前四高票價)</span></p>
                                <div class="twrbo-h-margin-top-sm">
                                    <ul class="twrbo-c-list twrbo-c-list--data twrbo-c-list--small twrbo-c-list--small">
                                        <li ng-show="dealItem.startDay != '' &amp;&amp; dealItem.endDay != ''">
                                            <div class="twrbo-c-additionalicon">
                                                <img src="/content/dam/twrbo/images/icon/icon_clock_dark.svg" alt="" width="16" height="16">
                                                <span ng-bind="dealItem.startDay" class="ng-binding">2023/08/22</span>
                                                <span>~</span>
                                                <span ng-bind="dealItem.endDay" class="ng-binding">2023/12/03</span>
                                            </div>
                                        </li>
                                        <li ng-show="dealItem.hasOwnProperty('B') &amp;&amp; dealItem.B.length > 0">
                                            <div class="twrbo-c-additionalicon">
                                                <img src="/content/dam/twrbo/images/icon/icon_card_dark.svg" alt="" width="16" height="16">
                                                <span>適用
                                                    <!-- ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">鼎極卡</span>
                                                        <span ng-show="!$last">/</span>
                                                    </span><!-- end ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">鈦金/御璽/晶緻卡</span>
                                                        <span ng-show="!$last">/</span>
                                                    </span><!-- end ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">聯名認同卡</span>
                                                        <span ng-show="!$last">/</span>
                                                    </span><!-- end ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">白金卡以上</span>
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
                                                <li ng-show="dealItem.storeUrl != ''">
                                                    <div class="twrbo-c-additionalicon">
                                                        <img src="/content/dam/twrbo/images/icon/icon_global_dark.svg" alt="" width="16" height="16">
                                                        <a ng-href="https://kham.com.tw/application/UTK02/UTK0201_.aspx?PRODUCT_ID=P093Q0YO#" class="twrbo-h-linkEffect-url--gy" href="https://kham.com.tw/application/UTK02/UTK0201_.aspx?PRODUCT_ID=P093Q0YO#">
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
                        <span class="twrbo-c-thumb picturefill-background" style="background-image: url(&quot;/content/dam/twrbo/images/creditcard/offer/Redeem000002.jpg&quot;); background-size: cover; background-repeat: no-repeat; background-position: 50% 50%;">
                            <span data-src="/content/dam/twrbo/images/creditcard/offer/Redeem000002.jpg" data-src-default="/content/dam/twrbo/images/matchCard.png"></span>
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
                                <span ng-bind="dealItem.name" class="ng-binding">台灣黃帽汽車百貨股份有限公司</span>
                            </span>
                        </div>
                        <div class="twrbo-l-productTextCard">
                            <div class="twrbo-l-productTextCard__detail">
                                <p><span ng-bind-html="dealItem.promDesc" class="ng-binding">*中信卡紅利點數每1,000點折抵NT80元，折抵上限為單筆消費金額20%。</span></p>
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
                                                        <a ng-href="tel:0266000022" target="_parent" class="twrbo-h-linkEffect-url--gy twrbo-c-link--tel" href="tel:0266000022">
                                                            <span ng-bind="dealItem.phone" class="ng-binding">02-6600-0022</span>
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
                                                <li ng-show="dealItem.storeUrl != ''">
                                                    <div class="twrbo-c-additionalicon">
                                                        <img src="/content/dam/twrbo/images/icon/icon_global_dark.svg" alt="" width="16" height="16">
                                                        <a ng-href="http://www.yellowhat.com.tw/" class="twrbo-h-linkEffect-url--gy" href="http://www.yellowhat.com.tw/">
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
                        <span class="twrbo-c-thumb picturefill-background" style="background-image: url(&quot;/content/dam/twrbo/images/creditcard/offer/SPR0002.jpg&quot;); background-size: cover; background-repeat: no-repeat; background-position: 50% 50%;">
                            <span data-src="/content/dam/twrbo/images/creditcard/offer/SPR0002.jpg" data-src-default="/content/dam/twrbo/images/matchCard.png"></span>
                        </span>
                        <div class="twrbo-h-gutters-out-sm-v">
                            <ul class="twrbo-c-label twrbo-c-label--trim">
                                <li ng-show="dealItem.promTag != ''">
                                    <ul class="twrbo-c-label twrbo-c-label--promo twrbo-c-label--trim">
                                        <li>
                                            <i class="twrbo-c-iLabel twrbo-c-iLabel--fire"></i>
                                            <span ng-bind="dealItem.promTag" class="ng-binding">折扣優惠</span>
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
                                <span ng-bind="dealItem.name" class="ng-binding">春河劇團《我妻我母我丈母娘》</span>
                            </span>
                        </div>
                        <div class="twrbo-l-productTextCard">
                            <div class="twrbo-l-productTextCard__detail">
                                <p><span ng-bind-html="dealItem.promDesc" class="ng-binding">網路購票刷中信卡（含簽帳卡），享9折優惠</span></p>
                                <div class="twrbo-h-margin-top-sm">
                                    <ul class="twrbo-c-list twrbo-c-list--data twrbo-c-list--small twrbo-c-list--small">
                                        <li ng-show="dealItem.startDay != '' &amp;&amp; dealItem.endDay != ''">
                                            <div class="twrbo-c-additionalicon">
                                                <img src="/content/dam/twrbo/images/icon/icon_clock_dark.svg" alt="" width="16" height="16">
                                                <span ng-bind="dealItem.startDay" class="ng-binding">2023/10/02</span>
                                                <span>~</span>
                                                <span ng-bind="dealItem.endDay" class="ng-binding">2023/12/10</span>
                                            </div>
                                        </li>
                                        <li ng-show="dealItem.hasOwnProperty('B') &amp;&amp; dealItem.B.length > 0">
                                            <div class="twrbo-c-additionalicon">
                                                <img src="/content/dam/twrbo/images/icon/icon_card_dark.svg" alt="" width="16" height="16">
                                                <span>適用
                                                    <!-- ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">鼎極卡</span>
                                                        <span ng-show="!$last">/</span>
                                                    </span><!-- end ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">鈦金/御璽/晶緻卡</span>
                                                        <span ng-show="!$last">/</span>
                                                    </span><!-- end ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">聯名認同卡</span>
                                                        <span ng-show="!$last">/</span>
                                                    </span><!-- end ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">白金卡以上</span>
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
                                                <li ng-show="dealItem.storeUrl != ''">
                                                    <div class="twrbo-c-additionalicon">
                                                        <img src="/content/dam/twrbo/images/icon/icon_global_dark.svg" alt="" width="16" height="16">
                                                        <a ng-href="https://www.opentix.life/event/1650738768421212163" class="twrbo-h-linkEffect-url--gy" href="https://www.opentix.life/event/1650738768421212163">
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
                        <span class="twrbo-c-thumb picturefill-background" style="background-image: url(&quot;/content/dam/twrbo/images/creditcard/offer/Redeem000003.jpg&quot;); background-size: cover; background-repeat: no-repeat; background-position: 50% 50%;">
                            <span data-src="/content/dam/twrbo/images/creditcard/offer/Redeem000003.jpg" data-src-default="/content/dam/twrbo/images/matchCard.png"></span>
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
                                <span ng-bind="dealItem.name" class="ng-binding">台灣中油</span>
                            </span>
                        </div>
                        <div class="twrbo-l-productTextCard">
                            <div class="twrbo-l-productTextCard__detail">
                                <p><span ng-bind-html="dealItem.promDesc" class="ng-binding">*中油聯名卡紅利點數每100點折抵NT8元，折抵上限為單筆消費金額100%
*中信卡紅利點數每300點折抵NT24元，，折抵上限為單筆消費金額100%</span></p>
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
                                                        <span ng-bind="card.filterItemName" class="ng-binding">鼎極卡</span>
                                                        <span ng-show="!$last">/</span>
                                                    </span><!-- end ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">鈦金/御璽/晶緻卡</span>
                                                        <span ng-show="!$last">/</span>
                                                    </span><!-- end ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">聯名認同卡</span>
                                                        <span ng-show="!$last">/</span>
                                                    </span><!-- end ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">白金卡以上</span>
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
                                                <li ng-show="dealItem.phone != ''">
                                                    <div class="twrbo-c-additionalicon">
                                                        <img src="/content/dam/twrbo/images/icon/icon_phone_dark.svg" alt="" width="16" height="16">
                                                        <a ng-href="tel:0287898989" target="_parent" class="twrbo-h-linkEffect-url--gy twrbo-c-link--tel" href="tel:0287898989">
                                                            <span ng-bind="dealItem.phone" class="ng-binding">02-8789-8989</span>
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
                                                <li ng-show="dealItem.storeUrl != ''">
                                                    <div class="twrbo-c-additionalicon">
                                                        <img src="/content/dam/twrbo/images/icon/icon_global_dark.svg" alt="" width="16" height="16">
                                                        <a ng-href="https://www.cpc.com.tw/" class="twrbo-h-linkEffect-url--gy" href="https://www.cpc.com.tw/">
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
                        <span class="twrbo-c-thumb picturefill-background" style="background-image: url(&quot;/content/dam/twrbo/images/creditcard/offer/53350271B.jpg&quot;); background-size: cover; background-repeat: no-repeat; background-position: 50% 50%;">
                            <span data-src="/content/dam/twrbo/images/creditcard/offer/53350271B.jpg" data-src-default="/content/dam/twrbo/images/matchCard.png"></span>
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
                                        <sapn ng-bind="tag.filterItemName" class="ng-binding">分期0利率</sapn></a>
                                </li><!-- end ngRepeat: tag in dealItem.C -->
                            </ul>
                        </div>
                    </div>
                    <div class="twrbo-l-productCard__text">
                        <div class="twrbo-h-margin-bottom-md">
                            <span class="twrbo-c-h3 twrbo-c-link twrbo-c-link--ignoreEffect">
                                <span ng-bind="dealItem.name" class="ng-binding">美少苓分期0利率</span>
                            </span>
                        </div>
                        <div class="twrbo-l-productTextCard">
                            <div class="twrbo-l-productTextCard__detail">
                                <p><span ng-bind-html="dealItem.promDesc" class="ng-binding">活動期間刷中信卡可享分期0利率優惠，分期期數及條件限制請洽門市人員</span></p>
                                <div class="twrbo-h-margin-top-sm">
                                    <ul class="twrbo-c-list twrbo-c-list--data twrbo-c-list--small twrbo-c-list--small">
                                        <li ng-show="dealItem.startDay != '' &amp;&amp; dealItem.endDay != ''">
                                            <div class="twrbo-c-additionalicon">
                                                <img src="/content/dam/twrbo/images/icon/icon_clock_dark.svg" alt="" width="16" height="16">
                                                <span ng-bind="dealItem.startDay" class="ng-binding">2022/01/01</span>
                                                <span>~</span>
                                                <span ng-bind="dealItem.endDay" class="ng-binding">2024/12/31</span>
                                            </div>
                                        </li>
                                        <li ng-show="dealItem.hasOwnProperty('B') &amp;&amp; dealItem.B.length > 0">
                                            <div class="twrbo-c-additionalicon">
                                                <img src="/content/dam/twrbo/images/icon/icon_card_dark.svg" alt="" width="16" height="16">
                                                <span>適用
                                                    <!-- ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">鼎極卡</span>
                                                        <span ng-show="!$last">/</span>
                                                    </span><!-- end ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">鈦金/御璽/晶緻卡</span>
                                                        <span ng-show="!$last">/</span>
                                                    </span><!-- end ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">聯名認同卡</span>
                                                        <span ng-show="!$last">/</span>
                                                    </span><!-- end ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">白金卡以上</span>
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
                                                <li ng-show="dealItem.storeUrl != ''">
                                                    <div class="twrbo-c-additionalicon">
                                                        <img src="/content/dam/twrbo/images/icon/icon_global_dark.svg" alt="" width="16" height="16">
                                                        <a ng-href="https://m.facebook.com/106697887613827/" class="twrbo-h-linkEffect-url--gy" href="https://m.facebook.com/106697887613827/">
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
                        <span class="twrbo-c-thumb picturefill-background" style="background-image: url(&quot;/content/dam/twrbo/images/creditcard/offer/PWS0001.jpg&quot;); background-size: cover; background-repeat: no-repeat; background-position: 50% 50%;">
                            <span data-src="/content/dam/twrbo/images/creditcard/offer/PWS0001.jpg" data-src-default="/content/dam/twrbo/images/matchCard.png"></span>
                        </span>
                        <div class="twrbo-h-gutters-out-sm-v">
                            <ul class="twrbo-c-label twrbo-c-label--trim">
                                <li ng-show="dealItem.promTag != ''">
                                    <ul class="twrbo-c-label twrbo-c-label--promo twrbo-c-label--trim">
                                        <li>
                                            <i class="twrbo-c-iLabel twrbo-c-iLabel--fire"></i>
                                            <span ng-bind="dealItem.promTag" class="ng-binding">折扣優惠</span>
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
                                <span ng-bind="dealItem.name" class="ng-binding">表演工作坊《隱藏的寶藏》</span>
                            </span>
                        </div>
                        <div class="twrbo-l-productTextCard">
                            <div class="twrbo-l-productTextCard__detail">
                                <p><span ng-bind-html="dealItem.promDesc" class="ng-binding">網路購票刷中信卡（含簽帳卡），享95折優惠</span></p>
                                <div class="twrbo-h-margin-top-sm">
                                    <ul class="twrbo-c-list twrbo-c-list--data twrbo-c-list--small twrbo-c-list--small">
                                        <li ng-show="dealItem.startDay != '' &amp;&amp; dealItem.endDay != ''">
                                            <div class="twrbo-c-additionalicon">
                                                <img src="/content/dam/twrbo/images/icon/icon_clock_dark.svg" alt="" width="16" height="16">
                                                <span ng-bind="dealItem.startDay" class="ng-binding">2023/08/25</span>
                                                <span>~</span>
                                                <span ng-bind="dealItem.endDay" class="ng-binding">2023/12/31</span>
                                            </div>
                                        </li>
                                        <li ng-show="dealItem.hasOwnProperty('B') &amp;&amp; dealItem.B.length > 0">
                                            <div class="twrbo-c-additionalicon">
                                                <img src="/content/dam/twrbo/images/icon/icon_card_dark.svg" alt="" width="16" height="16">
                                                <span>適用
                                                    <!-- ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">鼎極卡</span>
                                                        <span ng-show="!$last">/</span>
                                                    </span><!-- end ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">鈦金/御璽/晶緻卡</span>
                                                        <span ng-show="!$last">/</span>
                                                    </span><!-- end ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">聯名認同卡</span>
                                                        <span ng-show="!$last">/</span>
                                                    </span><!-- end ngRepeat: card in dealItem.B --><span ng-repeat="card in dealItem.B" class="ng-scope">
                                                        <span ng-bind="card.filterItemName" class="ng-binding">白金卡以上</span>
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
                                                <li ng-show="dealItem.storeUrl != ''">
                                                    <div class="twrbo-c-additionalicon">
                                                        <img src="/content/dam/twrbo/images/icon/icon_global_dark.svg" alt="" width="16" height="16">
                                                        <a ng-href="https://pwshop.tw/t07Z6yQa" class="twrbo-h-linkEffect-url--gy" href="https://pwshop.tw/t07Z6yQa">
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
                        <span class="twrbo-c-thumb picturefill-background" style="background-image: url(&quot;/content/dam/twrbo/images/creditcard/offer/Redeem000037.jpg&quot;); background-size: cover; background-repeat: no-repeat; background-position: 50% 50%;">
                            <span data-src="/content/dam/twrbo/images/creditcard/offer/Redeem000037.jpg" data-src-default="/content/dam/twrbo/images/matchCard.png"></span>
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
                                <span ng-bind="dealItem.name" class="ng-binding">耐途耐汽車事業有限公司</span>
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
                                                        <a ng-href="tel:0282286318" target="_parent" class="twrbo-h-linkEffect-url--gy twrbo-c-link--tel" href="tel:0282286318">
                                                            <span ng-bind="dealItem.phone" class="ng-binding">02-8228-6318</span>
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
                                                <li ng-show="dealItem.storeUrl != ''">
                                                    <div class="twrbo-c-additionalicon">
                                                        <img src="/content/dam/twrbo/images/icon/icon_global_dark.svg" alt="" width="16" height="16">
                                                        <a ng-href="http://www.9to9.com.tw" class="twrbo-h-linkEffect-url--gy" href="http://www.9to9.com.tw">
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
                        <span class="twrbo-c-thumb picturefill-background" style="background-image: url(&quot;/content/dam/twrbo/images/creditcard/offer/Redeem000041.jpg&quot;); background-size: cover; background-repeat: no-repeat; background-position: 50% 50%;">
                            <span data-src="/content/dam/twrbo/images/creditcard/offer/Redeem000041.jpg" data-src-default="/content/dam/twrbo/images/matchCard.png"></span>
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
                                <span ng-bind="dealItem.name" class="ng-binding">墊腳石圖書</span>
                            </span>
                        </div>
                        <div class="twrbo-l-productTextCard">
                            <div class="twrbo-l-productTextCard__detail">
                                <p><span ng-bind-html="dealItem.promDesc" class="ng-binding">*中信卡紅利點數每100點折抵NT8元，折抵上限為單筆消費金額100%。</span></p>
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
                                                        <a ng-href="tel:034255116" target="_parent" class="twrbo-h-linkEffect-url--gy twrbo-c-link--tel" href="tel:034255116">
                                                            <span ng-bind="dealItem.phone" class="ng-binding">03-4255116</span>
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
                                                <li ng-show="dealItem.storeUrl != ''">
                                                    <div class="twrbo-c-additionalicon">
                                                        <img src="/content/dam/twrbo/images/icon/icon_global_dark.svg" alt="" width="16" height="16">
                                                        <a ng-href="http://www.steppingstone.com.tw" class="twrbo-h-linkEffect-url--gy" href="http://www.steppingstone.com.tw">
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
                        <span class="twrbo-c-thumb picturefill-background" style="background-image: url(&quot;/content/dam/twrbo/images/creditcard/offer/Redeem000086.jpg&quot;); background-size: cover; background-repeat: no-repeat; background-position: 50% 50%;">
                            <span data-src="/content/dam/twrbo/images/creditcard/offer/Redeem000086.jpg" data-src-default="/content/dam/twrbo/images/matchCard.png"></span>
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
                                <span ng-bind="dealItem.name" class="ng-binding">中興嘟嘟房停車場</span>
                            </span>
                        </div>
                        <div class="twrbo-l-productTextCard">
                            <div class="twrbo-l-productTextCard__detail">
                                <p><span ng-bind-html="dealItem.promDesc" class="ng-binding">*中信卡紅利點數每10點折抵NT1元，限全額折抵</span></p>
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
                                                        <a ng-href="tel:0226550818" target="_parent" class="twrbo-h-linkEffect-url--gy twrbo-c-link--tel" href="tel:0226550818">
                                                            <span ng-bind="dealItem.phone" class="ng-binding">02-26550818</span>
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
                                                <li ng-show="dealItem.storeUrl != ''">
                                                    <div class="twrbo-c-additionalicon">
                                                        <img src="/content/dam/twrbo/images/icon/icon_global_dark.svg" alt="" width="16" height="16">
                                                        <a ng-href="http://www.dodohome.com.tw" class="twrbo-h-linkEffect-url--gy" href="http://www.dodohome.com.tw">
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
                        <span class="twrbo-c-thumb picturefill-background" style="background-image: url(&quot;/content/dam/twrbo/images/creditcard/offer/Redeem000087.jpg&quot;); background-size: cover; background-repeat: no-repeat; background-position: 50% 50%;">
                            <span data-src="/content/dam/twrbo/images/creditcard/offer/Redeem000087.jpg" data-src-default="/content/dam/twrbo/images/matchCard.png"></span>
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
                                <span ng-bind="dealItem.name" class="ng-binding">台灣聯通停車場</span>
                            </span>
                        </div>
                        <div class="twrbo-l-productTextCard">
                            <div class="twrbo-l-productTextCard__detail">
                                <p><span ng-bind-html="dealItem.promDesc" class="ng-binding">*中信卡紅利點數每10點折抵NT1元，限全額折抵</span></p>
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
                                                        <a ng-href="tel:0225235000" target="_parent" class="twrbo-h-linkEffect-url--gy twrbo-c-link--tel" href="tel:0225235000">
                                                            <span ng-bind="dealItem.phone" class="ng-binding">02-25235000</span>
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
                                                <li ng-show="dealItem.storeUrl != ''">
                                                    <div class="twrbo-c-additionalicon">
                                                        <img src="/content/dam/twrbo/images/icon/icon_global_dark.svg" alt="" width="16" height="16">
                                                        <a ng-href="http://www.taiwan-parking.com.tw" class="twrbo-h-linkEffect-url--gy" href="http://www.taiwan-parking.com.tw">
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
csv_file_path = '中信其他短期優惠1.csv'
csv_columns = ['優惠名稱', '促銷描述', '開始日期', '結束日期', '適用卡片範疇']

with open(csv_file_path, 'w', newline='', encoding='utf-8-sig') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=csv_columns)
    writer.writeheader()
    for data in result_data:
        writer.writerow(data)

print(f'資料已經擷取並保存到 {csv_file_path}')