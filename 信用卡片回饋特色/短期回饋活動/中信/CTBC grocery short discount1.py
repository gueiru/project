import csv
from bs4 import BeautifulSoup

html = """
    <div class="twrbo-l-result__data">
            <div class="twrbo-l-resultList" data-list-id="creditcard" ng-show="isDealListSuccess &amp;&amp; dealList.totalDataRows > 0 ">
                
                <!-- ngRepeat: dealItem in dealList.promotionDetailList --><div ng-repeat="dealItem in dealList.promotionDetailList" class="twrbo-l-productCard twrbo-l-productCard--list ng-scope">
                    <div class="twrbo-l-productCard__thumb">
                        <span class="twrbo-c-thumb picturefill-background" style="background-image: url(&quot;/content/dam/twrbo/images/creditcard/offer/BGR202301.jpg&quot;); background-size: cover; background-repeat: no-repeat; background-position: 50% 50%;">
                            <span data-src="/content/dam/twrbo/images/creditcard/offer/BGR202301.jpg" data-src-default="/content/dam/twrbo/images/matchCard.png"></span>
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
                                </li><!-- end ngRepeat: tag in dealItem.C --><li ng-repeat="tag in dealItem.C" ng-show="dealItem.hasOwnProperty('C')" class="ng-scope">
                                    <a ng-click="onTagClick(tag.filterItemKey, tag.filterItemName)">
                                        <sapn ng-bind="tag.filterItemName" class="ng-binding">消費滿額禮</sapn></a>
                                </li><!-- end ngRepeat: tag in dealItem.C -->
                            </ul>
                        </div>
                    </div>
                    <div class="twrbo-l-productCard__text">
                        <div class="twrbo-h-margin-bottom-md">
                            <span class="twrbo-c-h3 twrbo-c-link twrbo-c-link--ignoreEffect">
                                <span ng-bind="dealItem.name" class="ng-binding">bgreen運動家具雙重送</span>
                            </span>
                        </div>
                        <div class="twrbo-l-productTextCard">
                            <div class="twrbo-l-productTextCard__detail">
                                <p><span ng-bind-html="dealItem.promDesc" class="ng-binding">百貨週年慶期間bgreen專櫃刷中信卡結帳金額滿2萬元贈活力鬆筋拍打棒(價值1,080元)及運動比你想的還輕鬆新書(價值450元)</span></p>
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
                                                        <a ng-href="https://mkt.ctbcbank.com/recent/202312/NB2023091818-31/index.html" class="twrbo-h-linkEffect-url--gy" href="https://mkt.ctbcbank.com/recent/202312/NB2023091818-31/index.html">
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
                        <span class="twrbo-c-thumb picturefill-background" style="background-image: url(&quot;/content/dam/twrbo/images/creditcard/offer/DEP202301.jpg&quot;); background-size: cover; background-repeat: no-repeat; background-position: 50% 50%;">
                            <span data-src="/content/dam/twrbo/images/creditcard/offer/DEP202301.jpg" data-src-default="/content/dam/twrbo/images/matchCard.png"></span>
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
                                        <sapn ng-bind="tag.filterItemName" class="ng-binding">紅利折抵</sapn></a>
                                </li><!-- end ngRepeat: tag in dealItem.C --><li ng-repeat="tag in dealItem.C" ng-show="dealItem.hasOwnProperty('C')" class="ng-scope">
                                    <a ng-click="onTagClick(tag.filterItemKey, tag.filterItemName)">
                                        <sapn ng-bind="tag.filterItemName" class="ng-binding">分期0利率</sapn></a>
                                </li><!-- end ngRepeat: tag in dealItem.C --><li ng-repeat="tag in dealItem.C" ng-show="dealItem.hasOwnProperty('C')" class="ng-scope">
                                    <a ng-click="onTagClick(tag.filterItemKey, tag.filterItemName)">
                                        <sapn ng-bind="tag.filterItemName" class="ng-binding">折扣優惠</sapn></a>
                                </li><!-- end ngRepeat: tag in dealItem.C --><li ng-repeat="tag in dealItem.C" ng-show="dealItem.hasOwnProperty('C')" class="ng-scope">
                                    <a ng-click="onTagClick(tag.filterItemKey, tag.filterItemName)">
                                        <sapn ng-bind="tag.filterItemName" class="ng-binding">消費滿額禮</sapn></a>
                                </li><!-- end ngRepeat: tag in dealItem.C -->
                            </ul>
                        </div>
                    </div>
                    <div class="twrbo-l-productCard__text">
                        <div class="twrbo-h-margin-bottom-md">
                            <span class="twrbo-c-h3 twrbo-c-link twrbo-c-link--ignoreEffect">
                                <span ng-bind="dealItem.name" class="ng-binding">2023年百貨週年慶</span>
                            </span>
                        </div>
                        <div class="twrbo-l-productTextCard">
                            <div class="twrbo-l-productTextCard__detail">
                                <p><span ng-bind-html="dealItem.promDesc" class="ng-binding">中信卡最高回饋13%，百貨消費單筆刷滿1,000元(含)以上，抽bgreen運動養生椅BR2(限量3台，每台價值189,800元)</span></p>
                                <div class="twrbo-h-margin-top-sm">
                                    <ul class="twrbo-c-list twrbo-c-list--data twrbo-c-list--small twrbo-c-list--small">
                                        <li ng-show="dealItem.startDay != '' &amp;&amp; dealItem.endDay != ''">
                                            <div class="twrbo-c-additionalicon">
                                                <img src="/content/dam/twrbo/images/icon/icon_clock_dark.svg" alt="" width="16" height="16">
                                                <span ng-bind="dealItem.startDay" class="ng-binding">2023/09/01</span>
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
                                                        <a ng-href="https://mkt.ctbcbank.com/recent/202312/NB2023092056-30/index.html" class="twrbo-h-linkEffect-url--gy" href="https://mkt.ctbcbank.com/recent/202312/NB2023092056-30/index.html">
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
                        <span class="twrbo-c-thumb picturefill-background" style="background-image: url(&quot;/content/dam/twrbo/images/creditcard/offer/SHOP0922.jpg&quot;); background-size: cover; background-repeat: no-repeat; background-position: 50% 50%;">
                            <span data-src="/content/dam/twrbo/images/creditcard/offer/SHOP0922.jpg" data-src-default="/content/dam/twrbo/images/matchCard.png"></span>
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
                                </li><!-- end ngRepeat: tag in dealItem.C --><li ng-repeat="tag in dealItem.C" ng-show="dealItem.hasOwnProperty('C')" class="ng-scope">
                                    <a ng-click="onTagClick(tag.filterItemKey, tag.filterItemName)">
                                        <sapn ng-bind="tag.filterItemName" class="ng-binding">消費滿額禮</sapn></a>
                                </li><!-- end ngRepeat: tag in dealItem.C -->
                            </ul>
                        </div>
                    </div>
                    <div class="twrbo-l-productCard__text">
                        <div class="twrbo-h-margin-bottom-md">
                            <span class="twrbo-c-h3 twrbo-c-link twrbo-c-link--ignoreEffect">
                                <span ng-bind="dealItem.name" class="ng-binding">UNIQLO、NET、 ZARA</span>
                            </span>
                        </div>
                        <div class="twrbo-l-productTextCard">
                            <div class="twrbo-l-productTextCard__detail">
                                <p><span ng-bind-html="dealItem.promDesc" class="ng-binding">全台【UNIQLO直營店、NET、ZARA、尚智運動、迪卡儂、鞋全家福之獨立實體門市】刷中信卡，單筆消費滿額享回饋。</span></p>
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
                                                        <a ng-href="https://mkt.ctbcbank.com/long/creditcard/NB2023061218/index.html" class="twrbo-h-linkEffect-url--gy" href="https://mkt.ctbcbank.com/long/creditcard/NB2023061218/index.html">
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
                        <span class="twrbo-c-thumb picturefill-background" style="background-image: url(&quot;/content/dam/twrbo/images/creditcard/offer/HGP202301.jpg&quot;); background-size: cover; background-repeat: no-repeat; background-position: 50% 50%;">
                            <span data-src="/content/dam/twrbo/images/creditcard/offer/HGP202301.jpg" data-src-default="/content/dam/twrbo/images/matchCard.png"></span>
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
                                </li><!-- end ngRepeat: tag in dealItem.C --><li ng-repeat="tag in dealItem.C" ng-show="dealItem.hasOwnProperty('C')" class="ng-scope">
                                    <a ng-click="onTagClick(tag.filterItemKey, tag.filterItemName)">
                                        <sapn ng-bind="tag.filterItemName" class="ng-binding">消費滿額禮</sapn></a>
                                </li><!-- end ngRepeat: tag in dealItem.C -->
                            </ul>
                        </div>
                    </div>
                    <div class="twrbo-l-productCard__text">
                        <div class="twrbo-h-margin-bottom-md">
                            <span class="twrbo-c-h3 twrbo-c-link twrbo-c-link--ignoreEffect">
                                <span ng-bind="dealItem.name" class="ng-binding">HAPPY GO</span>
                            </span>
                        </div>
                        <div class="twrbo-l-productTextCard">
                            <div class="twrbo-l-productTextCard__detail">
                                <p><span ng-bind-html="dealItem.promDesc" class="ng-binding">HAPPY GO Pay綁定中信卡，於遠東集團12大通路刷卡滿額享最高回饋10倍點數</span></p>
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
                                                        <a ng-href="https://www.ctbcbank.com/content/dam/minisite/recent/202312/NB2022121912-31/index.html" class="twrbo-h-linkEffect-url--gy" href="https://www.ctbcbank.com/content/dam/minisite/recent/202312/NB2022121912-31/index.html">
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
                        <span class="twrbo-c-thumb picturefill-background" style="background-image: url(&quot;/content/dam/twrbo/images/creditcard/offer/JUST202301.jpg&quot;); background-size: cover; background-repeat: no-repeat; background-position: 50% 50%;">
                            <span data-src="/content/dam/twrbo/images/creditcard/offer/JUST202301.jpg" data-src-default="/content/dam/twrbo/images/matchCard.png"></span>
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
                                </li><!-- end ngRepeat: tag in dealItem.C --><li ng-repeat="tag in dealItem.C" ng-show="dealItem.hasOwnProperty('C')" class="ng-scope">
                                    <a ng-click="onTagClick(tag.filterItemKey, tag.filterItemName)">
                                        <sapn ng-bind="tag.filterItemName" class="ng-binding">消費滿額禮</sapn></a>
                                </li><!-- end ngRepeat: tag in dealItem.C -->
                            </ul>
                        </div>
                    </div>
                    <div class="twrbo-l-productCard__text">
                        <div class="twrbo-h-margin-bottom-md">
                            <span class="twrbo-c-h3 twrbo-c-link twrbo-c-link--ignoreEffect">
                                <span ng-bind="dealItem.name" class="ng-binding">香草集</span>
                            </span>
                        </div>
                        <div class="twrbo-l-productTextCard">
                            <div class="twrbo-l-productTextCard__detail">
                                <p><span ng-bind-html="dealItem.promDesc" class="ng-binding">全台香草集門市/百貨專櫃刷中信卡單筆結帳滿888元送品牌沐浴體驗組(限量5,000份)</span></p>
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
                                                        <a ng-href="https://ctbc.tw/m7XFNT" class="twrbo-h-linkEffect-url--gy" href="https://ctbc.tw/m7XFNT">
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
                        <span class="twrbo-c-thumb picturefill-background" style="background-image: url(&quot;/content/dam/twrbo/images/creditcard/offer/POY202301.jpg&quot;); background-size: cover; background-repeat: no-repeat; background-position: 50% 50%;">
                            <span data-src="/content/dam/twrbo/images/creditcard/offer/POY202301.jpg" data-src-default="/content/dam/twrbo/images/matchCard.png"></span>
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
                                </li><!-- end ngRepeat: tag in dealItem.C --><li ng-repeat="tag in dealItem.C" ng-show="dealItem.hasOwnProperty('C')" class="ng-scope">
                                    <a ng-click="onTagClick(tag.filterItemKey, tag.filterItemName)">
                                        <sapn ng-bind="tag.filterItemName" class="ng-binding">消費滿額禮</sapn></a>
                                </li><!-- end ngRepeat: tag in dealItem.C -->
                            </ul>
                        </div>
                    </div>
                    <div class="twrbo-l-productCard__text">
                        <div class="twrbo-h-margin-bottom-md">
                            <span class="twrbo-c-h3 twrbo-c-link twrbo-c-link--ignoreEffect">
                                <span ng-bind="dealItem.name" class="ng-binding">寶雅POYA</span>
                            </span>
                        </div>
                        <div class="twrbo-l-productTextCard">
                            <div class="twrbo-l-productTextCard__detail">
                                <p><span ng-bind-html="dealItem.promDesc" class="ng-binding">POYA 寶雅APP綁定中信卡，刷卡消費或儲值單筆滿NT899元送寶雅點數10,000點</span></p>
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
                                                        <a ng-href="https://www.ctbcbank.com/content/dam/minisite/recent/202312/NB2022121315-31/index.html" class="twrbo-h-linkEffect-url--gy" href="https://www.ctbcbank.com/content/dam/minisite/recent/202312/NB2022121315-31/index.html">
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
                        <span class="twrbo-c-thumb picturefill-background" style="background-image: url(&quot;/content/dam/twrbo/images/creditcard/offer/Redeem000023.jpg&quot;); background-size: cover; background-repeat: no-repeat; background-position: 50% 50%;">
                            <span data-src="/content/dam/twrbo/images/creditcard/offer/Redeem000023.jpg" data-src-default="/content/dam/twrbo/images/matchCard.png"></span>
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
                                <span ng-bind="dealItem.name" class="ng-binding">勤美 誠品綠園道</span>
                            </span>
                        </div>
                        <div class="twrbo-l-productTextCard">
                            <div class="twrbo-l-productTextCard__detail">
                                <p><span ng-bind-html="dealItem.promDesc" class="ng-binding">*中信卡紅利點數每1,000點折抵NT80元，折抵上限100%。</span></p>
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
                                                        <a ng-href="tel:0423281000" target="_parent" class="twrbo-h-linkEffect-url--gy twrbo-c-link--tel" href="tel:0423281000">
                                                            <span ng-bind="dealItem.phone" class="ng-binding">04-23281000</span>
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
                                                        <a ng-href="https://parklane.com.tw/" class="twrbo-h-linkEffect-url--gy" href="https://parklane.com.tw/">
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
                        <span class="twrbo-c-thumb picturefill-background" style="background-image: url(&quot;/content/dam/twrbo/images/creditcard/offer/Redeem000024.jpg&quot;); background-size: cover; background-repeat: no-repeat; background-position: 50% 50%;">
                            <span data-src="/content/dam/twrbo/images/creditcard/offer/Redeem000024.jpg" data-src-default="/content/dam/twrbo/images/matchCard.png"></span>
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
                                <span ng-bind="dealItem.name" class="ng-binding">金典 綠園道商場</span>
                            </span>
                        </div>
                        <div class="twrbo-l-productTextCard">
                            <div class="twrbo-l-productTextCard__detail">
                                <p><span ng-bind-html="dealItem.promDesc" class="ng-binding">*中信卡紅利點數每1,000點折抵NT80元，折抵上限100%。</span></p>
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
                                                        <a ng-href="tel:0423198000" target="_parent" class="twrbo-h-linkEffect-url--gy twrbo-c-link--tel" href="tel:0423198000">
                                                            <span ng-bind="dealItem.phone" class="ng-binding">04-23198000</span>
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
                                                        <a ng-href="https://parklanes.com.tw/" class="twrbo-h-linkEffect-url--gy" href="https://parklanes.com.tw/">
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
                        <span class="twrbo-c-thumb picturefill-background" style="background-image: url(&quot;/content/dam/twrbo/images/creditcard/offer/Redeem000029.jpg&quot;); background-size: cover; background-repeat: no-repeat; background-position: 50% 50%;">
                            <span data-src="/content/dam/twrbo/images/creditcard/offer/Redeem000029.jpg" data-src-default="/content/dam/twrbo/images/matchCard.png"></span>
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
                                <span ng-bind="dealItem.name" class="ng-binding">台北101購物中心</span>
                            </span>
                        </div>
                        <div class="twrbo-l-productTextCard">
                            <div class="twrbo-l-productTextCard__detail">
                                <p><span ng-bind-html="dealItem.promDesc" class="ng-binding">*101卡聯名卡紅利數點每1,000點折抵NT100元*中信卡紅利點數每1,000點折抵NT80元，折抵上限20%</span></p>
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
                                                        <a ng-href="tel:0281018800" target="_parent" class="twrbo-h-linkEffect-url--gy twrbo-c-link--tel" href="tel:0281018800">
                                                            <span ng-bind="dealItem.phone" class="ng-binding">02-81018800</span>
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
                                                        <a ng-href="https://www.taipei-101.com.tw/" class="twrbo-h-linkEffect-url--gy" href="https://www.taipei-101.com.tw/">
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
                        <span class="twrbo-c-thumb picturefill-background" style="background-image: url(&quot;/content/dam/twrbo/images/creditcard/offer/Redeem000004.jpg&quot;); background-size: cover; background-repeat: no-repeat; background-position: 50% 50%;">
                            <span data-src="/content/dam/twrbo/images/creditcard/offer/Redeem000004.jpg" data-src-default="/content/dam/twrbo/images/matchCard.png"></span>
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
                                <span ng-bind="dealItem.name" class="ng-binding">漢神百貨</span>
                            </span>
                        </div>
                        <div class="twrbo-l-productTextCard">
                            <div class="twrbo-l-productTextCard__detail">
                                <p><span ng-bind-html="dealItem.promDesc" class="ng-binding">*中信卡紅利數點每1,000點折抵NT80元，折抵上限100%</span></p>
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
                                                        <a ng-href="tel:072157266#6801" target="_parent" class="twrbo-h-linkEffect-url--gy twrbo-c-link--tel" href="tel:072157266#6801">
                                                            <span ng-bind="dealItem.phone" class="ng-binding">07-215-7266#6801</span>
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
                                                        <a ng-href="https://www.hanshin.com.tw/" class="twrbo-h-linkEffect-url--gy" href="https://www.hanshin.com.tw/">
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
                        <span class="twrbo-c-thumb picturefill-background" style="background-image: url(&quot;/content/dam/twrbo/images/creditcard/offer/Redeem000032.jpg&quot;); background-size: cover; background-repeat: no-repeat; background-position: 50% 50%;">
                            <span data-src="/content/dam/twrbo/images/creditcard/offer/Redeem000032.jpg" data-src-default="/content/dam/twrbo/images/matchCard.png"></span>
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
                                <span ng-bind="dealItem.name" class="ng-binding">美麗華百樂園</span>
                            </span>
                        </div>
                        <div class="twrbo-l-productTextCard">
                            <div class="twrbo-l-productTextCard__detail">
                                <p><span ng-bind-html="dealItem.promDesc" class="ng-binding">*中信卡紅利數點每1,000點折抵NT80元，折抵上限20%</span></p>
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
                                                        <a ng-href="tel:0221753456" target="_parent" class="twrbo-h-linkEffect-url--gy twrbo-c-link--tel" href="tel:0221753456">
                                                            <span ng-bind="dealItem.phone" class="ng-binding">02-21753456</span>
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
                                                        <a ng-href="http://www.miramar.com.tw/" class="twrbo-h-linkEffect-url--gy" href="http://www.miramar.com.tw/">
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
                        <span class="twrbo-c-thumb picturefill-background" style="background-image: url(&quot;/content/dam/twrbo/images/creditcard/offer/Redeem000033.jpg&quot;); background-size: cover; background-repeat: no-repeat; background-position: 50% 50%;">
                            <span data-src="/content/dam/twrbo/images/creditcard/offer/Redeem000033.jpg" data-src-default="/content/dam/twrbo/images/matchCard.png"></span>
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
                                <span ng-bind="dealItem.name" class="ng-binding">南紡購物中心</span>
                            </span>
                        </div>
                        <div class="twrbo-l-productTextCard">
                            <div class="twrbo-l-productTextCard__detail">
                                <p><span ng-bind-html="dealItem.promDesc" class="ng-binding">*南紡聯名卡/中信卡紅利數點每1,000點折抵NT80元，折抵上限20%。</span></p>
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
                                                        <a ng-href="tel:062366222" target="_parent" class="twrbo-h-linkEffect-url--gy twrbo-c-link--tel" href="tel:062366222">
                                                            <span ng-bind="dealItem.phone" class="ng-binding">06-2366222</span>
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
                                                        <a ng-href="http://www.tsrd.com.tw/" class="twrbo-h-linkEffect-url--gy" href="http://www.tsrd.com.tw/">
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
                        <span class="twrbo-c-thumb picturefill-background" style="background-image: url(&quot;/content/dam/twrbo/images/creditcard/offer/Redeem000034.jpg&quot;); background-size: cover; background-repeat: no-repeat; background-position: 50% 50%;">
                            <span data-src="/content/dam/twrbo/images/creditcard/offer/Redeem000034.jpg" data-src-default="/content/dam/twrbo/images/matchCard.png"></span>
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
                                <span ng-bind="dealItem.name" class="ng-binding">新光三越</span>
                            </span>
                        </div>
                        <div class="twrbo-l-productTextCard">
                            <div class="twrbo-l-productTextCard__detail">
                                <p><span ng-bind-html="dealItem.promDesc" class="ng-binding">*中信卡紅利數點每1,000點折抵NT60元，折抵上限100%</span></p>
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
                                                        <a ng-href="https://www.skm.com.tw/" class="twrbo-h-linkEffect-url--gy" href="https://www.skm.com.tw/">
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
                        <span class="twrbo-c-thumb picturefill-background" style="background-image: url(&quot;/content/dam/twrbo/images/creditcard/offer/Redeem000035.jpg&quot;); background-size: cover; background-repeat: no-repeat; background-position: 50% 50%;">
                            <span data-src="/content/dam/twrbo/images/creditcard/offer/Redeem000035.jpg" data-src-default="/content/dam/twrbo/images/matchCard.png"></span>
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
                                <span ng-bind="dealItem.name" class="ng-binding">環球購物中心</span>
                            </span>
                        </div>
                        <div class="twrbo-l-productTextCard">
                            <div class="twrbo-l-productTextCard__detail">
                                <p><span ng-bind-html="dealItem.promDesc" class="ng-binding">*環球購物聯名卡/中信卡紅利數點每1,000點折抵NT80元，折抵上限20%。</span></p>
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
                                                        <a ng-href="https://www.twglobalmall.com/" class="twrbo-h-linkEffect-url--gy" href="https://www.twglobalmall.com/">
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
                        <span class="twrbo-c-thumb picturefill-background" style="background-image: url(&quot;/content/dam/twrbo/images/creditcard/offer/Redeem000036.jpg&quot;); background-size: cover; background-repeat: no-repeat; background-position: 50% 50%;">
                            <span data-src="/content/dam/twrbo/images/creditcard/offer/Redeem000036.jpg" data-src-default="/content/dam/twrbo/images/matchCard.png"></span>
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
                                <span ng-bind="dealItem.name" class="ng-binding">大葉髙島屋</span>
                            </span>
                        </div>
                        <div class="twrbo-l-productTextCard">
                            <div class="twrbo-l-productTextCard__detail">
                                <p><span ng-bind-html="dealItem.promDesc" class="ng-binding">*大高卡聯名卡紅利數點每1,000點折抵NT100元*中信卡紅利點數每1,000點折抵NT80元，折抵上限100%</span></p>
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
                                                        <a ng-href="tel:0228312345" target="_parent" class="twrbo-h-linkEffect-url--gy twrbo-c-link--tel" href="tel:0228312345">
                                                            <span ng-bind="dealItem.phone" class="ng-binding">02-2831-2345</span>
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
                                                        <a ng-href="http://www.dayeh-takashimaya.com.tw" class="twrbo-h-linkEffect-url--gy" href="http://www.dayeh-takashimaya.com.tw">
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
                        <span class="twrbo-c-thumb picturefill-background" style="background-image: url(&quot;/content/dam/twrbo/images/creditcard/offer/Redeem000076.jpg&quot;); background-size: cover; background-repeat: no-repeat; background-position: 50% 50%;">
                            <span data-src="/content/dam/twrbo/images/creditcard/offer/Redeem000076.jpg" data-src-default="/content/dam/twrbo/images/matchCard.png"></span>
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
                                <span ng-bind="dealItem.name" class="ng-binding">遠東百貨</span>
                            </span>
                        </div>
                        <div class="twrbo-l-productTextCard">
                            <div class="twrbo-l-productTextCard__detail">
                                <p><span ng-bind-html="dealItem.promDesc" class="ng-binding">*中信卡紅利點數每1,000點折抵NT80元，折抵上限100%。</span></p>
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
                                                        <a ng-href="https://www.feds.com.tw/" class="twrbo-h-linkEffect-url--gy" href="https://www.feds.com.tw/">
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
                        <span class="twrbo-c-thumb picturefill-background" style="background-image: url(&quot;/content/dam/twrbo/images/creditcard/offer/Redeem000077.jpg&quot;); background-size: cover; background-repeat: no-repeat; background-position: 50% 50%;">
                            <span data-src="/content/dam/twrbo/images/creditcard/offer/Redeem000077.jpg" data-src-default="/content/dam/twrbo/images/matchCard.png"></span>
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
                                <span ng-bind="dealItem.name" class="ng-binding">漢神巨蛋購物廣場</span>
                            </span>
                        </div>
                        <div class="twrbo-l-productTextCard">
                            <div class="twrbo-l-productTextCard__detail">
                                <p><span ng-bind-html="dealItem.promDesc" class="ng-binding">*中信卡紅利數點每1,000點折抵NT80元，折抵上限100%</span></p>
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
                                                        <a ng-href="tel:0800621688" target="_parent" class="twrbo-h-linkEffect-url--gy twrbo-c-link--tel" href="tel:0800621688">
                                                            <span ng-bind="dealItem.phone" class="ng-binding">0800-621688</span>
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
                                                        <a ng-href="http://www.hanshinarena.com.tw" class="twrbo-h-linkEffect-url--gy" href="http://www.hanshinarena.com.tw">
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
                        <span class="twrbo-c-thumb picturefill-background" style="background-image: url(&quot;/content/dam/twrbo/images/creditcard/offer/Redeem000078.jpg&quot;); background-size: cover; background-repeat: no-repeat; background-position: 50% 50%;">
                            <span data-src="/content/dam/twrbo/images/creditcard/offer/Redeem000078.jpg" data-src-default="/content/dam/twrbo/images/matchCard.png"></span>
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
                                <span ng-bind="dealItem.name" class="ng-binding">統一時代百貨</span>
                            </span>
                        </div>
                        <div class="twrbo-l-productTextCard">
                            <div class="twrbo-l-productTextCard__detail">
                                <p><span ng-bind-html="dealItem.promDesc" class="ng-binding">*中信卡紅利數點每1,000點折抵NT60元，折抵上限20%</span></p>
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
                                                        <a ng-href="tel:0227299699" target="_parent" class="twrbo-h-linkEffect-url--gy twrbo-c-link--tel" href="tel:0227299699">
                                                            <span ng-bind="dealItem.phone" class="ng-binding">02-27299699</span>
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
                                                        <a ng-href="http://www.uni-ustyle.com.tw/" class="twrbo-h-linkEffect-url--gy" href="http://www.uni-ustyle.com.tw/">
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
                        <span class="twrbo-c-thumb picturefill-background" style="background-image: url(&quot;/content/dam/twrbo/images/creditcard/offer/Redeem000079.jpg&quot;); background-size: cover; background-repeat: no-repeat; background-position: 50% 50%;">
                            <span data-src="/content/dam/twrbo/images/creditcard/offer/Redeem000079.jpg" data-src-default="/content/dam/twrbo/images/matchCard.png"></span>
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
                                <span ng-bind="dealItem.name" class="ng-binding">京站時尚廣場</span>
                            </span>
                        </div>
                        <div class="twrbo-l-productTextCard">
                            <div class="twrbo-l-productTextCard__detail">
                                <p><span ng-bind-html="dealItem.promDesc" class="ng-binding">*中信卡紅利數點每1,000點折抵NT60元，折抵上限30%</span></p>
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
                                                        <a ng-href="tel:0800880058" target="_parent" class="twrbo-h-linkEffect-url--gy twrbo-c-link--tel" href="tel:0800880058">
                                                            <span ng-bind="dealItem.phone" class="ng-binding">0800-880058</span>
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
                                                        <a ng-href="https://www.qsquare.com.tw/" class="twrbo-h-linkEffect-url--gy" href="https://www.qsquare.com.tw/">
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
                        <span class="twrbo-c-thumb picturefill-background" style="background-image: url(&quot;/content/dam/twrbo/images/creditcard/offer/Redeem000080.jpg&quot;); background-size: cover; background-repeat: no-repeat; background-position: 50% 50%;">
                            <span data-src="/content/dam/twrbo/images/creditcard/offer/Redeem000080.jpg" data-src-default="/content/dam/twrbo/images/matchCard.png"></span>
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
                                <span ng-bind="dealItem.name" class="ng-binding">廣三SOGO</span>
                            </span>
                        </div>
                        <div class="twrbo-l-productTextCard">
                            <div class="twrbo-l-productTextCard__detail">
                                <p><span ng-bind-html="dealItem.promDesc" class="ng-binding">*中信卡紅利數點每1,000點折抵NT60元，折抵上限20%</span></p>
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
                                                        <a ng-href="tel:0423233788" target="_parent" class="twrbo-h-linkEffect-url--gy twrbo-c-link--tel" href="tel:0423233788">
                                                            <span ng-bind="dealItem.phone" class="ng-binding">04-23233788</span>
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
                                                        <a ng-href="http://www.kssogo.com.tw/" class="twrbo-h-linkEffect-url--gy" href="http://www.kssogo.com.tw/">
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
                        <span class="twrbo-c-thumb picturefill-background" style="background-image: url(&quot;/content/dam/twrbo/images/creditcard/offer/Redeem000081.jpg&quot;); background-size: cover; background-repeat: no-repeat; background-position: 50% 50%;">
                            <span data-src="/content/dam/twrbo/images/creditcard/offer/Redeem000081.jpg" data-src-default="/content/dam/twrbo/images/matchCard.png"></span>
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
                                <span ng-bind="dealItem.name" class="ng-binding">耐斯廣場購物中心</span>
                            </span>
                        </div>
                        <div class="twrbo-l-productTextCard">
                            <div class="twrbo-l-productTextCard__detail">
                                <p><span ng-bind-html="dealItem.promDesc" class="ng-binding">*中信卡紅利數點每1,000點折抵NT60元，折抵上限20%</span></p>
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
                                                        <a ng-href="tel:0809001234" target="_parent" class="twrbo-h-linkEffect-url--gy twrbo-c-link--tel" href="tel:0809001234">
                                                            <span ng-bind="dealItem.phone" class="ng-binding">0809-001234</span>
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
                                                        <a ng-href="http://www.niceplaza.com.tw/" class="twrbo-h-linkEffect-url--gy" href="http://www.niceplaza.com.tw/">
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
                        <span class="twrbo-c-thumb picturefill-background" style="background-image: url(&quot;/content/dam/twrbo/images/creditcard/offer/Redeem000082.jpg&quot;); background-size: cover; background-repeat: no-repeat; background-position: 50% 50%;">
                            <span data-src="/content/dam/twrbo/images/creditcard/offer/Redeem000082.jpg" data-src-default="/content/dam/twrbo/images/matchCard.png"></span>
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
                                <span ng-bind="dealItem.name" class="ng-binding">統一夢時代購物中心</span>
                            </span>
                        </div>
                        <div class="twrbo-l-productTextCard">
                            <div class="twrbo-l-productTextCard__detail">
                                <p><span ng-bind-html="dealItem.promDesc" class="ng-binding">*中信卡紅利數點每1,000點折抵NT60元，折抵上限20%</span></p>
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
                                                        <a ng-href="tel:079733888" target="_parent" class="twrbo-h-linkEffect-url--gy twrbo-c-link--tel" href="tel:079733888">
                                                            <span ng-bind="dealItem.phone" class="ng-binding">07-9733888</span>
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
                                                        <a ng-href="http://www.dreammall.com.tw:10425/" class="twrbo-h-linkEffect-url--gy" href="http://www.dreammall.com.tw:10425/">
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
                        <span class="twrbo-c-thumb picturefill-background" style="background-image: url(&quot;/content/dam/twrbo/images/creditcard/offer/Redeem000083.jpg&quot;); background-size: cover; background-repeat: no-repeat; background-position: 50% 50%;">
                            <span data-src="/content/dam/twrbo/images/creditcard/offer/Redeem000083.jpg" data-src-default="/content/dam/twrbo/images/matchCard.png"></span>
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
                                <span ng-bind="dealItem.name" class="ng-binding">大立百貨</span>
                            </span>
                        </div>
                        <div class="twrbo-l-productTextCard">
                            <div class="twrbo-l-productTextCard__detail">
                                <p><span ng-bind-html="dealItem.promDesc" class="ng-binding">*中信卡紅利數點每1,000點折抵NT60元，折抵上限20%</span></p>
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
                                                        <a ng-href="tel:072613060" target="_parent" class="twrbo-h-linkEffect-url--gy twrbo-c-link--tel" href="tel:072613060">
                                                            <span ng-bind="dealItem.phone" class="ng-binding">07-2613060</span>
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
                                                        <a ng-href="http://www.starplace-talee.com.tw/" class="twrbo-h-linkEffect-url--gy" href="http://www.starplace-talee.com.tw/">
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
                        <span class="twrbo-c-thumb picturefill-background" style="background-image: url(&quot;/content/dam/twrbo/images/creditcard/offer/Redeem000084.jpg&quot;); background-size: cover; background-repeat: no-repeat; background-position: 50% 50%;">
                            <span data-src="/content/dam/twrbo/images/creditcard/offer/Redeem000084.jpg" data-src-default="/content/dam/twrbo/images/matchCard.png"></span>
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
                                <span ng-bind="dealItem.name" class="ng-binding">太平洋百貨豐原店</span>
                            </span>
                        </div>
                        <div class="twrbo-l-productTextCard">
                            <div class="twrbo-l-productTextCard__detail">
                                <p><span ng-bind-html="dealItem.promDesc" class="ng-binding">*中信卡紅利數點每1,000點折抵NT60元，折抵上限20%</span></p>
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
                                                        <a ng-href="tel:0425291111" target="_parent" class="twrbo-h-linkEffect-url--gy twrbo-c-link--tel" href="tel:0425291111">
                                                            <span ng-bind="dealItem.phone" class="ng-binding">04-25291111</span>
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
                                                        <a ng-href="https://fy.pacific-mall.com.tw" class="twrbo-h-linkEffect-url--gy" href="https://fy.pacific-mall.com.tw">
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
                        <span class="twrbo-c-thumb picturefill-background" style="background-image: url(&quot;/content/dam/twrbo/images/creditcard/offer/Redeem000103.jpg&quot;); background-size: cover; background-repeat: no-repeat; background-position: 50% 50%;">
                            <span data-src="/content/dam/twrbo/images/creditcard/offer/Redeem000103.jpg" data-src-default="/content/dam/twrbo/images/matchCard.png"></span>
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
                                <span ng-bind="dealItem.name" class="ng-binding">太平洋百貨屏東店</span>
                            </span>
                        </div>
                        <div class="twrbo-l-productTextCard">
                            <div class="twrbo-l-productTextCard__detail">
                                <p><span ng-bind-html="dealItem.promDesc" class="ng-binding">*中信卡紅利數點每1,000點折抵NT60元，折抵上限20%</span></p>
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
                                                <li ng-show="dealItem.phone != ''" class="ng-hide">
                                                    <div class="twrbo-c-additionalicon">
                                                        <img src="/content/dam/twrbo/images/icon/icon_phone_dark.svg" alt="" width="16" height="16">
                                                        <a ng-href="tel:" target="_parent" class="twrbo-h-linkEffect-url--gy twrbo-c-link--tel" href="tel:">
                                                            <span ng-bind="dealItem.phone" class="ng-binding"></span>
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
                                                        <a ng-href="http://pd.pacific-mall.com.tw" class="twrbo-h-linkEffect-url--gy" href="http://pd.pacific-mall.com.tw">
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
csv_file_path = '中信百貨短期優惠1.csv'
csv_columns = ['優惠名稱', '促銷描述', '開始日期', '結束日期', '適用卡片範疇']

with open(csv_file_path, 'w', newline='', encoding='utf-8-sig') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=csv_columns)
    writer.writeheader()
    for data in result_data:
        writer.writerow(data)

print(f'資料已經擷取並保存到 {csv_file_path}')