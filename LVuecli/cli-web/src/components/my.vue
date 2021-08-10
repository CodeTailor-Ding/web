<template>
  <a-layout id="components-layout-demo-basic">
    <a-layout-sider width='350px'>
      <a-descriptions :style="{ padding: '35px'}" title="信息总览" bordered :column=1>
        <a-descriptions-item v-for="(item, index) in sysmsg" :key="index" :label=item[0]>
          {{item[1]}}
        </a-descriptions-item>
      </a-descriptions>
    </a-layout-sider>
    <a-layout>
      <a-row :gutter="[25, 25]" :style="{ padding: '50px', background: '#fff', minHeight: '806px' }">
        <a-col :xs="24" :sm="24" :md="24" :lg="24" :xl="24">
          <a-table :pagination="{ pageSize: 3 }" :columns="customercolumns" :data-source="customerdata" size='middle' :scroll="{ x: 1300 }">
            <template slot="customRender" slot-scope="text, record, index, column">
              <span v-if="searchText && searchedColumn === column.dataIndex">
                <template
                v-for="(fragment, i) in text
                    .toString()
                    .split(new RegExp(`(?<=${searchText})|(?=${searchText})`, 'i'))"
                >
                  <mark
                    v-if="fragment.toLowerCase() === searchText.toLowerCase()"
                    :key="i"
                    class="highlight"
                    >{{ fragment }}</mark>
                  <template v-else>{{ fragment }}</template>
                </template>
              </span>
              <template v-else>
                  {{ text }}
              </template>
            </template>
            <template slot="title">
                客户基本信息
            </template>
          </a-table>
        </a-col>
        <a-col :xs="24" :sm="24" :md="24" :lg="24" :xl="24">
          <a-table :pagination="{ pageSize: 4 }" :columns="tradecolumns" :data-source="tradedata" size='middle' :scroll="{ x: 1300 }">
            <template slot="customRender" slot-scope="text, record, index, column">
              <span v-if="searchText && searchedColumn === column.dataIndex">
                <template
                v-for="(fragment, i) in text
                    .toString()
                    .split(new RegExp(`(?<=${searchText})|(?=${searchText})`, 'i'))"
                >
                  <mark
                    v-if="fragment.toLowerCase() === searchText.toLowerCase()"
                    :key="i"
                    class="highlight"
                    >{{ fragment }}</mark>
                  <template v-else>{{ fragment }}</template>
                </template>
              </span>
              <template v-else>
                  {{ text }}
              </template>
            </template>
            <template slot="title">
                持仓信息
            </template>
          </a-table>
        </a-col>
      </a-row>
    </a-layout>
  </a-layout>
  
</template>

<script>
const customercolumns = [
  {
    title: '序号',
    dataIndex: 'index',
    key: 'index',
    width: 50,
    fixed: 'left',
    customRender:(text,record,index)=>`${index+1}`,
  },
  {
    title: '客户名称',
    dataIndex: 'name',
    width: 110,
    fixed: 'left',
  },
  {
    title: '客户代码',
    dataIndex: 'code',
  },
  {
    title: '客户状态',
    dataIndex: 'status',
  },
  {
    title: '客户风险等级',
    dataIndex: 'risk',
  },
  {
    title: '机构标志',
    dataIndex: 'sign',
  },
  {
    title: '投资者类型',
    dataIndex: 'classify',
  },
];
const customerdata = [];
for (let i =0; i < 21; ++i){
  customerdata.push({
    key: `${i}`,
    name: `客户${i}`,
    code: `00000${i}`,
    status: '正常',
    risk: -1,
    sign: -1,
    classify: -1,
  })
}
const tradedata = [];
for (let i =0; i < 20; ++i){
  tradedata.push({
    key: `${i}`,
    name: `中国人民银行${i}`,
    code: `00000${i}`,
    position: 500,
    AvailableForSale: 500,
    CostPrice: 20,
    LatestPrice: 30,
    Floating: '10%',
    MarketValue: 10000,
    RateOfReturn: '50%',
  })
}
const tradecolumns = [
  {
    title: '序号',
    dataIndex: 'index',
    key: 'index',
    width: 50,
    fixed: 'left',
    customRender:(text,record,index)=>`${index+1}`,
  },
  {
    title: '证券名称',
    dataIndex: 'name',
    width: 120,
    fixed: 'left',
  },
  {
    title: '证券代码',
    dataIndex: 'code',
  },
  {
    title: '总持仓',
    dataIndex: 'position',
  },
  {
    title: '可卖数',
    dataIndex: 'AvailableForSale',
  },
  {
    title: '成本价',
    dataIndex: 'CostPrice',
  },
  {
    title: '最新价',
    dataIndex: 'LatestPrice',
  },
  {
    title: '浮盈',
    dataIndex: 'Floating',
  },
  {
    title: '市值',
    dataIndex: 'MarketValue',
  },
  {
    title: '收益率',
    dataIndex: 'RateOfReturn',
  },
];
export default {
    name: 'my',
    data() {
        return {
            sysmsg: {
                "Assets": ['总资产', 10000000.0],
                "MarketCapitalization": ['总市值', 200000000.0],
                "FloatingProfit": ['总浮盈', 21321],
                "CurrentBalance": ['当前余额', 213213],
                "AvailableFunds": ['可用资金', 231323],
                "numberOfCustomers": ['客户数量', 21]
            },
            customerdata,
            tradedata,
            // customerdata: [
            //   {
            //     key: '1',
            //     name: '客户1',
            //     code: '000001',
            //     status: '正常',
            //     risk: -1,
            //     sign: -1,
            //     classify: -1,
            //   },
            //   {
            //     key: '2',
            //     name: '客户2',
            //     code: '000002',
            //     status: '正常',
            //     risk: -1,
            //     sign: -1,
            //     classify: -1,
            //   },
            //   {
            //     key: '3',
            //     name: '客户3',
            //     code: '000003',
            //     status: '正常',
            //     risk: -1,
            //     sign: -1,
            //     classify: -1,
            //   }
            // ],
            // tradedata: [
            //   {
            //     key: '1',
            //     name: '中国人民银行1',
            //     code: '000001',
            //     position: 500,
            //     AvailableForSale: 500,
            //     CostPrice: 20,
            //     LatestPrice: 30,
            //     Floating: '10%',
            //     MarketValue: 10000,
            //     RateOfReturn: '50%',
            //   },
            //   {
            //     key: '2',
            //     name: '中国人民银行2',
            //     code: '000002',
            //     position: 500,
            //     AvailableForSale: 500,
            //     CostPrice: 20,
            //     LatestPrice: 30,
            //     Floating: '10%',
            //     MarketValue: 10000,
            //     RateOfReturn: '50%',
            //   },
            //   {
            //     key: '3',
            //     name: '中国人民银行3',
            //     code: '000003',
            //     position: 500,
            //     AvailableForSale: 500,
            //     CostPrice: 20,
            //     LatestPrice: 30,
            //     Floating: '10%',
            //     MarketValue: 10000,
            //     RateOfReturn: '50%',
            //   },
            //   {
            //     key: '4',
            //     name: '中国人民银行4',
            //     code: '000004',
            //     position: 500,
            //     AvailableForSale: 500,
            //     CostPrice: 20,
            //     LatestPrice: 30,
            //     Floating: '10%',
            //     MarketValue: 10000,
            //     RateOfReturn: '50%',
            //   }
            // ],
            customercolumns,
            tradecolumns,
        };
    },
    methods: {

    }
}
</script>

<style>
#components-layout-demo-basic {
  text-align: center;
  background: #fff;
  min-height: 850px;
}
#components-layout-demo-basic .ant-layout-sider {
  background: #ffffff00;
  color: rgb(255, 255, 255);
  line-height: 120px;
}
</style>