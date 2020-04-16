import React from 'react'

import { connect } from 'react-redux'
import { query } from '../reducers/query'

import Row from 'react-bootstrap/Row'
import Col from 'react-bootstrap/Col'
import Card from 'react-bootstrap/Card'

import {
  LoadingBox,
  ErrorBox,
  BaseQueryComponent
} from './common'

import Pie from './pie'

class ApprovalStats extends BaseQueryComponent {
  constructor (props) {
    super(props)
    this.state.name = 'changes_top_approval'
    this.state.graph_type = 'approval_stats'
  }

  render () {
    if (!this.props.approval_stats_loading) {
      if (this.props.approval_stats_error) {
        return <ErrorBox
          error={this.props.approval_stats_error}
        />
      }
      const ignoredApproval = [
        'Code-Review+0',
        'Verified+0',
        'Workflow+0',
        'COMMENTED'
      ]
      return (
        <Row>
          <Col>
            <Card>
              <Card.Header>
                <Card.Title>Approvals dispersion stats</Card.Title>
              </Card.Header>
              <Card.Body>
                <Row>
                  <Col>
                    <Pie
                      data={this.props.approval_stats_result}
                      filtered_items={ignoredApproval}
                    />
                  </Col>
                </Row>
              </Card.Body>
            </Card>
          </Col>
        </Row>
      )
    } else {
      return <LoadingBox />
    }
  }
}

const mapStateToProps = state => {
  return {
    approval_stats_loading: state.QueryReducer.approval_stats_loading,
    approval_stats_result: state.QueryReducer.approval_stats_result,
    approval_stats_error: state.QueryReducer.approval_stats_error
  }
}

const mapDispatchToProps = dispatch => {
  return {
    handleQuery: (params) => dispatch(query(params))
  }
}

const CApprovalStats = connect(mapStateToProps, mapDispatchToProps)(ApprovalStats)

export {
  CApprovalStats
}
