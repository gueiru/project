import csv
from bs4 import BeautifulSoup

html = """
    <div class="twrbo-l-result__data">
            <div class="twrbo-l-resultList" data-list-id="creditcard" ng-show="isDealListSuccess &amp;&amp; dealList.totalDataRows > 0 ">
                
                <!-- ngRepeat: dealItem in dealList.promotionDetailList --><div ng-repeat="dealItem in dealList.promotionDetailList" class="twrbo-l-productCard twrbo-l-productCard--list ng-scope">
                    <div class="twrbo-l-productCard__thumb">
                        <span class="twrbo-c-thumb picturefill-background" style="background-image: url(&quot;/content/dam/twrbo/images/creditcard/offer/BQ0926.jpg&quot;); background-size: cover; background-repeat: no-repeat; background-position: 50% 50%;">
                            <span data-src="/content/dam/twrbo/images/creditcard/offer/BQ0926.jpg" data-src-default="/content/dam/twrbo/images/matchCard.png"></span>
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
                                        <sapn ng-bind="tag.filterItemName" class="ng-binding">消費滿額禮</sapn></a>
                                </li><!-- end ngRepeat: tag in dealItem.C -->
                            </ul>
                        </div>
                    </div>
                    <div class="twrbo-l-productCard__text">
                        <div class="twrbo-h-margin-bottom-md">
                            <span class="twrbo-c-h3 twrbo-c-link twrbo-c-link--ignoreEffect">
                                <span ng-bind="dealItem.name" class="ng-binding">特力屋週年慶</span>
                            </span>
                        </div>
                        <div class="twrbo-l-productTextCard">
                            <div class="twrbo-l-productTextCard__detail">
                                <p><span ng-bind-html="dealItem.promDesc" class="ng-binding">刷中信卡滿額享最高500元特力屋電子折價券！</span></p>
                                <div class="twrbo-h-margin-top-sm">
                                    <ul class="twrbo-c-list twrbo-c-list--data twrbo-c-list--small twrbo-c-list--small">
                                        <li ng-show="dealItem.startDay != '' &amp;&amp; dealItem.endDay != ''">
                                            <div class="twrbo-c-additionalicon">
                                                <img src="/content/dam/twrbo/images/icon/icon_clock_dark.svg" alt="" width="16" height="16">
                                                <span ng-bind="dealItem.startDay" class="ng-binding">2023/10/05</span>
                                                <span>~</span>
                                                <span ng-bind="dealItem.endDay" class="ng-binding">2023/11/14</span>
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
                                                        <a ng-href="https://mkt.ctbcbank.com/recent/202311/NB2023091910-14/index.html" class="twrbo-h-linkEffect-url--gy" href="https://mkt.ctbcbank.com/recent/202311/NB2023091910-14/index.html">
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
                        <span class="twrbo-c-thumb picturefill-background" style="background-image: url(&quot;/content/dam/twrbo/images/creditcard/offer/CARREMONEY12.jpg&quot;); background-size: cover; background-repeat: no-repeat; background-position: 50% 50%;">
                            <span data-src="/content/dam/twrbo/images/creditcard/offer/CARREMONEY12.jpg" data-src-default="/content/dam/twrbo/images/matchCard.png"></span>
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
                                        <sapn ng-bind="tag.filterItemName" class="ng-binding">消費滿額禮</sapn></a>
                                </li><!-- end ngRepeat: tag in dealItem.C -->
                            </ul>
                        </div>
                    </div>
                    <div class="twrbo-l-productCard__text">
                        <div class="twrbo-h-margin-bottom-md">
                            <span class="twrbo-c-h3 twrbo-c-link twrbo-c-link--ignoreEffect">
                                <span ng-bind="dealItem.name" class="ng-binding">家樂福錢包</span>
                            </span>
                        </div>
                        <div class="twrbo-l-productTextCard">
                            <div class="twrbo-l-productTextCard__detail">
                                <p><span ng-bind-html="dealItem.promDesc" class="ng-binding">於家樂福實體門市持中信卡儲值家樂福錢包，單筆儲值滿NT1,000元（含）享家樂福錢包儲值金30元。(限量1,000份)</span></p>
                                <div class="twrbo-h-margin-top-sm">
                                    <ul class="twrbo-c-list twrbo-c-list--data twrbo-c-list--small twrbo-c-list--small">
                                        <li ng-show="dealItem.startDay != '' &amp;&amp; dealItem.endDay != ''">
                                            <div class="twrbo-c-additionalicon">
                                                <img src="/content/dam/twrbo/images/icon/icon_clock_dark.svg" alt="" width="16" height="16">
                                                <span ng-bind="dealItem.startDay" class="ng-binding">2023/02/01</span>
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
                                                        <a ng-href="https://www.ctbcbank.com/content/dam/minisite/long/creditcard/carrefourPay/index.html" class="twrbo-h-linkEffect-url--gy" href="https://www.ctbcbank.com/content/dam/minisite/long/creditcard/carrefourPay/index.html">
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
                        <span class="twrbo-c-thumb picturefill-background" style="background-image: url(&quot;/content/dam/twrbo/images/creditcard/offer/Redeem000038.jpg&quot;); background-size: cover; background-repeat: no-repeat; background-position: 50% 50%;">
                            <span data-src="/content/dam/twrbo/images/creditcard/offer/Redeem000038.jpg" data-src-default="/content/dam/twrbo/images/matchCard.png"></span>
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
                                <span ng-bind="dealItem.name" class="ng-binding">聖德科斯生機食品</span>
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
                                                        <a ng-href="tel:0800082880" target="_parent" class="twrbo-h-linkEffect-url--gy twrbo-c-link--tel" href="tel:0800082880">
                                                            <span ng-bind="dealItem.phone" class="ng-binding">0800-082880</span>
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
                                                        <a ng-href="http://www.santacruz.com.tw/" class="twrbo-h-linkEffect-url--gy" href="http://www.santacruz.com.tw/">
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
                        <span class="twrbo-c-thumb picturefill-background" style="background-image: url(&quot;/content/dam/twrbo/images/creditcard/offer/HICAFE0001.jpg&quot;); background-size: cover; background-repeat: no-repeat; background-position: 50% 50%;">
                            <span data-src="/content/dam/twrbo/images/creditcard/offer/HICAFE0001.jpg" data-src-default="/content/dam/twrbo/images/matchCard.png"></span>
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
                                        <sapn ng-bind="tag.filterItemName" class="ng-binding">買一送一</sapn></a>
                                </li><!-- end ngRepeat: tag in dealItem.C -->
                            </ul>
                        </div>
                    </div>
                    <div class="twrbo-l-productCard__text">
                        <div class="twrbo-h-margin-bottom-md">
                            <span class="twrbo-c-h3 twrbo-c-link twrbo-c-link--ignoreEffect">
                                <span ng-bind="dealItem.name" class="ng-binding">萊爾富</span>
                            </span>
                        </div>
                        <div class="twrbo-l-productTextCard">
                            <div class="twrbo-l-productTextCard__detail">
                                <p><span ng-bind-html="dealItem.promDesc" class="ng-binding">週三刷中信卡，指定咖啡享買一送一優惠</span></p>
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
                                                        <a ng-href="https://www.ctbcbank.com/content/dam/minisite/long/creditcard/Hi-cafe/index.html" class="twrbo-h-linkEffect-url--gy" href="https://www.ctbcbank.com/content/dam/minisite/long/creditcard/Hi-cafe/index.html">
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
                        <span class="twrbo-c-thumb picturefill-background" style="background-image: url(&quot;/content/dam/twrbo/images/creditcard/offer/OP0011.jpg&quot;); background-size: cover; background-repeat: no-repeat; background-position: 50% 50%;">
                            <span data-src="/content/dam/twrbo/images/creditcard/offer/OP0011.jpg" data-src-default="/content/dam/twrbo/images/matchCard.png"></span>
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
                                        <sapn ng-bind="tag.filterItemName" class="ng-binding">消費滿額禮</sapn></a>
                                </li><!-- end ngRepeat: tag in dealItem.C -->
                            </ul>
                        </div>
                    </div>
                    <div class="twrbo-l-productCard__text">
                        <div class="twrbo-h-margin-bottom-md">
                            <span class="twrbo-c-h3 twrbo-c-link twrbo-c-link--ignoreEffect">
                                <span ng-bind="dealItem.name" class="ng-binding">OPEN錢包</span>
                            </span>
                        </div>
                        <div class="twrbo-l-productTextCard">
                            <div class="twrbo-l-productTextCard__detail">
                                <p><span ng-bind-html="dealItem.promDesc" class="ng-binding">OPEN錢包綁定中信卡 於指定通路消費滿額享最高10%回饋</span></p>
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
                                                        <a ng-href="https://www.ctbcbank.com/content/dam/minisite/long/creditcard/open/index.html" class="twrbo-h-linkEffect-url--gy" href="https://www.ctbcbank.com/content/dam/minisite/long/creditcard/open/index.html">
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
csv_file_path = '中信超商量販短期優惠1.csv'
csv_columns = ['優惠名稱', '促銷描述', '開始日期', '結束日期', '適用卡片範疇']

with open(csv_file_path, 'w', newline='', encoding='utf-8-sig') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=csv_columns)
    writer.writeheader()
    for data in result_data:
        writer.writerow(data)

print(f'資料已經擷取並保存到 {csv_file_path}')