import React from 'react';

class ExampleWork extends React.Component {
  render() {
    return (
      <section classname="section section--alignCentered section--description">

        { this.props.work.map( (example, idx) => {
            return (
              <ExampleWorkBubble example={example} key={idx} />
            )
          })
        }

      </section>
    )
  }
}

class ExampleWorkBubble extends React.Component {
  render() {
    return (
      <div classname="section__exampleWrapper">
        <div classname="section__example">
          <img alt="example screenshot of a project involving code"
               classname="section__exampleImage"
               src="images/example1.png"/>
          <dl classname="color--cloud">
            <dt classname="section__exampleTitle section__text--centered">
              Work Example
            </dt>
            <dd></dd>
          </dl>
        </div>
      </div>
    )
  }
}
export default ExampleWork;
