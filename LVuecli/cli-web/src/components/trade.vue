<template>
  <a-tabs type="card" @change="callback" class="trade-tabs">
        <a-tab-pane key="1" tab="普通交易">
        <a-row :gutter="[10, 10]" :style="{ padding: '10px', background: '#fff', minHeight: '560px' }">
            <a-col :xs="24" :sm="24" :md="24" :lg="24" :xl="16">
            <a-table :columns="columns" :data-source="data" size='middle' :scroll="{ x: 1300 }">
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
            <a-col :xs="24" :sm="12" :md="12" :lg="12" :xl="4">
                <a-card title="交易" style="width: 100%;" :headStyle="{height:'30px',fontSize:'16px'}" :bodyStyle="{padding:'0'}" >
                    <a-form-model
                        ref="ruleForm"
                        :model="form"
                        :rules="rules"
                        :label-col="labelCol"
                        :wrapper-col="wrapperCol"
                    >
                        <a-form-model-item ref="name" label="证券名称" prop="name" :colon="false">
                            <span style="margin:0 10px">{{form.name}}</span>
                        </a-form-model-item>
                        <a-form-model-item ref="instrument" label="证券代码" prop="instrument" :colon="false">
                            <a-input
                                v-model="form.instrument"
                                @blur="
                                () => {
                                    $refs.instrument.onFieldBlur();
                                }
                                "
                            />
                        </a-form-model-item>
                        <a-form-model-item  prop="ins" :wrapper-col="{ span: 14, offset: 8 }">
                            <a-radio-group v-model="form.ins" >
                                <a-radio value=".SHA">
                                上证A
                                </a-radio>
                                <a-radio value=".SZA">
                                深证A
                                </a-radio>
                            </a-radio-group>
                        </a-form-model-item>
                        <a-form-model-item label="委托类型" prop="type" :colon="false">
                            <a-select v-model="form.type" placeholder="请选择委托类型">
                                <a-select-option value="limit">
                                限价
                                </a-select-option>
                                <a-select-option value="best">
                                对方最优剩余限价
                                </a-select-option>
                            </a-select>
                        </a-form-model-item>
                        
                        <a-form-model-item label="委托价格" prop="price" :colon="false">
                            <a-input-number
                                :v-model="form.price"
                                :default-value="1000"
                                :formatter="value => `$ ${value}`.replace(/\B(?=(\d{3})+(?!\d))/g, ',')"
                                :parser="value => value.replace(/\$\s?|(,*)/g, '')"
                                style="width:130px"
                            /> (元)
                            
                        </a-form-model-item>
                        <a-form-model-item label="委托数量" prop="amount" :colon="false">
                            <a-input-number
                                :v-model="form.amount"
                                :default-value="100"
                                :formatter="value => `${value}`.replace(/\B(?=(\d{3})+(?!\d))/g, ',')"
                                :parser="value => value.replace(/\$\s?|(,*)/g, '')"
                                style="width:130px"
                            /> (股)
                            
                        </a-form-model-item>
                        <a-form-model-item :wrapper-col="{ span: 20, offset: 3 }">
                            <a-row>
                                <a-col :span="12" style="line-height: 30px;text-align: center;">
                                    <a-button @click="onSubmit">
                                        买入(B)
                                    </a-button>  
                                    <span style="display:block;line-height: 20px;color:red;">41651200 [B]</span>
                                    <a-button size="small" style="width:50px;color:red;">
                                        全仓
                                    </a-button>
                                    <a-button size="small" style="margin:0 3px;width:50px;color:red;">
                                        半仓
                                    </a-button>
                                    <a-button size="small" style="width:50px;color:red;">
                                        1/3仓
                                    </a-button>
                                    <a-button size="small" style="margin:0 3px;width:50px;color:red;">
                                        1/4仓
                                    </a-button>
                                </a-col>
                                <a-col :span="12" style="line-height: 30px;text-align: center;">
                                    <a-button @click="resetForm">
                                        卖出(S)
                                    </a-button>
                                    <span style="display:block;line-height: 20px;color:green;">10000200 [S]</span>
                                    <a-button size="small" style="width:50px;color:green;">
                                        全仓
                                    </a-button>
                                    <a-button size="small" style="margin:0 3px;width:50px;color:green;">
                                        半仓
                                    </a-button>
                                    <a-button size="small" style="width:50px;color:green;">
                                        1/3仓
                                    </a-button>
                                    <a-button size="small" style="margin:0 3px;width:50px;color:green;">
                                        1/4仓
                                    </a-button>
                                </a-col>
                            </a-row>
                            
                            
                        </a-form-model-item>
                    </a-form-model>
                </a-card>
            </a-col>
            <a-col :xs="24" :sm="12" :md="12" :lg="12" :xl="4">
                <a-card :title="five_quotations" style="width: 100%" :headStyle="{height:'40px',fontSize:'14px'}" >
                    <a-row type="flex" justify="space-around" align="middle" v-for="item in quotations" :key="item.key" style="margin:3px 0;">
                        <a-divider v-show="item.key==='new'"/>
                        <a-col :span="4">
                            {{item.name}}
                        </a-col>
                        <a-col :span="4" :style="{color:item.color}">
                            {{item.price}}
                        </a-col>
                        <a-col :span="6" :style="{color:item.color}">
                            {{item.amount}}
                        </a-col>
                        <a-divider v-show="item.key==='new'"/>
                    </a-row>
                    <a-divider style="margin-top:8px"/>
                    <a-row type="flex" justify="space-around" align="middle" style="margin:3px 0;">
                        <a-col :span="8" :style="{color:'red'}">
                            涨停价:
                        </a-col>
                        <a-col :span="8" :style="{color:'green'}">
                            跌停价:
                        </a-col>
                    </a-row>
                    <a-row type="flex" justify="space-around" align="middle" style="margin:3px 0;">
                        <a-col :span="8" >
                            前收盘:
                        </a-col>
                        <a-col :span="8" :style="{color:'red'}">
                            涨幅:
                        </a-col>
                    </a-row>
                </a-card>
            </a-col>
        </a-row>
        </a-tab-pane>
        <a-tab-pane key="2" tab="新股/配股">
        Content of Tab Pane 2
        </a-tab-pane>
        <a-tab-pane key="3" tab="ETF申购赎回">
        Content of Tab Pane 3
        </a-tab-pane>
    </a-tabs>
</template>

<script>
const columns = [
  {
    title: '序号',
    dataIndex: 'index',
    key: 'index',
    width: 50,
    fixed: 'left',
    customRender:(text,record,index)=>`${index+1}`,
  },
  {
    title: '名称',
    dataIndex: 'name',
    width: 80,
    fixed: 'left',
  },
  {
    title: '证券代码',
    dataIndex: 'instrument',
    key: 'instrument',
    scopedSlots: {
      filterDropdown: 'filterDropdown',
      filterIcon: 'filterIcon',
      customRender: 'customRender',
    },
    onFilter: (value, record) =>
      record.instrument
        .toString()
        .toLowerCase()
        .includes(value.toLowerCase()),
    onFilterDropdownVisibleChange: visible => {
      if (visible) {
        setTimeout(() => {
          this.searchInput.focus();
        }, 0);
      }
    },
  },
  {
    title: '总持仓',
    dataIndex: 'position',
  },
  {
    title: '可卖',
    dataIndex: 'markrtable',
  },
  {
    title: '累计买',
    dataIndex: 'buy',
  },
  {
    title: '累计卖',
    dataIndex: 'sale',
  },
  {
    title: '成本价',
    dataIndex: 'cost',
  },
  {
    title: '最新价',
    dataIndex: 'price',
  },
  {
    title: '浮盈',
    dataIndex: 'profit',
  },
  {
    title: '市值',
    dataIndex: 'value',
  },
  {
    title: '证券账户',
    dataIndex: 'account',
  },
];
export default {
  name: 'trade',
  data() {
    return {
      searchText: '',
      searchInput: null,
      searchedColumn: '',
      data: [
        {
          key: '1',
          name: '平安银行',
          instrument: '000001',
          position: 1000000,
          markrtable: 10000,
          buy: 0,
          sale: 0,
          cost: 10.90,
          price: 23.90,
          profit: 1200000,
          value: 3242432432.00,
          account: '0212312121'
        }
      ],
      columns,
      five_quotations: '五档行情',
      labelCol: { span: 8 },
      wrapperCol: { span: 14 },
      form: {
        name: '',
        instrument: '',
        ins: '.SHA',
        type: 'limit',
        price: '',
        amount: '',
      },
      rules: {
        type: [{ required: true, message: 'Please select Activity zone', trigger: 'change' }],
      },
      quotations: [
          {
              key:'sale_5',
              name:'卖⑤',
              price: 24.05,
              amount: 3800,
              color: 'red'
          },
          {
              key:'sale_4',
              name:'卖④',
              price: 24.05,
              amount: 3800,
              color: 'red'
          },
          {
              key:'sale_3',
              name:'卖③',
              price: 24.05,
              amount: 3800,
              color: 'red'
          },
          {
              key:'sale_2',
              name:'卖②',
              price: 24.05,
              amount: 3800,
              color: 'red'
          },
          {
              key:'sale_1',
              name:'卖①',
              price: 24.05,
              amount: 3800,
              color: 'red'
          },
          {
              key:'new',
              name:'最新',
              price: 24.00,
              color: 'red'
          },
          {
              key:'buy_1',
              name:'买①',
              price: 23.99,
              amount: 200,
              color: 'red'
          },
          {
              key:'buy_2',
              name:'买②',
              price: 23.99,
              amount: 200,
              color: 'red'
          },
          {
              key:'buy_3',
              name:'买③',
              price: 23.99,
              amount: 200,
              color: 'red'
          },
          {
              key:'buy_4',
              name:'买④',
              price: 23.99,
              amount: 200,
              color: 'red'
          },
          {
              key:'buy_5',
              name:'买⑤',
              price: 23.99,
              amount: 200,
              color: 'red'
          },
      ]
    };
  },
  methods: {
    callback(key) {
      console.log(key);
    },
    handleSearch(selectedKeys, confirm, dataIndex) {
      confirm();
      this.searchText = selectedKeys[0];
      this.searchedColumn = dataIndex;
    },

    handleReset(clearFilters) {
      clearFilters();
      this.searchText = '';
    },
    onSubmit() {
      this.$refs.ruleForm.validate(valid => {
        if (valid) {
          alert('submit!');
        } else {
          console.log('error submit!!');
          return false;
        }
      });
    },
    resetForm() {
      this.$refs.ruleForm.resetFields();
    },
  },
}
</script>

<style scoped>
.highlight {
  background-color: rgb(255, 192, 105);
  padding: 0px;
}

.trade-tabs .ant-form-item {
    margin-bottom:5px;
}

.trade-tabs .ant-divider-horizontal{
    margin: 3px 0;
}
</style>